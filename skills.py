import re

# ----------------------------------------
# SKILLS DATABASE
# ----------------------------------------

skills_database = [

    "python",
    "java",
    "sql",
    "mysql",

    "machine learning",
    "deep learning",
    "data science",
    "statistics",

    "power bi",
    "tableau",
    "excel",

    "tensorflow",
    "pandas",
    "numpy",
    "opencv",

    "streamlit",
    "flask",
    "django",

    "html",
    "css",
    "javascript",
    "react",

    "git",
    "github",

    "artificial intelligence",
    "data analytics",
    "data visualization",

    "scikit-learn",
    "matplotlib",
    "seaborn",

    "mongodb",
    "postgresql",

    "aws",
    "azure",

    "linux",
    "docker"
]

# ----------------------------------------
# SKILL DETECTION FUNCTION
# ----------------------------------------

def find_skills(text):

    if not text:
        return []

    text = text.lower()

    found_skills = []

    for skill in skills_database:

        pattern = r'\b' + re.escape(skill.lower()) + r'\b'

        if re.search(pattern, text):

            found_skills.append(skill)

    return sorted(list(set(found_skills)))