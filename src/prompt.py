# Importing modules
from langchain_core.prompts import PromptTemplate

# Prompt for resume and job description
resume_job_description_prompt = """
Act as an advanced ATS (Applicant Tracking System) evaluator with expertise in analyzing resumes for technical and competitive roles in fields like:
- Software Engineering
- Data Science
- Data Analysis
- Big Data Engineering
- Software Testing
- DevOps
- Cloud Engineering
- Cybersecurity
- Machine Learning Engineering
- AI Engineering
- Blockchain Engineering
- Quantum Computing
- Full Stack Development
- Frontend Development
- Backend Development
- Mobile Development
- Game Development
- Web Development

Evaluate the provided resume against the given job description, considering:
1. Keyword and skill alignment.
2. Relevance of experience and achievements to the job requirements.
3. Overall compatibility with the job description based on ATS criteria.

Perform the following analysis and respond in the specified Markdown format:

### Inputs:
- Resume: {resume_text}
- Job Description: {job_description}

### Resume Analysis:

   - "JD Match": "percentage between 0-100",
   - "MissingKeywords": ["keyword1", "keyword2", ...],
   - "Profile Summary": "Provide a detailed evaluation of how well the resume aligns with the job description, highlighting strengths, gaps, and specific improvement suggestions to optimize ATS performance."

### Guidelines for Analysis:
- **JD Match**: Use semantic similarity techniques to calculate a compatibility percentage between the resume and the job description.
- **Missing Keywords**: Extract critical skills, tools, or technologies mentioned in the job description but absent in the resume.
- **Profile Summary**: Include an overview of the alignment between the candidate’s profile and job requirements, such as relevant skills, achievements, and areas needing enhancement.

Make your response clear, actionable, and tailored to a highly competitive job market.
"""

# Creating a prompt template
resume_analysis_prompt_template = PromptTemplate(template=resume_job_description_prompt, input_variables=["resume_text", "job_description"])


# Prompt for cover letter
cover_letter_prompt = '''
You are an expert in creating professional and impactful cover letters tailored to specific job roles. Based on the following details, generate a personalized and compelling cover letter that highlights the candidate's strengths, relevant experience, and alignment with the job requirements.

Inputs:
- **Name**: {name}
- **Job Title**: {job_title}
- **Job Description**: {job_description}
- **Company Name**: {company_name}
- **Resume Data**: {resume_data}

Instructions:
1. Start the cover letter with a formal salutation addressed to the hiring manager or company. If no specific name is available, use "Dear Hiring Manager."
2. In the introduction:
   - State the job role being applied for.
   - Briefly express enthusiasm for the position and the company.
   - If available, provide a short description of the company, highlighting its values, mission, or achievements. If no information is available, skip this step.
3. In the body:
   - Highlight key accomplishments and experiences from the candidate’s **resume data** that align with the job description. Focus on achievements that showcase the candidate’s qualifications and skills.
   - Demonstrate knowledge of the company’s goals and how the candidate can contribute to achieving those goals.
4. In the conclusion:
   - Reiterate interest in the role and express a desire to contribute to the company.
   - Include a polite call to action, such as requesting an interview or offering further discussion.
   - Close with a professional sign-off (e.g., "Sincerely," or "Best regards,").
   
The cover letter should be well-structured, grammatically correct, and ready for submission.

---

Here is the sample draft:

Dear [Hiring Manager/Specific Name if available],

I am excited to apply for the [Job Title] position at {company_name}, as advertised in [Job Posting Source/Description if available]. With my background in [Key Expertise or Industry from resume], coupled with a proven track record of [Specific Achievement or Skill from resume], I am eager to contribute to {company_name}'s success.

[Optional: A brief sentence about {company_name}, such as its mission, values, or notable achievements, if available. Otherwise, skip this step.]

In my previous role at [Previous Employer/Project from resume], I [Specific Accomplishment or Responsibility from resume]. My experience in [Relevant Skills or Tools from resume] has prepared me to excel in [Specific Job Requirement from job description].

I have developed strong proficiency in [Key Skills from resume] and am confident in my ability to bring this expertise to {company_name}. I am particularly excited about contributing to [Specific project/goal mentioned in the job description or company’s mission].

I would welcome the opportunity to discuss how my skills and experiences align with the needs of {company_name}. Thank you for considering my application. I look forward to the possibility of contributing to your team's success.

Sincerely,  
[Candidate's Name]  
[Contact Information]

---

### Guidelines for Including Resume Data:
- Extract relevant information from the candidate’s resume {resume_data}, such as **skills**, **accomplishments**, **previous work experience**, and **educational background**.
- Align these details with the **job description** to show how the candidate is a perfect fit for the position.
- If the resume contains any **quantifiable achievements**, highlight them (e.g., "Increased sales by 30%" or "Managed a team of 10").
- If no specific details are available for the company, skip the company description and focus on the job and resume alignment.

---

### Guidelines for the Company Section:
- If information about {company_name} is provided, include a brief and positive description, such as:
  - “{company_name} is known for its innovative approach in [industry].”
  - “As a leader in [specific field], {company_name} is dedicated to [mission/goal].”
- If no information is known , omit this part and continue with the rest of the cover letter.

Make sure the tone is professional yet personable, and emphasize the candidate's unique value to the employer.

'''

