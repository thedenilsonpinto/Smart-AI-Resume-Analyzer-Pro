import streamlit as st
from resume_parser import extract_text
from skills import find_skills
from report_generator import create_report
from ai_engine import resume_feedback
from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Smart AI Resume Analyzer Pro",
    page_icon="📄",
    layout="wide"
)
logo = Image.open("assets/logo.png")

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Main Background */

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #0f172a
    );
}

/* Glass Cards */

.metric-card {

    background: rgba(255,255,255,0.08);

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.15);

    padding: 25px;

    border-radius: 20px;

    text-align: center;

    box-shadow: 0 8px 32px rgba(0,0,0,0.3);

    margin-bottom: 15px;
}

/* Titles */

.metric-title {

    font-size: 18px;

    color: white;

    font-weight: bold;
}

/* Values */

.metric-value {

    font-size: 36px;

    color: #38bdf8;

    font-weight: bold;
}

/* Headers */

h1 {

    color: #38bdf8;
}

h2,h3 {

    color: white;
}

/* Upload Box */

[data-testid="stFileUploader"] {

    background: rgba(255,255,255,0.05);

    border-radius: 15px;

    padding: 15px;
}

/* Sidebar */

section[data-testid="stSidebar"] {

    background: #111827;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

col1, col2 = st.columns([1, 4])

with col1:
    st.image(logo, width=150)

with col2:
    st.title(" Smart AI Resume Analyzer Pro")
    st.sidebar.image(
    logo,
    width=180
)
    st.write("Developed by Denilson Pinto B")

st.sidebar.info("""
Developed by Denilson Pinto B 
using Artificial Intelligence.

Smart AI Resume Analyzer Pro 
is an AI-powered application that analyzes resumes,
evaluates ATS compatibility, identifies skills, 
and provides recommendations to improve career opportunities.

""")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div style="
background:rgba(255,255,255,0.08);
backdrop-filter:blur(10px);
padding:25px;
border-radius:20px;
text-align:center;
border:1px solid rgba(255,255,255,0.15);
">

<h1 style="color:#38bdf8;">
🚀 Smart AI Resume Analyzer Pro
</h1>

<p style="color:white;">

Analyze resumes, detect skills,
calculate ATS scores and receive
AI-powered career recommendations.

</p>

<p style="color:#94a3b8;">

Developed by Denilson Pinto B

</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description (Optional)"
)

# --------------------------------------------------
# MAIN APP
# --------------------------------------------------

