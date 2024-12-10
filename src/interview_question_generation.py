from src.prompt import interview_question_prompt_template
from src.helper import extract_text_from_pdf
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

def get_interview_questions(resume_data,job_description):

    resume_data = extract_text_from_pdf(resume_data)

    model = GoogleGenerativeAI(model="gemini-1.5-flash")
    chain = interview_question_prompt_template | model | StrOutputParser()

    response = chain.invoke({"resume_data": resume_data, "job_description": job_description})

    return response