import streamlit as st
import time
import base64
import pandas as pd
import matplotlib.pyplot as plt

from resume_parser import extract_resume_text
from skill_extractor import load_skills_database, extract_skills
from similarity import compute_similarity
from ats_score import calculate_ats_score


st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("AI Resume Analyzer")

st.write("Upload your resume and compare it with a job description to see how well it matches.")


# ---------- PDF PREVIEW FUNCTION ----------

def show_pdf_preview(uploaded_file):

    pdf_bytes = uploaded_file.read()
    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    pdf_display = f"""
        <iframe
        src="data:application/pdf;base64,{base64_pdf}"
        width="100%"
        height="900"
        type="application/pdf">
        </iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)


# ---------- FILE UPLOAD ----------

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])


# ---------- TWO COLUMN LAYOUT ----------

col1, col2 = st.columns(2)

with col1:

    if resume_file:
        st.subheader("Resume Preview")

        show_pdf_preview(resume_file)


with col2:

    job_description = st.text_area(
        "Paste Job Description",
        height=300
    )


# ---------- ANALYZE BUTTON ----------

if st.button("Analyze Resume"):

    if resume_file and job_description:

        progress = st.progress(0)
        status = st.empty()

        status.text("Parsing Resume...")
        progress.progress(20)
        time.sleep(1)

        resume_file.seek(0)
        resume_text = extract_resume_text(resume_file)

        status.text("Loading Skills Database...")
        progress.progress(40)
        time.sleep(1)

        skills_db = load_skills_database()

        status.text("Detecting Skills...")
        progress.progress(60)
        time.sleep(1)

        resume_skills = extract_skills(resume_text, skills_db)
        job_skills = extract_skills(job_description.lower(), skills_db)

        status.text("Matching Job Description...")
        progress.progress(80)
        time.sleep(1)

        match_score = compute_similarity(resume_text, job_description)

        status.text("Calculating ATS Score...")
        progress.progress(100)
        time.sleep(1)

        ats_score = calculate_ats_score(resume_text, resume_skills, skills_db)

        status.success("Analysis Complete")


        missing_skills = list(set(job_skills) - set(resume_skills))


        st.divider()

        st.header("Resume Analysis Dashboard")

        colA, colB = st.columns(2)

        colA.metric("ATS Score", f"{ats_score}%")
        colB.metric("Job Match Score", f"{match_score}%")

        st.divider()


        # ---------- SKILLS ----------

        col3, col4 = st.columns(2)

        with col3:

            st.subheader("Skills Found in Resume")

            if resume_skills:
                st.success(", ".join(resume_skills))
            else:
                st.warning("No skills detected")


        with col4:

            st.subheader("Missing Skills")

            if missing_skills:
                st.error(", ".join(missing_skills))
            else:
                st.success("No missing skills")


        st.divider()


        # ---------- CHART ----------

        # ---------- GRAPHICAL ANALYSIS ----------

        st.subheader("Graphical Analysis")
        col1, col2 = st.columns(2)

        # -------- SCORE COMPARISON --------

        with col1:
            st.write("### ATS vs Job Match Score")
            score_data = pd.DataFrame({
                "Score": [ats_score, match_score]
                }, index=["ATS Score", "Job Match"])
            st.bar_chart(score_data)


        # -------- SKILL COVERAGE PIE --------

        with col2:
            st.write("### Skill Coverage")
            skills_found = len(resume_skills)
            skills_required = len(job_skills)
            missing = len(missing_skills)
            pie_data = [skills_found, missing]
            labels = ["Skills Found", "Missing Skills"]
            fig1, ax1 = plt.subplots()
            ax1.pie(
                pie_data,
                labels=labels,
                autopct='%1.1f%%',
                startangle=90
                )
            ax1.axis('equal')
            st.pyplot(fig1)


        # ---------- SUGGESTIONS ----------

        st.subheader("Suggestions to Improve Resume")

        suggestions = []

        if match_score < 60:
            suggestions.append(
                "Improve alignment with the job description by adding relevant keywords."
            )

        if ats_score < 70:
            suggestions.append(
                "Add more skills and keywords to improve ATS compatibility."
            )

        if missing_skills:
            suggestions.append(
                "Consider adding these skills: "
                + ", ".join(missing_skills[:5])
            )

        if suggestions:

            for s in suggestions:
                st.warning(s)

        else:

            st.success("Your resume is well aligned with the job description.")


    else:

        st.error("Please upload a resume and paste the job description.")