# Creating a prompt template
cover_letter_prompt_template = PromptTemplate(template=cover_letter_prompt, input_variables=["resume_data","job_description", "company_name","name","job_title"])


# Prompt for interview questions
interview_question_prompt = '''
You are an expert interviewer skilled in designing personalized and insightful questions. Based on the candidate's resume data and the provided job description, generate a set of interview questions aimed at assessing the candidate’s qualifications, skills, and alignment with the role.

Inputs:
- **Resume Data**: {resume_data}
- **Job Description**: {job_description}

### Instructions:
1. Create 50 interview questions categorized into the following sections:

    - Behavioral Questions: Evaluate the candidate's problem-solving, leadership, and teamwork abilities based on their past experiences.
    - Technical Questions: Test the candidate’s technical proficiency in skills and tools mentioned in the resume or job description.
    - Situational Questions: Present hypothetical job-relevant scenarios to assess decision-making and problem-solving abilities.
    - Role-Specific Questions: Focus on the responsibilities and tasks described in the job description.
    - General and Cultural Fit Questions: Gauge the candidate’s motivation, personality, and alignment with the company culture.

2. Use the {resume_data} to:

    - Reference specific achievements and skills to craft personalized questions.
    - Incorporate relevant experiences and certifications as discussion points.

3. Use the {job_description} to:

    - Align the questions with the role's key responsibilities and required skills.
    - Tailor questions to evaluate the candidate’s readiness for specific tasks or challenges outlined in the job description.

'''

# Creating a prompt template
interview_question_prompt_template = PromptTemplate(template=interview_question_prompt, input_variables=["resume_data","job_description"])


# Prompt for resume formatting
resume_formatting_prompt = """
Act as an expert in resume evaluation for ATS (Applicant Tracking System) optimization, with a focus on making resumes compliant with best practices for a wide range of professional roles, including technical, managerial, and creative fields. 

Evaluate the provided resume based on the following criteria:
1. **Font and Format Consistency**:
   - Check for consistent font styles, sizes, and heading formatting throughout the resume.
   - Ensure proper use of headings (e.g., Experience, Education, Skills) and subheadings.
   - Identify any potential formatting issues that might negatively impact ATS readability.

2. **ATS Optimization**:
   - Evaluate the inclusion of critical keywords for the role based on industry best practices.
   - Ensure the structure is optimized for ATS, including the use of simple, standard section headings and plain text (no images, tables, or unusual formatting).
   - Suggest any missing sections, such as a Skills section or certifications, which can be important for ATS.

3. **Content Quality**:
   - Assess the clarity and impact of the professional summary and experience sections.
   - Suggest improvements in language (e.g., using stronger action verbs, clear bullet points, concise phrasing).
   - Check for redundancy and suggest streamlining where necessary.

4. **Relevance to Industry-Specific Requirements**:
   - Evaluate the alignment of the resume with industry-specific skills and technologies, focusing on the role’s needs.

### Inputs:
- Resume: {resume_text}

### Output in Markdown Format:
   - "ATS Compatibility Score": "percentage between 0-100",
   - "MissingKeywords": ["keyword1", "keyword2", ...],
   - "Formatting Issues": ["issue1", "issue2", ...],
   - "Profile Summary": "Provide a detailed evaluation of how well the resume aligns with ATS criteria, highlighting strengths, weaknesses, and areas of improvement for optimization."

### Guidelines for Analysis:
- **ATS Compatibility Score**: Calculate the percentage of ATS-friendly features in the resume, considering factors like keyword density, simple formatting, and structural consistency.
- **Missing Keywords**: List critical skills, tools, or technologies that should be included for better ATS compatibility.
- **Formatting Issues**: Identify any formatting issues that could prevent the resume from being parsed correctly by ATS systems, such as inconsistent headings, font sizes, or the use of tables/images.
- **Profile Summary**: Provide actionable feedback for improving the resume’s ATS compatibility and content clarity. This may include specific suggestions for enhancing job experience descriptions or restructuring sections for better ATS readability.
"""

# Creating a prompt template
resume_formatting_prompt_template = PromptTemplate(template=resume_formatting_prompt, input_variables=["resume_text"])


# Prompt for resume generation
resume_generation_prompt = """
You are an expert in resume generation for ATS (Applicant Tracking System) optimization, with a focus on making resumes compliant with best practices for a wide range of professional roles, including technical, managerial, and creative fields. 

- Professional Summary
    - Skills
    - Work Experience
    - Education
    - Certifications

    Resume:
    {resume_text}

    Job Description:
    {job_description}
"""

# Creating a prompt template
resume_generation_prompt_template = PromptTemplate(template=resume_generation_prompt, input_variables=["resume_text","job_description"])

# Chatbot prompt
chatbot_prompt = """You are CareerBot, a professional virtual assistant specializing in career-related guidance. Your role is to assist users with:

1. Resume building and optimization.
2. Interview preparation, including generating role-specific questions and answers.
3. Career advice, such as skill-building, certifications, and job application strategies.
4. Job search and professional development tips.

# User Input:
{user}

Always respond with clear, professional, and actionable advice relevant to the user's career. If a query falls outside career-related topics, politely decline with a message like:
'I specialize in career-related topics and cannot assist with this query.'

Focus on providing value specific to the user's job search or professional development needs. Maintain a professional tone, and ensure your responses are concise and relevant."""