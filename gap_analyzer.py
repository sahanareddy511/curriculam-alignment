def analyze_gap(resume_skills, job_skills):
    """
    Compares resume skills with job skills to find missing skills and calculate match percentage.
    """
    resume_set = set([s.lower() for s in resume_skills])
    job_set = set([s.lower() for s in job_skills])
    
    # Calculate matches
    matched_skills = resume_set.intersection(job_set)
    
    # Calculate missing skills
    missing_skills = list(job_set - resume_set)
    
    # Calculate match percentage
    if not job_set:
        match_percentage = 0
    else:
        match_percentage = (len(matched_skills) / len(job_set)) * 100
        
    return {
        "match_percentage": round(match_percentage, 2),
        "missing_skills": missing_skills,
        "matched_skills": list(matched_skills)
    }