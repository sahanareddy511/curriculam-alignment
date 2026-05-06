def generate_roadmap(missing_skills):
    """
    Generates a simple weekly learning roadmap for missing skills.
    """
    roadmap = {}
    
    if not missing_skills:
        return {"Week 1": "Congratulations! You match all the required skills. Focus on building projects."}
    
    # Sort missing skills simply to have a deterministic order
    sorted_skills = sorted(missing_skills)
    
    # Assign 1-2 skills per week
    week_num = 1
    for i in range(0, len(sorted_skills), 2):
        chunk = sorted_skills[i:i+2]
        week_plan = f"Learn {', '.join(chunk).title()}"
        roadmap[f"Week {week_num}"] = week_plan
        week_num += 1
        
    return roadmap