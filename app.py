import streamlit as st
import requests

st.set_page_config(page_title="AI Code Review Assistant", page_icon="🤖", layout="wide")

st.title("🤖 AI Code Review Assistant")
st.write("Upload your Python code file, and the AI will provide a detailed review.")

uploaded_file = st.file_uploader("Choose a Python (.py) file", type="py")

if st.button("Review Code"):
    if uploaded_file is not None:
        with st.spinner("The AI is analyzing your code..."):
            try:
                api_url = "http://127.0.0.1:8000/review"
                files = {'code_file': (uploaded_file.name, uploaded_file.getvalue(), 'text/x-python')}
                response = requests.post(api_url, files=files, timeout=120)

                if response.status_code == 200:
                    st.success("Review complete!")
                    review_data = response.json()

                    # --- FULL DISPLAY LOGIC ---
                    st.header("Code Review Summary")

                    col1, col2 = st.columns(2)
                    col1.metric("Readability Score", f"{review_data.get('readability_score', 'N/A')} / 10")
                    col2.metric("Potential Bugs Found", len(review_data.get('potential_bugs', [])))

                    st.subheader("Overall Feedback")
                    st.info(review_data.get('overall_feedback', 'No feedback provided.'))

                    st.subheader("Improvement Suggestions")
                    for suggestion in review_data.get('improvement_suggestions', []):
                        st.warning(f"💡 {suggestion}")
                    
                    st.subheader("Line-by-Line Analysis")
                    with st.expander("Click to see detailed line-by-line feedback"):
                        line_feedback = review_data.get('line_by_line_feedback', [])
                        if not line_feedback:
                            st.write("No line-by-line feedback was provided.")
                        else:
                            for line_review in line_feedback:
                                feedback = line_review.get('feedback', 'No feedback for this line.')
                                st.markdown(f"**Line {line_review.get('line_number', '?')}:** `{line_review.get('code_line', '')}`\n\n*Feedback: {feedback}*")
                                st.divider()
                else:
                    st.error(f"Error from server (Status Code {response.status_code}): {response.text}")

            except requests.exceptions.ConnectionError:
                st.error("Connection Error: Could not connect to the backend.")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please upload a file first.")