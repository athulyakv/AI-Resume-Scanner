from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(resume_text, job_description):

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    tfidf = vectorizer.fit_transform(documents)

    score = cosine_similarity(tfidf[0:1], tfidf[1:2])

    return round(score[0][0] * 100, 2)