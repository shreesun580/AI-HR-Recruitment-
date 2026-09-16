def load_knowledge_base():

    with open(
        "data/hr_knowledge.txt",
        "r"
    ) as file:

        return file.read()


def retrieve_information(query):

    knowledge = load_knowledge_base()

    sections = knowledge.split("\n\n")

    query_words = query.lower().split()

    results = []

    for section in sections:

        section_lower = section.lower()

        matches = 0

        for word in query_words:

            if word in section_lower:
                matches += 1

        if matches > 0:
            results.append(section)

    return results


def generate_recommendation(score):

    if score >= 80:
        return "STRONG CANDIDATE - SHORTLIST"

    elif score >= 60:
        return "MODERATE CANDIDATE - FURTHER REVIEW"

    else:
        return "LOW MATCH - TRAINING REQUIRED"