if uploaded_file:

    text = extract_text(uploaded_file)

    st.subheader("📋 Resume Content")

    with st.expander("View Resume"):
        st.write(text)

    # --------------------------------------------
    # SKILLS
    # --------------------------------------------

    skills = find_skills(text)

    st.subheader("💡 Detected Skills")

    if skills:

        for skill in skills:
            st.success(skill.title())

    else:
        st.warning("No Skills Detected")

    # --------------------------------------------
    # ATS SCORE
    # --------------------------------------------

    score = min(len(skills) * 10, 100)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">
                ATS Score
            </div>
            <div class="metric-value">
                {score}%
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">
                Skills Found
            </div>
            <div class="metric-value">
                {len(skills)}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("📈 Resume Strength")

    st.progress(score)

    if score >= 80:
        st.success("🔥 Excellent Resume")

    elif score >= 60:
        st.warning("⚡ Good Resume")

    else:
        st.error("❌ Needs Improvement")

    # --------------------------------------------
    # REQUIRED SKILLS
    # --------------------------------------------

    required_skills = [
        "python",
        "sql",
        "machine learning",
        "statistics",
        "power bi"
    ]

    missing_skills = []

    for skill in required_skills:

        if skill not in skills:
            missing_skills.append(skill)

    st.subheader("🚀 Missing Skills")

    if missing_skills:

        for skill in missing_skills:
            st.error(skill.title())

    else:
        st.success("No Missing Skills")

    # --------------------------------------------
    # JOB MATCH
    # --------------------------------------------

    match_score = (
        (len(required_skills) - len(missing_skills))
        / len(required_skills)
    ) * 100

    st.subheader("🎯 Job Match Percentage")

    st.progress(int(match_score))

    st.success(f"{match_score:.0f}% Match")

    # --------------------------------------------
    # RESUME GRADE
    # --------------------------------------------

    st.subheader("🏆 Resume Grade")

    if score >= 90:
        grade = "A+"

    elif score >= 80:
        grade = "A"

    elif score >= 70:
        grade = "B+"

    elif score >= 60:
        grade = "B"

    else:
        grade = "Needs Improvement"

    st.success(grade)

    # --------------------------------------------
    # JOB ROLE PREDICTOR
    # --------------------------------------------

    st.subheader("🎯 Predicted Job Role")

    job_role = "General IT Professional"

    if (
        "python" in skills and
        "machine learning" in skills and
        "statistics" in skills
    ):
        job_role = "🤖 Data Scientist"

    elif (
        "python" in skills and
        "machine learning" in skills
    ):
        job_role = "🚀 AI Engineer"

    elif (
        "sql" in skills and
        "power bi" in skills
    ):
        job_role = "📊 Data Analyst"

    elif "python" in skills:
        job_role = "🐍 Python Developer"

    st.success(job_role)

    # --------------------------------------------
    # AI FEEDBACK
    # --------------------------------------------

    st.subheader("🤖 AI Resume Feedback")

    st.info(
        resume_feedback(score)
    )

    # --------------------------------------------
    # CAREER READINESS
    # --------------------------------------------

    career_score = (
        score + match_score
    ) / 2

    st.subheader("🏅 Career Readiness Score")

    st.progress(int(career_score))

    st.success(
        f"{career_score:.0f}% Ready"
    )

    # --------------------------------------------
    # RESUME SUMMARY
    # --------------------------------------------

    st.subheader("📄 Resume Summary")

    summary = f"""
Detected Skills:
{', '.join(skills)}

ATS Score:
{score}

Predicted Role:
{job_role}

Career Readiness:
{career_score:.0f}%
"""

    st.info(summary)

    # --------------------------------------------
    # JOB DESCRIPTION MATCHING
    # --------------------------------------------

    if job_description:

        st.subheader("🎯 Resume vs Job Description")

        jd_skills = find_skills(job_description)

        matched = []

        for skill in jd_skills:

            if skill in skills:
                matched.append(skill)

        jd_match = (
            len(matched)
            / max(len(jd_skills), 1)
        ) * 100

        st.progress(int(jd_match))

        st.success(
            f"JD Match Score: {jd_match:.0f}%"
        )

    # --------------------------------------------
    # SECTION CHECKER
    # --------------------------------------------

    st.subheader("📚 Resume Section Analysis")

    sections = [
        "education",
        "skills",
        "projects",
        "experience",
        "certifications"
    ]

    for section in sections:

        if section in text.lower():
            st.success(f"{section.title()} Found")

        else:
            st.error(f"{section.title()} Missing")

    # --------------------------------------------
    # INTERVIEW QUESTIONS
    # --------------------------------------------

    st.subheader("🎤 Interview Questions")

    questions = []

    if "python" in skills:
        questions.append("Explain Python decorators.")

    if "sql" in skills:
        questions.append("Difference between JOIN and UNION?")

    if "machine learning" in skills:
        questions.append("What is overfitting?")

    if "statistics" in skills:
        questions.append("What is Central Limit Theorem?")

    if "power bi" in skills:
        questions.append("What is DAX in Power BI?")

    for q in questions:
        st.write("•", q)

    # --------------------------------------------
    # RADAR CHART
    # --------------------------------------------

    st.subheader("🕸 Skill Radar Chart")

    categories = {
        "Python": 1 if "python" in skills else 0,
        "SQL": 1 if "sql" in skills else 0,
        "ML": 1 if "machine learning" in skills else 0,
        "Statistics": 1 if "statistics" in skills else 0,
        "Power BI": 1 if "power bi" in skills else 0
    }

    labels = list(categories.keys())
    values = list(categories.values())

    values += values[:1]

    angles = np.linspace(
        0,
        2 * np.pi,
        len(labels),
        endpoint=False
    ).tolist()

    angles += angles[:1]

    fig = plt.figure(figsize=(5, 5))

    ax = plt.subplot(111, polar=True)

    ax.plot(angles, values)

    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])

    ax.set_xticklabels(labels)

    st.pyplot(fig)

    # --------------------------------------------
    # PIE CHART
    # --------------------------------------------

    st.subheader("📊 Skills Analysis")

    found = len(skills)
    missing = len(missing_skills)

    fig2, ax2 = plt.subplots()

    ax2.pie(
        [found, missing],
        labels=["Detected", "Missing"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig2)

    # --------------------------------------------
    # PDF REPORT
    # --------------------------------------------

    st.subheader("📥 Download Report")

    if st.button("Generate PDF Report"):

        pdf_path = create_report(
            score,
            skills,
            missing_skills,
            match_score
        )

        with open(pdf_path, "rb") as file:

            st.download_button(
                "Download Report",
                data=file,
                file_name="Resume_Report.pdf",
                mime="application/pdf"
            )