from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel, Field
from rag.agents import investigate
from rag.vision import analyze_image

app = FastAPI(title="Enterprise RAG Multi-Agent API", version="0.1.0")


class Query(BaseModel):
    question: str = Field(min_length=3, max_length=1000)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/ask")
def ask(query: Query):
    return investigate(query.question)


@app.post("/api/vision/inspect")
async def vision(file: UploadFile = File(...)):
    if file.content_type not in ("image/png", "image/jpeg", "image/webp"):
        raise HTTPException(415, "Allowed: PNG, JPEG, WebP")
    raw = await file.read(4_000_001)
    try:
        return analyze_image(raw)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
