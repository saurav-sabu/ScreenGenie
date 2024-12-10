import streamlit as st
from PIL import Image
import time
import random
from src.cover_letter_generation import get_cover_letter
from src.resume_analysis import get_resume_analysis
from src.helper import create_word_document
from src.interview_question_generation import get_interview_questions
from src.ats_formatting import get_ats_formatting_tips
from src.resume_generation import get_resume_generation


# Set the page configuration
st.set_page_config(
    page_title="ScreenGenie - Your Resume Assistant",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for animations and styling
st.markdown(
    """
    <style>
        @keyframes fadeIn {
            0% {opacity: 0;}
            100% {opacity: 1;}
        }
        .fade-in {
            animation: fadeIn 2s ease-in;
        }
        .main-header {
            text-align: center;
            font-size: 50px;
            color: #FF6347;
            font-weight: bold;
        }
        .sub-header {
            text-align: center;
            font-size: 20px;
            color: #2F4F4F;
        }
        .stButton > button {
            background-color: #FF7F50;
            color: white;
            border-radius: 5px;
            border: none;
        }
        .stButton > button:hover {
            background-color: #FF4500;
        }
        .faq-header {
            font-size: 25px;
            font-weight: bold;
            color: #FF6347;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "📄 Resume Analysis", "📝 Cover Letter Generator", "🎨 ATS Formatting", "💬 Interview Question Generator", "🎨 Resume Generation", "❓ FAQs", "📞 Contact"])

# Header
st.markdown("<div class='main-header fade-in'>Welcome to ScreenGenie ✨</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header fade-in'>Making resume screening feel magical and effortless.</div>", unsafe_allow_html=True)

# Home Page
if page == "🏠 Home":
    st.markdown("<h2 style='text-align:center;'>🎉 Let's Get Started!</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        ScreenGenie simplifies your job application process by analyzing resumes, generating tailored cover letters, and optimizing resumes for ATS systems. 
        Use the sidebar to navigate through the app's features!
        """
    )
    gif_url = "https://media.tenor.com/images/22518735.gif"  # Replace with the direct URL of the GIF
    st.markdown(
        f"""
        <div style="text-align: center;">
        <img src="{gif_url}" alt="ScreenGenie GIF" style="width:50%; height:auto; border-radius:10px;">
    </div>
    """,
        unsafe_allow_html=True,
    )

# Resume Analysis Page
elif page == "📄 Resume Analysis":
    st.header("📄 Upload Your Resume for Analysis")
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    job_description = st.text_area(
        "Enter Job Description",
        placeholder="Paste the job description here to evaluate your resume's relevance."
    )

    generate_btn = st.button("Generate Analysis")

    if generate_btn and uploaded_file and job_description:
        st.success("Resume and Job Description uploaded successfully!")
        with st.spinner("Analyzing your resume against the job description..."):
            response = get_resume_analysis(uploaded_file,job_description)
            st.success("Analysis Complete!")
            word_document = create_word_document(response)
            st.download_button(
                label="Download Resume Analysis as Word Document",
                data=word_document,
                file_name="resume_analysis.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            st.write(response)

    elif not job_description:
        st.warning("Please provide the job description for a detailed analysis.")
    elif not uploaded_file:
        st.warning("Please upload your resume for analysis.")

# Cover Letter Generator Page
elif page == "📝 Cover Letter Generator":
    st.header("📝 Generate a Tailored Cover Letter")
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    if uploaded_file:
        name = st.text_input("Your Name", placeholder="Enter your name")
        job_title = st.text_input("Job Title", placeholder="Enter the job title you're applying for")
        company_name = st.text_input("Company Name", placeholder="Enter the company name")
        job_description = st.text_area("Job Description", placeholder="Enter job description")
        generate_btn = st.button("Generate Cover Letter")

        if generate_btn:
            with st.spinner("Generating your cover letter..."):
                st.success("Cover Letter Generated Successfully!")
                cover_letter = get_cover_letter(uploaded_file,job_description,company_name,name,job_title)
                st.text_area("Your Cover Letter", cover_letter, height=200)

                word_document = create_word_document(cover_letter)

                # Provide download link for Word document
                st.download_button(
                    label="Download Cover Letter as Word Document",
                    data=word_document,
                    file_name="cover_letter.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
    else:
        st.warning("Please upload your resume for analysis first.")

elif page == "🎨 Resume Generation":
    st.header("🎨 Resume Generation")
    uploaded_file = st.file_uploader("Upload your resume for Resume Generation", type=["pdf"])
    job_description = st.text_area("Job Description", placeholder="Enter job description")
    generate_btn = st.button("Generate Resume")
    if generate_btn and uploaded_file and job_description:
        st.success("File uploaded successfully!")
        with st.spinner("Generating your resume..."):
            resume_generation = get_resume_generation(uploaded_file,job_description)
            st.download_button(
                label="Download Resume as Word Document",
                data=resume_generation,
                file_name="resume_generation.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

elif page == "🤖 Live Interview Simulation":
    st.header("🤖 Live Interview Simulation")
    uploaded_file = st.file_uploader("Upload your resume for Resume Generation", type=["pdf"])
    job_description = st.text_area("Job Description", placeholder="Enter job description")
    generate_btn = st.button("Generate Resume")
    if generate_btn and uploaded_file and job_description:
        st.success("File uploaded successfully!")
        with st.spinner("Generating your resume..."):
            resume_generation = get_resume_generation(uploaded_file,job_description)
            st.download_button(
                label="Download Resume as Word Document",
                data=resume_generation,
                file_name="resume_generation.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

# ATS Formatting Page
elif page == "🎨 ATS Formatting Tips":
    st.header("🎨 ATS Formatting Tips")
    ats_file = st.file_uploader("Upload your resume for getting ATS Formatting Tips", type=["pdf"])
    if ats_file:
        st.success("File uploaded successfully!")
        with st.spinner("Optimizing your resume for ATS systems..."):
            ats_formatting_tips = get_ats_formatting_tips(ats_file)
            st.write(ats_formatting_tips)
        st.snow()
        st.markdown("### 🎉 ATS Optimization Complete!")
        st.download_button(
            "📥 Download ATS-Optimized Resume",
            data=ats_file.getvalue(),
            file_name=f"ATS_Optimized_{ats_file.name}",
            mime="application/octet-stream"
        )
    else:
        st.warning("Please upload your resume for ATS formatting.")

# FAQs Page
elif page == "❓ FAQs":
    st.header("❓ Frequently Asked Questions")
    st.markdown("<div class='faq-header'>1. What is ScreenGenie?</div>", unsafe_allow_html=True)
    st.write("ScreenGenie is an all-in-one platform designed to assist job seekers in their career journey. It offers features like personalized cover letter generation, resume analysis, and tailored interview question preparation to help you stand out in the job market.")

    st.markdown("<div class='faq-header'>2. Who can use ScreenGenie?</div>", unsafe_allow_html=True)
    st.write("ScreenGenie is ideal for job seekers at all levels, from fresh graduates to experienced professionals, looking to enhance their job applications and interview preparation.")

    st.markdown("<div class='faq-header'>3. Is my data secure?</div>", unsafe_allow_html=True)
    st.write("Yes, ScreenGenie does not store or share your data. All processing is done securely.")

    st.markdown("<div class='faq-header'>4. Can I use this for free?</div>", unsafe_allow_html=True)
    st.write("Yes, ScreenGenie is free to use!")

    st.markdown("<div class='faq-header'>5. What formats does ScreenGenie support for uploads?</div>", unsafe_allow_html=True)
    st.write("You can upload your resume in PDF format for analysis and generating cover letters or interview questions.")

    st.markdown("<div class='faq-header'>6. How does the Cover Letter Generator work?</div>", unsafe_allow_html=True)
    st.write("Our Cover Letter Generator uses advanced AI to craft personalized and impactful cover letters. It considers your resume, the job description, and the company details to create a tailored cover letter that highlights your strengths.")

    st.markdown("<div class='faq-header'>7. What format can I download the cover letter in?</div>", unsafe_allow_html=True)
    st.write("You can download the cover letter as a Word document for easy editing.")

    st.markdown("<div class='faq-header'>8. What is Resume Analysis, and how does it help me?</div>", unsafe_allow_html=True)
    st.write("The Resume Analysis feature reviews your uploaded resume and evaluates it against the job description. It highlights areas for improvement, missing skills, and formatting suggestions to optimize your resume for ATS systems and hiring managers.")

# Contact Page
elif page == "📞 Contact":
    st.header("📞 Contact Us")
    st.markdown(
        """
        Have questions or need support? Reach out to us:
        - 📧 Email: saurav.sabu9@gmail.com
        - 📞 Phone: +91-8451842018
        - 🌐 Website: [www.screengenie.com](https://www.screengenie.com)
        """
    )
    st.image("https://media.giphy.com/media/xT0GqeSlGSRQutQWCA/giphy.gif", width=150)
    st.success("We’re here to help!")

elif page == "💬 Interview Question Generator":
    st.header("💬 Generate Interview Questions")

    uploaded_file = st.file_uploader("Upload your resume for Interview Question Generation", type=["pdf"])

    if uploaded_file:
        st.success("File uploaded successfully!")
        job_description = st.text_area("Job Description", placeholder="Enter job description")
        generate_btn = st.button("Generate Interview Questions")

        if generate_btn and job_description:
            with st.spinner("Generating interview questions..."):
                interview_questions = get_interview_questions(uploaded_file,job_description)
                st.write(interview_questions)
                word_interview = create_word_document(interview_questions)
                # Provide download link for Word document
                st.download_button(
                    label="💬 Download Interview Questions as Word Document",
                    data=word_interview,
                    file_name="interview_questions.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
        else:
            st.warning("Please provide the job description for interview question generation.")
    else:
        st.warning("Please upload your resume for interview question generation.")

