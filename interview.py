QUESTION_BANK = {

    "python":
    "Explain your experience with Python and describe a project where you used it.",

    "sql":
    "What is the difference between INNER JOIN and LEFT JOIN in SQL?",

    "git":
    "How do you use Git for version control?",

    "rest api":
    "What is a REST API and how have you used it?",

    "machine learning":
    "Explain a machine learning project you have worked on.",

    "power bi":
    "Explain a Power BI dashboard you have created.",

    "excel":
    "Which Excel functions have you used for data analysis?",

    "html":
    "What is the purpose of HTML in web development?",

    "css":
    "How does CSS help in designing responsive web pages?",

    "javascript":
    "What is JavaScript and where have you used it?",

    "java":
    "Explain the main features of Java.",

    "data structures":
    "Which data structures have you used in your projects?",

    "algorithms":
    "Explain an algorithm you have implemented."
}


def generate_interview_questions(skills):

    questions = []

    for skill in skills:

        key = skill.lower()

        if key in QUESTION_BANK:

            questions.append(
                QUESTION_BANK[key]
            )

    return questions
