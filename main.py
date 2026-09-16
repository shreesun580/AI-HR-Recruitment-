import os
import glob

from src.resume_parser import extract_text
from src.matcher import extract_skills, match_candidate
from src.interview import generate_interview_questions
from src.agent import recruitment_agent


def display_report(result):

    print("\n")
    print("=" * 65)
    print("              AI HR RECRUITMENT REPORT")
    print("=" * 65)

    print("\nJOB TITLE")
    print("-" * 65)
    print(result["job_title"])

    print("\nCANDIDATE SKILLS")
    print("-" * 65)

    for skill in result["candidate_skills"]:
        print("✓", skill)

    print("\nMATCHED SKILLS")
    print("-" * 65)

    for skill in result["matched"]:
        print("✓", skill)

    print("\nMISSING SKILLS")
    print("-" * 65)

    if result["missing"]:
        for skill in result["missing"]:
            print("✗", skill)
    else:
        print("None")

    print("\nMATCH SCORE")
    print("-" * 65)
    print(result["score"], "%")

    print("\nHR RECOMMENDATION")
    print("-" * 65)
    print(result["recommendation"])

    print("\nINTERVIEW QUESTIONS")
    print("-" * 65)

    for i, question in enumerate(result["questions"], 1):
        print(f"{i}. {question}")

    print("\n" + "=" * 65)


def main():

    resume_files = glob.glob("resumes/*.pdf")

    if not resume_files:
        print("❌ No resume found in resumes folder.")
        return

    resume_path = resume_files[0]

    job_title = input("\nEnter Job Title: ")

    skill_input = input(
        "Enter Required Skills (comma separated): "
    )

    job_skills = [
        skill.strip()
        for skill in skill_input.split(",")
        if skill.strip()
    ]

    while True:

        print("\n")
        print("=" * 55)
        print("       AI HR RECRUITMENT ASSISTANT")
        print("=" * 55)

        print("\n1. View Resume")
        print("2. Extract Candidate Skills")
        print("3. Match Candidate")
        print("4. Generate Interview Questions")
        print("5. Generate Full Recruitment Report")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            text = extract_text(resume_path)

            print("\n========== RESUME ==========")
            print(text[:5000])

        elif choice == "2":

            text = extract_text(resume_path)
            skills = extract_skills(text)

            print("\n========== CANDIDATE SKILLS ==========")

            for skill in skills:
                print("✓", skill)

        elif choice == "3":

            text = extract_text(resume_path)
            candidate_skills = extract_skills(text)

            score, matched, missing = match_candidate(
                candidate_skills,
                job_skills
            )

            print("\n========== MATCH RESULT ==========")
            print("Match Score:", score, "%")

            print("\nMatched:")

            for skill in matched:
                print("✓", skill)

            print("\nMissing:")

            for skill in missing:
                print("✗", skill)

        elif choice == "4":

            questions = generate_interview_questions(
                job_skills
            )

            print("\n========== INTERVIEW QUESTIONS ==========")

            for i, question in enumerate(questions, 1):
                print(f"{i}. {question}")

        elif choice == "5":

            result = recruitment_agent(
                resume_path,
                job_title,
                job_skills
            )

            display_report(result)

        elif choice == "6":

            print("\nThank you for using AI HR Recruitment Assistant!")
            break

        else:

            print("\n❌ Invalid choice.")


if __name__ == "__main__":
    main()
