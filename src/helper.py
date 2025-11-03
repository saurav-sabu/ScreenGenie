# Importing modules
import pymupdf4llm
from docx import Document
from io import BytesIO
from langchain_google_genai import ChatGoogleGenerativeAI
from src.prompt import chatbot_prompt
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Extracting text from PDF
def extract_text_from_pdf(file):

    # Checking if the file is not None
    if file is not None:
        save_path = f"./{file.name}"

        # Save the uploaded file to the defined path
        with open(save_path, "wb") as f:
            f.write(file.getbuffer())

        # Extracting text from the PDF file
        text = pymupdf4llm.to_markdown(save_path)    
        return text

    else:
        return None
    
# Creating a word document
def create_word_document(cover_letter):
    # Create a new Document
    doc = Document()
    doc.add_paragraph(cover_letter)
    
    # Save the document to a BytesIO object for downloading
    byte_io = BytesIO()
    doc.save(byte_io)
    byte_io.seek(0)  # Go to the start of the stream
    return byte_io


def initialize_llm_pipeline():

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

    prompt = ChatPromptTemplate.from_messages([
        ("system", chatbot_prompt),
        ("user", "{user}")
    ])

    llm_chain = prompt | llm

    return llm_chain

