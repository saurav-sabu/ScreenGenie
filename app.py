import os
import streamlit as st
from src.helper import *
from dotenv import load_dotenv

# Loading environment variables

# Set page configuration
st.set_page_config(
    page_title="Smart ATS Tracking System",
    page_icon=":computer:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background-color: #f9f9f9;
        }
        .title {
            font-size: 3rem;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-top: 20px;
        }
        .header {
            font-size: 1.5rem;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        .sub-header {
            font-size: 1.2rem;
            color: #34495e;
            margin-bottom: 5px;
        }
        .upload-section {
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .analyze-button {
            background-color: #2980b9;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 1rem;
            font-weight: bold;
            margin-top: 20px;
        }
        .analyze-button:hover {
            background-color: #3498db;
        }
        .results-section {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .results-item {
            font-size: 1rem;
            margin-bottom: 10px;
            color: #2c3e50;
        }
        .footer {
            font-size: 0.9rem;
            color: #7f8c8d;
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)


def initialize_session_state():
    if 'processing' not in st.session_state:
        st.session_state.processing = False


def main():
    load_dotenv()
    
    initialize_session_state()


    # App Title
    st.markdown('<div class="title">ScreenGenie - Making resume screening feel magical and effortless</div>', unsafe_allow_html=True)

    # Job Description Section
    st.markdown('<div class="header">Step 1: Enter Job Description</div>', unsafe_allow_html=True)
    job_description = st.text_area(
        "Paste the job description here:", 
        placeholder="e.g., Data Scientist role requiring Python, machine learning, and SQL expertise...",
        height=150
    )

    # Resume Upload Section
    st.markdown('<div class="header">Step 2: Upload Resumes</div>', unsafe_allow_html=True)
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    file = st.file_uploader(
        "Upload resumes in PDF format",
        type="pdf",
        accept_multiple_files=False,
        help="Supported format: PDF"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    resume_text = ""

    # Analyze Button
    if st.button("Analyze Resumes", help="Click to analyze resumes against the job description.",disabled=st.session_state.processing):

        if not job_description:
            st.warning("Please enter a job description before analyzing resumes.")

        if not file:
            st.warning("Please upload at least one resume before analyzing.")

        st.session_state.processing = True

        try:
            with st.spinner("Analyzing resumes..."):

                if file is not None:
                    resume_text = extract_text_from_pdf(file)
                
                input_prompt = prepare_resume_analysis_prompt(resume_text, job_description)

                response = get_resume_analysis(input_prompt,resume_text,job_description)

                response_json = json.loads(response)

                st.success("Analysis complete!")

                match_percentage = response_json.get("JD Match", "N/A")
                st.metric("Job Description Match", f"{match_percentage}%")

                st.subheader("Missing Keywords")
                for keyword in response_json["MissingKeywords"]:
                    if keyword:
                        st.write(keyword)
                    else:
                        st.write("No missing keywords found")

                st.subheader("Profile Summary")
                st.write(response_json["Profile Summary"])

        except Exception as e:
            st.error("Something went wrong 🧐🧐")
            st.error(e)

        finally:
            st.session_state.processing = False

    # Footer
    st.markdown('<div class="footer">Powered by AI | ScreenGenie © 2024</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()








