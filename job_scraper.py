def get_job_skills(role):
    """
    Returns a mock list of required skills for a specific job role.
    In a real app, this would scrape job boards.
    """
    
    mock_job_data = {
        "Data Analyst": [
            "python", "sql", "excel", "tableau", "data analysis", "statistics", 
            "communication", "pandas", "numpy"
        ],
        "Web Developer": [
            "html", "css", "javascript", "react", "node.js", "git", 
            "responsive design", "api"
        ],
        "AI Engineer": [
            "python", "tensorflow", "pytorch", "machine learning", "deep learning", 
            "nlp", "docker", "cloud computing", "mathematics"
        ]
    }
    
    # Return skills for the role, or empty list if not found
    return mock_job_data.get(role, [])