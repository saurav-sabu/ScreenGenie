from src.prompt import resume_formatting_prompt_template
from src.helper import extract_text_from_pdf
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

def get_ats_formatting_tips(resume_data):

    resume_data = extract_text_from_pdf(resume_data)

    model = GoogleGenerativeAI(model="gemini-1.5-flash")
    chain = resume_formatting_prompt_template | model | StrOutputParser()

    response = chain.invoke({"resume_text": resume_data})

    return response