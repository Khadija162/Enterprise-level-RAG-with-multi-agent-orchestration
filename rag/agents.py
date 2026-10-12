"""Deterministic agent routing, evidence retrieval and conservative synthesis."""
from .retrieval import chunks_from_directory, search


def select_agent(question: str) -> str:
    q = question.lower()
    if any(word in q for word in ("security", "privacy", "safety", "attack", "risk")):
        return "safety_agent"
    if any(word in q for word in ("azure", "cloud", "storage", "pipeline", "spark")):
        return "platform_agent"
    return "research_agent"


def investigate(question: str, data_dir="data/public") -> dict:
    agent = select_agent(question)
    docs = chunks_from_directory(data_dir)
    citations = search(question, docs, k=3)
    if not citations or citations[0]["score"] < 0.03:
        return {"agent": agent, "answer": "Insufficient evidence in the indexed sources.", "citations": []}
    extracts = [item["text"][:360] for item in citations]
    answer = "Evidence excerpts from the indexed corpus (not an independent conclusion):\n" + "\n".join(
        f"[{i}] {snippet}" for i, snippet in enumerate(extracts, start=1)
    )
    return {"agent": agent, "answer": answer,
            "citations": [{"id": i, "source": c["source"], "chunk": c["chunk"], "score": c["score"]}
                          for i, c in enumerate(citations, start=1)]}
