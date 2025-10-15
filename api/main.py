# 1. All imports go at the top
import os
import json
import google.generativeai as genai
from fastapi import FastAPI, File, UploadFile, HTTPException
from dotenv import load_dotenv

# 2. Load environment variables and configure services
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 3. Create the FastAPI app instance
app = FastAPI(title="AI Code Review Assistant")

# 4. Define your routes
@app.get("/")
def read_root():
    """Provides a simple welcome message for the API root."""
    return {"message": "Welcome to the AI Code Review Assistant API!"}

@app.post("/review")
async def review_code_file(code_file: UploadFile = File(...)):
    """
    Receives a code file, sends it to the Gemini AI for a detailed review,
    and returns the structured feedback as a JSON object.
    """
    code_as_string = (await code_file.read()).decode('utf-8')
    
    prompt = f"""
    You are an expert code reviewer specializing in Python. Analyze the following code snippet.
    Your final output MUST be a single, valid JSON object. Do not wrap it in markdown.
    
    The JSON object should have the following structure:
    {{
      "readability_score": <an integer score from 1 to 10 for readability>,
      "overall_feedback": "<a concise, one-paragraph summary of the code's quality>",
      "potential_bugs": [
        "<a string describing a potential bug>"
      ],
      "improvement_suggestions": [
        "<a string describing a specific optimization or best-practice suggestion>"
      ],
      "line_by_line_feedback": [
        {{
          "line_number": <integer>,
          "code_line": "<the exact line of code>",
          "feedback": "<specific feedback for this line>"
        }}
      ]
    }}

    Here is the code to review:
    ---
    {code_as_string}
    ---
    """
    
    try:
        # IMPORTANT: Use the model name that worked for you!
        model = genai.GenerativeModel('gemini-2.5-pro') 
        response = model.generate_content(prompt)
        
        # Robustly find and extract the JSON object from the AI's response
        response_text = response.text
        start_index = response_text.find('{')
        end_index = response_text.rfind('}') + 1
        
        if start_index == -1 or end_index == 0:
            raise ValueError("Could not find a valid JSON object in the AI's response.")
                
        json_string = response_text[start_index:end_index]
        
        # Parse the cleaned string into a JSON object
        review_json = json.loads(json_string)
        return review_json

    except (json.JSONDecodeError, ValueError) as e:
        error_detail = f"Error parsing AI response: {e}. Raw response was: {response.text}"
        raise HTTPException(status_code=500, detail=error_detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred during AI review: {str(e)}")