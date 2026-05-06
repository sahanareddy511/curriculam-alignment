from flask import Flask, render_template, request
from skill_extractor import extract_skills

app = Flask(__name__)

# 🔹 Industry skill categories
SKILL_CATEGORIES = {
    "Programming": ["python", "java", "c++"],
    "Web Development": ["html", "css", "javascript", "react"],
    "Data & AI": ["machine learning", "data analysis", "pandas", "numpy"],
    "Cloud & DevOps": ["aws", "docker", "kubernetes"],
    "Database": ["sql"]
}

# 🔹 Role-based industry skills (NEW)
ROLE_SKILLS = {
    "Data Analyst": ["python", "data analysis", "sql", "pandas", "excel"],
    "Web Developer": ["html", "css", "javascript", "react", "node.js"],
    "AI Engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch"],
    "Software Tester": ["testing", "selenium", "java", "automation", "jira"],
    "Software Architect": ["system design", "microservices", "aws", "design patterns", "scalability"],
    "DevOps Engineer": ["docker", "kubernetes", "aws", "ci/cd", "linux"],
    "Backend Developer": ["python", "flask", "django", "sql", "api"],
    "Frontend Developer": ["html", "css", "javascript", "react", "ui/ux"]
}

# 🔹 Insight generator
def generate_insight(skills, missing):
    if not skills:
        return "No skills detected in the resume."

    if len(missing) == 0:
        return "Hurrayyy.... You are well aligned with industry requirements."

    insight = "You have a good foundation in "
    insight += ", ".join(skills[:3])
    insight += " but you need to improve in areas like "
    insight += ", ".join(missing[:3])
    insight += " to become industry-ready."

    return insight

# 🔹 Categorize skills
def categorize_skills(skills):
    categorized = {}

    for category, skill_list in SKILL_CATEGORIES.items():
        categorized[category] = []

        for skill in skills:
            if skill in skill_list:
                categorized[category].append(skill)

    return categorized


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['resume']
        text = ""

        if file:
            filename = file.filename

            if filename.endswith('.txt'):
                text = file.read().decode('utf-8')

            elif filename.endswith('.pdf'):
                from PyPDF2 import PdfReader
                reader = PdfReader(file)
                for page in reader.pages:
                    if page.extract_text():
                        text += page.extract_text()

            elif filename.endswith('.docx'):
                import docx
                doc = docx.Document(file)
                for para in doc.paragraphs:
                    text += para.text

        # 🔹 Extract skills
        skills = extract_skills(text)

        # 🔹 Get selected role
        selected_role = request.form.get('role')

        # 🔹 Get role-based industry skills
        industry_skills = ROLE_SKILLS.get(selected_role, [])

        # 🔹 Missing skills
        missing_skills = [s for s in industry_skills if s not in skills]

        # 🔹 Matched skills
        matched_skills = [s for s in skills if s in industry_skills]

        # 🔹 Match score
        match_score = int((len(matched_skills) / len(industry_skills)) * 100) if industry_skills else 0

        # 🔹 Features
        insight = generate_insight(skills, missing_skills)
        categorized_skills = categorize_skills(skills)

        return render_template(
            'index.html',
            skills=skills,
            missing=missing_skills,
            score=match_score,
            insight=insight,
            categorized=categorized_skills,
            matched=matched_skills
        )

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)