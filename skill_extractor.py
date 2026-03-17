import pandas as pd
import re


def load_skills_database():

    df = pd.read_csv("data/skills_db.csv")

    df.columns = df.columns.str.lower().str.strip()

    skills = df["skill"].dropna().tolist()

    return [s.lower() for s in skills]


def extract_skills(text, skills_db):

    text = text.lower()

    detected = []

    for skill in skills_db:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            detected.append(skill)

    return list(set(detected))