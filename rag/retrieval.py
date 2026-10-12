"""Local lexical retrieval with source tracing and no paid services."""
import re
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def chunks_from_directory(path="data/public"):
    records = []
    for file in sorted(Path(path).glob("*.txt")):
        text = file.read_text(encoding="utf-8")
        paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
        for i, paragraph in enumerate(paragraphs):
            if len(paragraph) >= 40:
                records.append({"source": file.name, "chunk": i, "text": paragraph[:4000]})
    return records


def search(question: str, documents: list[dict], k: int = 3):
    if not documents:
        return []
    corpus = [record["text"] for record in documents]
    matrix = TfidfVectorizer(stop_words="english", ngram_range=(1, 2)).fit_transform(corpus + [question])
    similarities = cosine_similarity(matrix[-1], matrix[:-1])[0]
    best = sorted(range(len(similarities)), key=lambda i: -similarities[i])[:k]
    return [{**documents[i], "score": round(float(similarities[i]), 4)} for i in best if similarities[i] > 0]
