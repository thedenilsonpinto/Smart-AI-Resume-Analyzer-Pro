from reportlab.pdfgen import canvas


def create_report(
    score,
    skills,
    missing_skills,
    match_score
):

    filename = "Resume_Report.pdf"

    c = canvas.Canvas(filename)

    c.setFont("Helvetica-Bold", 18)

    c.drawString(
        150,
        800,
        "Resume Analysis Report"
    )

    c.setFont("Helvetica", 12)

    c.drawString(
        50,
        760,
        f"ATS Score : {score}%"
    )

    c.drawString(
        50,
        735,
        f"Job Match : {match_score:.0f}%"
    )

    c.drawString(
        50,
        700,
        "Detected Skills:"
    )

    y = 680

    for skill in skills:

        c.drawString(
            70,
            y,
            f"- {skill}"
        )

        y -= 20

    y -= 10

    c.drawString(
        50,
        y,
        "Missing Skills:"
    )

    y -= 20

    for skill in missing_skills:

        c.drawString(
            70,
            y,
            f"- {skill}"
        )

        y -= 20

    c.save()

    return filename