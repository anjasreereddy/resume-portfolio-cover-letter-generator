from flask import Flask, render_template, request
from datetime import datetime   # ✅ Added for auto date

app = Flask(__name__)

# ================= DASHBOARD =================
@app.route('/')
def dashboard():
    return render_template("dashboard.html")


# ================= RESUME =================
@app.route('/resume_form', methods=['GET', 'POST'])
def resume_form():
    if request.method == 'POST':
        institutes = request.form.getlist("institute[]")
        degrees = request.form.getlist("degree[]")
        gpas = request.form.getlist("gpa[]")

        education_data = []
        for i in range(len(institutes)):
            education_data.append({
                "institute": institutes[i],
                "degree": degrees[i],
                "gpa": gpas[i]
            })

        return render_template(
            "resume_template.html",
            name=request.form.get("name"),
            role=request.form.get("role"),
            phone=request.form.get("phone"),
            email=request.form.get("email"),
            address=request.form.get("address"),
            skills=request.form.get("skills"),
            languages=request.form.get("languages"),
            profile=request.form.get("profile"),
            websites=request.form.get("websites"),
            certifications=request.form.get("certifications"),
            activities=request.form.get("activities"),
            additional=request.form.get("additional"),
            education=education_data
        )

    return render_template("resume_form.html")


# ================= COVER LETTER (UPDATED) =================
@app.route('/cover_letter_form', methods=['GET', 'POST'])
def cover_letter_form():
    if request.method == 'POST':
        # Get all fields from form
        name = request.form.get("name", "").strip()
        role = request.form.get("role", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        address = request.form.get("address", "").strip()
        recipient = request.form.get("recipient", "").strip()
        para1 = request.form.get("para1", "").strip()
        para2 = request.form.get("para2", "").strip()
        para3 = request.form.get("para3", "").strip()
        dateVal = request.form.get("date", "").strip()

        # ✅ If date not provided → auto fill today's date
        if not dateVal:
            dateVal = datetime.now().strftime("%B %d, %Y")

        # ✅ Required fields validation
        required_fields = [name, role, email, phone, address, recipient, para1, para2, para3]
        if not all(required_fields):
            error_msg = "Please fill all compulsory fields before generating the cover letter."
            return render_template("cover_letter_form.html", error=error_msg)

        # ✅ Render cover letter template
        return render_template(
            "cover_letter_template.html",
            name=name,
            role=role,
            email=email,
            phone=phone,
            address=address,
            recipient=recipient,
            para1=para1,
            para2=para2,
            para3=para3,
            date=dateVal
        )

    return render_template("cover_letter_form.html")


# ================= PORTFOLIO =================
@app.route('/portfolio_form', methods=['GET', 'POST'])
def portfolio_form():
    if request.method == 'POST':
        name = request.form.get("name", "")
        role_main = request.form.get("role", "")
        skills = request.form.get("skills", "")
        about = request.form.get("about", "")

        total_projects = int(request.form.get("total_projects") or 0)
        projects = []
        for i in range(1, total_projects + 1):
            projects.append({
                "title": request.form.get(f"title_{i}", ""),
                "role": request.form.get(f"role_{i}", ""),
                "tech": request.form.get(f"tech_{i}", ""),
                "overview": request.form.get(f"overview_{i}", ""),
                "results": request.form.get(f"results_{i}", "")
            })

        return render_template(
            "portfolio_template.html",
            name=name,
            role=role_main,
            skills=skills,
            about=about,
            total_projects=total_projects,
            projects=projects
        )

    return render_template("portfolio_form.html")


# ================= PORTFOLIO TEMPLATE ROUTE =================
@app.route('/portfolio_template')
def portfolio_template():
    name = request.args.get("name", "")
    role_main = request.args.get("role", "")
    skills = request.args.get("skills", "")
    about = request.args.get("about", "")
    total_projects = int(request.args.get("total_projects") or 0)

    projects = []
    for i in range(1, total_projects + 1):
        projects.append({
            "title": request.args.get(f"title_{i}", ""),
            "role": request.args.get(f"role_{i}", ""),
            "tech": request.args.get(f"tech_{i}", ""),
            "overview": request.args.get(f"overview_{i}", ""),
            "results": request.args.get(f"results_{i}", "")
        })

    return render_template(
        "portfolio_template.html",
        name=name,
        role=role_main,
        skills=skills,
        about=about,
        total_projects=total_projects,
        projects=projects
    )


if __name__ == '__main__':
    app.run(debug=True)