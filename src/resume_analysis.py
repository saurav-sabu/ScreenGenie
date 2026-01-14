# Importing modules
from langchain_google_genai import GoogleGenerativeAI
from src.prompt import resume_analysis_prompt_template
from src.helper import extract_text_from_pdf
from dotenv import load_dotenv

load_dotenv()

# Getting resume analysis
def get_resume_analysis(resume_text,job_description):
        
    # Extracting text from the PDF file
    resume_data = extract_text_from_pdf(resume_text)

    # Creating a model
    model = GoogleGenerativeAI(model="gemini-2.0-flash")

    # Creating a chain
    chain = resume_analysis_prompt_template | model 

    # Invoking the chain
    response = chain.invoke({"resume_text": resume_data, "job_description": job_description})

    return response