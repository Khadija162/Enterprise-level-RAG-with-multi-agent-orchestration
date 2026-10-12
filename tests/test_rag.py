from io import BytesIO
from PIL import Image
from fastapi.testclient import TestClient
from backend.main import app
from rag.agents import select_agent, investigate
from rag.vision import analyze_image


def test_routing():
    assert select_agent("How to secure Azure storage?") == "safety_agent"
    assert select_agent("How does Spark work?") == "platform_agent"


def test_evidence(tmp_path):
    (tmp_path / "source.txt").write_text("Azure storage uses role based access controls to limit exposure.\n\nData quality tracks validity and freshness to support observability.")
    result = investigate("How does data quality track freshness?", tmp_path)
    assert result["citations"]
    assert "source.txt" in str(result["citations"])


def test_insufficient_evidence(tmp_path):
    assert investigate("Unrelated query", tmp_path)["citations"] == []


def test_api():
    client = TestClient(app)
    assert client.get("/health").status_code == 200
    assert client.post("/api/ask", json={"question": "a"}).status_code == 422


def test_image():
    b = BytesIO()
    Image.new("RGB", (16, 16), "white").save(b, format="PNG")
    assert analyze_image(b.getvalue())["width"] == 16
