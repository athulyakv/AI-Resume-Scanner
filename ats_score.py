def calculate_ats_score(resume_text, skills_found, skills_db):

    score = 0

    skill_ratio = len(skills_found) / len(skills_db)

    score += skill_ratio * 40

    word_count = len(resume_text.split())

    if word_count > 400:
        score += 20
    elif word_count > 200:
        score += 10

    sections = ["experience", "education", "projects", "skills"]

    section_count = sum(1 for s in sections if s in resume_text)

    score += (section_count / len(sections)) * 20

    unique_words = len(set(resume_text.split()))

    if unique_words > 200:
        score += 20
    elif unique_words > 100:
        score += 10

    return round(score, 2)