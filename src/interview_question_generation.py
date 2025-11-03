# Importing modules
from src.prompt import interview_question_prompt_template
from src.helper import extract_text_from_pdf
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Function to get interview questions
def get_interview_questions(resume_data,job_description):

    # Extracting text from the PDF file
    resume_data = extract_text_from_pdf(resume_data)

    # Creating a model
    model = GoogleGenerativeAI(model="gemini-2.0-flash")

    # Creating a chain
    chain = interview_question_prompt_template | model | StrOutputParser()

    # Invoking the chain
    response = chain.invoke({"resume_data": resume_data, "job_description": job_description})

    return response