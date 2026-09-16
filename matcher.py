SKILLS = [
    "Python",
    "Java",
    "C",
    "SQL",
    "Git",
    "REST API",
    "Machine Learning",
    "Power BI",
    "Excel",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Data Structures",
    "Algorithms",
    "Statistics"
]


def extract_skills(resume_text):

    found_skills = []

    text = resume_text.lower()

    for skill in SKILLS:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills


def match_candidate(candidate_skills, job_skills):

    matched = []
    missing = []

    candidate_lower = [
        skill.lower()
        for skill in candidate_skills
    ]

    for skill in job_skills:

        if skill.lower() in candidate_lower:
            matched.append(skill)

        else:
            missing.append(skill)

    if job_skills:
        score = (
            len(matched) /
            len(job_skills)
        ) * 100
    else:
        score = 0

    return round(score, 2), matched, missing
