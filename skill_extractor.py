
# skill_extractor.py

# Predefined skill list
SKILL_LIST = [
    "python", "java", "c++", "javascript", "html", "css", "sql", "react", "flask",
    "django", "node.js", "aws", "azure", "docker", "kubernetes", "git",
    "machine learning", "deep learning", "nlp", "tensorflow", "pytorch",
    "pandas", "numpy", "scikit-learn", "data analysis", "tableau", "power bi",
    "communication", "leadership", "problem solving", "agile", "scrum",
    "project management", "linux", "bash"
]

def extract_skills(text):
    """
    Extract skills using simple keyword matching.
    """
    text = text.lower()
    extracted_skills = []

    for skill in SKILL_LIST:
        if skill in text:
            extracted_skills.append(skill)

    return list(set(extracted_skills))  # remove duplicates