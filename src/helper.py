# Importing modules
from langchain_google_genai import GoogleGenerativeAI
from src.prompt import *
import pymupdf4llm
import json
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import os

# Loading environment variables
load_dotenv()

# Extracting text from PDF
def extract_text_from_pdf(file):

    if file is not None:
    # Define the path where you want to save the file
        save_path = f"./{file.name}"

        # Save the uploaded file to the defined path
        with open(save_path, "wb") as f:
            f.write(file.getbuffer())

        text = pymupdf4llm.to_markdown(save_path)    
        return text


# Preparing resume analysis prompt
def prepare_resume_analysis_prompt(resume_text, job_description):
    
    # Checking if resume text is provided
    if not resume_text:
        raise ValueError("No resume text provided.")
    
    # Checking if job description is provided
    elif not job_description:
        raise ValueError("No job description provided.")
    
    # Formatting the prompt
    resume_prompt_template = resume_job_description_prompt

    return resume_prompt_template

# Getting resume analysis
def get_resume_analysis(resume_prompt,resume_text,job_description):
    # Trying to get the response from the model
    try:
        prompt = resume_prompt.format(resume_text=resume_text, job_description=job_description)
        model = GoogleGenerativeAI(model="gemini-1.5-pro")
        response = model.invoke(prompt)

        # print(response)
        # Checking if response is received
        if not response:
            raise ValueError("No response from the model.")
        
        # Loading the response as JSON
        response_json = json.loads(response)

        print(response_json)
        
        # Checking if all required fields are present
        required_keys = ["JD Match", "MissingKeywords", "Profile Summary"]

        # Checking if all required fields are present
        for field in required_keys:
            if field not in response_json:
                raise ValueError(f"Required field '{field}' not found in the response.")
        
        return response.content
    
    # Handling exceptions
    except Exception as e:
        print(f"Error in get_resume_analysis: {e}")
        return None
