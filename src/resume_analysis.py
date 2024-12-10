import json
from langchain_google_genai import GoogleGenerativeAI
from src.prompt import resume_analysis_prompt_template
from src.helper import extract_text_from_pdf
import re

# Getting resume analysis
def get_resume_analysis(resume_text,job_description):
        
        resume_data = extract_text_from_pdf(resume_text)

    # Trying to get the response from the model
        model = GoogleGenerativeAI(model="gemini-1.5-flash")

        chain = resume_analysis_prompt_template | model 

        response = chain.invoke({"resume_text": resume_data, "job_description": job_description})

        return response