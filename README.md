# AI-Resume-Scanner
AI Resume Analyzer – A Python + Streamlit application that scans resumes, extracts skills, compares them with job descriptions, calculates ATS and job match scores, identifies missing skills, and provides visual insights to help improve resumes for specific job roles.

#LIVE DEMO
https://ai-resume-scanner-nou1.onrender.com


# AI Resume Analyzer

An AI-powered web application that analyzes resumes and compares them with job descriptions to evaluate candidate-job compatibility. The system extracts skills from resumes, calculates ATS compatibility scores, identifies missing skills, and provides improvement suggestions through an interactive dashboard.


# Features

* Resume upload and preview (PDF)
* Resume text extraction
* Technical skill detection from resumes
* Job description comparison
* ATS (Applicant Tracking System) compatibility scoring
* Job match percentage calculation
* Missing skills identification
* Resume improvement suggestions
* Interactive dashboard with graphical analysis
* Resume strength indicator


# Dashboard Insights

The application generates a detailed analysis dashboard including:

* ATS compatibility score
* Job match percentage
* Extracted resume skills
* Required job skills
* Missing skills
* Skill gap analysis
* Resume strength indicator
* Visual charts for score comparison and skill coverage


# Technologies Used

Frontend / UI

* Streamlit

Backend

* Python

Libraries

* pdfminer.six – Resume PDF text extraction
* pandas – Data processing
* scikit-learn – TF-IDF and cosine similarity
* matplotlib – Data visualization
* numpy – Numerical operations


# Project Structure


AI-Resume-Analyzer
│
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── similarity.py
├── ats_score.py
│
├── data
│   └── skills_db.csv
│
└── requirements.txt



# How It Works

1. User uploads a resume in PDF format.
2. The system extracts text from the resume.
3. Skills are detected using a predefined skills database.
4. The job description is analyzed to extract required skills.
5. Resume and job description are compared using TF-IDF and cosine similarity.
6. The system calculates:

   * ATS compatibility score
   * Job match percentage
7. Missing skills are identified.
8. Results are displayed in an interactive dashboard with charts and recommendations.





# Example Use Case

Upload a resume and paste a job description such as:

Backend Software Engineer
Skills: Python, Docker, AWS, SQL

The system will analyze the resume and show:

* Job match percentage
* ATS score
* Skills present in resume
* Skills missing for the job
* Suggestions to improve the resume


# Future Improvements

* AI-based semantic skill extraction
* LLM-powered resume feedback
* Resume ranking for multiple candidates
* Interactive skill radar charts
* Integration with job APIs
* Advanced NLP models for job matching
