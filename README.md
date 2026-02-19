📄 Resume, Portfolio & Cover Letter Builder
(Rule-Based Web Application)
📌 Project Summary
This project is a rule-based web application developed using Flask that allows students and freshers to generate:
Resume
Cover Letter
Portfolio
The system collects user input through structured forms and formats the data into predefined professional templates.
⚠️ This is NOT an AI-powered system.
It does not use machine learning or external APIs.
It works using predefined formatting rules and template rendering logic.
🎯 Purpose of the Project
The main objective of this project is:
To help students quickly create job-ready documents
To automate formatting using rule-based logic
To demonstrate Flask-based full-stack development skills
This project was developed as part of an internship academic submission.
🏗️ Project Structure
Copy code

resume-portfolio-coverletter-builder/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   │   ├── coverletter.css
│   │   ├── dashboard.css
│   │   ├── portfolio.css
│   │   └── resume.css
│   │
│   └── js/
│       ├── html2canvas.min.js
│       └── main.js
│
└── templates/
    ├── dashboard.html
    ├── resume_form.html
    ├── resume_template.html
    ├── cover_letter_form.html
    ├── cover_letter_template.html
    ├── portfolio_form.html
    └── portfolio_template.html
⚙️ Technologies Used
Python
Flask
HTML
CSS
JavaScript
html2canvas (for image download functionality)
🖥️ Application Workflow
1️⃣ Dashboard
When the Flask server runs, the dashboard page opens.
It contains:
Project introduction
Note for students and freshers
Three navigation buttons:
Resume Form
Cover Letter Form
Portfolio Form
2️⃣ Resume Generator
User fills required details
Mandatory fields validation applied
Clicking “Generate Resume”:
Displays structured resume template
Two options available:
Go Back
Download Image
If any mistake occurs:
User can use browser back button
Edit details
Regenerate updated resume
3️⃣ Cover Letter Generator
User fills form
Clicks “Generate Cover Letter”
Structured format displayed
Download as image option available
Go Back option available
4️⃣ Portfolio Generator
User enters project details
Supports multiple projects
Pages dynamically increase based on number of projects
Structured alignment maintained
Download image option available
🧠 System Logic (Rule-Based)
The application works using:
Form data collection
Flask routing
Template rendering
Conditional validations
Predefined formatting rules
It does NOT:
Generate automatic content
Use AI models
Use external APIs
Use any paid AI services
It simply formats user-provided data into structured templates.
🚀 Installation & Setup
Step 1: Clone Repository
Copy code

git clone <repository-link>
cd resume-portfolio-coverletter-builder
Step 2: Install Dependencies
Copy code

pip install -r requirements.txt
Step 3: Run Application
Copy code

python app.py
Step 4: Open in Browser
Copy code

http://127.0.0.1:5000/
📥 Features
Structured Resume Generation
Cover Letter Formatting
Multi-Project Portfolio Support
Mandatory Field Validation
Image Download Functionality
Clean UI
Beginner-Friendly Flask Structure
📌 Limitations
No AI-based content generation
No database integration
No user authentication
No PDF export (Image only)
No cloud deployment
🔮 Future Enhancements
Add PDF download option
Add multiple design themes
Add login & user accounts
Add database storage
Add optional AI suggestion system
👩‍💻 Developed For
Academic / Internship submission project
Built using Flask full-stack web development concepts.
