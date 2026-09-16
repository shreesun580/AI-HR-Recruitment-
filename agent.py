
from .resume_parser import extract_text
from .matcher import extract_skills, match_candidate
from .rag import retrieve_information, generate_recommendation
from .interview import generate_interview_questions


def recruitment_agent(resume_path, job_title, job_skills):

    print("\n" + "=" * 60)
    print("          AI HR RECRUITMENT AGENT")
    print("=" * 60)

    # Tool 1 - Resume Parser
    print("\n[TOOL 1] Reading resume...")
    resume_text = extract_text(resume_path)
    print("✓ Resume successfully read")

    # Tool 2 - Skill Extraction
    print("\n[TOOL 2] Extracting skills...")
    candidate_skills = extract_skills(resume_text)
    print("✓ Skills extracted")

    # Tool 3 - Candidate Matching
    print("\n[TOOL 3] Matching candidate...")
    score, matched, missing = match_candidate(
        candidate_skills,
        job_skills
    )
    print("✓ Candidate matching completed")

    # Tool 4 - RAG
    print("\n[TOOL 4] Retrieving HR knowledge...")
    rag_results = retrieve_information(job_title)
    print("✓ HR knowledge retrieved")

    # Tool 5 - Recommendation
    recommendation = generate_recommendation(score)

    # Tool 6 - Interview Questions
    questions = generate_interview_questions(job_skills)

    return {
        "job_title": job_title,
        "candidate_skills": candidate_skills,
        "job_skills": job_skills,
        "score": score,
        "matched": matched,
        "missing": missing,
        "recommendation": recommendation,
        "rag_results": rag_results,
        "questions": questions
    }
