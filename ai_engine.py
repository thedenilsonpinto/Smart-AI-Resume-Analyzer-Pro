def resume_feedback(score):

    if score >= 90:

        return """
Excellent Resume

✔ Strong ATS Compatibility

✔ Excellent Technical Skill Set

✔ Good Career Readiness

✔ Resume is highly competitive
"""

    elif score >= 75:

        return """
Good Resume

✔ Strong Foundation

✔ Add More Projects

✔ Include Certifications

✔ Improve Resume Keywords
"""

    elif score >= 60:

        return """
Average Resume

✔ Add More Skills

✔ Improve Project Section

✔ Add Internships

✔ Improve ATS Keywords
"""

    else:

        return """
Weak Resume

✔ Add Technical Skills

✔ Add Academic Projects

✔ Add Certifications

✔ Improve Resume Structure
"""