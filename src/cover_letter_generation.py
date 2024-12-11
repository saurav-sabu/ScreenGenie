# Importing modules
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from src.prompt import cover_letter_prompt_template
from src.helper import extract_text_from_pdf

# Function to get cover letter
def get_cover_letter(resume_data,job_description,company_name,name,job_title):

    # Extracting text from the PDF file
    resume_data = extract_text_from_pdf(resume_data)

    # Creating a model
    model = GoogleGenerativeAI(model="gemini-1.5-pro")

    # Creating a chain
    chain = cover_letter_prompt_template | model | StrOutputParser()

    # Invoking the chain
    response = chain.invoke({"resume_data": resume_data, "job_description": job_description, "company_name":company_name,"name":name,"job_title":job_title})

    return response
