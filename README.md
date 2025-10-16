

🤖 AI Code Review Assistant
An intelligent, automated code reviewer powered by Google's Gemini AI. This tool analyzes Python code for readability, potential bugs, and best practices, providing instant, detailed feedback through a clean and interactive web interface.

🌟 Key Features
Intelligent Code Analysis: Leverages the power of Large Language Models to provide insightful feedback on code quality.

Detailed Feedback: Get a readability score, a list of potential bugs, optimization suggestions, and a complete line-by-line analysis.

Interactive UI: A simple and intuitive web interface built with Streamlit makes it easy to upload files and view results.

Robust Backend: Powered by a high-performance FastAPI server to handle requests efficiently.

Easy to Run: A simple launcher script starts both the backend and frontend with a single command.

📸 Application Screenshot
Here you can add a screenshot of your beautiful Streamlit application in action!

🛠️ Tech Stack
Backend: Python, FastAPI

Frontend: Streamlit

AI Model: Google Gemini Pro

API Communication: requests

Environment Management: python-dotenv

⚙️ Setup and Installation
Follow these steps to set up and run the project on your local machine.

1. Prerequisites
Python 3.9+

An active Google Gemini API Key. You can get one from Google AI Studio.

2. Clone the Repository
Clone this repository to your local machine:

Bash

git clone https://github.com/chinnivenkatesh/AI-Code-Review-Assistant.git
cd AI-Code-Review-Assistant
3. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

Bash

# Create a virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
4. Install Dependencies
Install all the required Python packages using the requirements.txt file.

Bash

pip install -r requirements.txt
5. Configure Your API Key
Create a file named .env in the root directory of the project. This file will hold your secret API key.

GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
Note: The .gitignore file is configured to prevent your .env file from being uploaded to GitHub.

▶️ How to Run
Once you have completed the setup, you can launch the entire application with a single command using the provided launcher script.

Bash

python run.py
This command will:

Start the FastAPI backend server on http://localhost:8000.

Start the Streamlit frontend UI on http://localhost:8501.

Automatically open the application in your default web browser.

To stop the application, simply press Ctrl+C in the terminal where the script is running.

📂 Project Structure
Here is a brief overview of the key files in this project:

├── api/
│   └── main.py         # The FastAPI backend server and AI logic.
├── app.py              # The Streamlit frontend user interface.
├── run.py              # The launcher script to start both servers.
├── requirements.txt    # A list of all Python package dependencies.
├── .env                # Your secret API key (you must create this).
└── README.md           # This file.

