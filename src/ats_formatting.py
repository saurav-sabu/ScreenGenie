# Importing modules
from src.prompt import resume_formatting_prompt_template
from src.helper import extract_text_from_pdf
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Function to get ATS formatting tips
def get_ats_formatting_tips(resume_data):

    # Extracting text from the PDF file
    resume_data = extract_text_from_pdf(resume_data)

    # Creating a model
    model = GoogleGenerativeAI(model="gemini-2.0-flash")

    # Creating a chain
    chain = resume_formatting_prompt_template | model | StrOutputParser()

    # Invoking the chain
    response = chain.invoke({"resume_text": resume_data})

    return response