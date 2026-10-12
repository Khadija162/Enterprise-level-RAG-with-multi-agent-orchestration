"""Web interface for citation-grounded multi-agent research."""
import os
import requests
import streamlit as st
st.set_page_config(page_title="Enterprise Multi-Agent RAG", layout="wide")
st.title("Enterprise RAG · Multi-Agent Research")
st.caption("Source-grounded knowledge assistant | Open documents | Experimental VLM interface")
api = os.getenv("API_URL", "http://127.0.0.1:8000")
with st.tab("Ask sources") if False else st.container():
    question = st.text_input("Question", "What is responsible data engineering?")
    if st.button("Investigate"):
        try:
            result = requests.post(api + "/api/ask", json={"question": question}, timeout=15)
            result.raise_for_status()
            data = result.json()
            st.info("Selected agent: " + data["agent"])
            st.text(data["answer"])
            st.json(data["citations"])
        except requests.RequestException as exc:
            st.error(str(exc))
st.divider()
st.subheader("Image interface (metadata only)")
image = st.file_uploader("Upload a non-sensitive image", type=["png", "jpg", "webp"])
if image and st.button("Inspect image"):
    try:
        r = requests.post(api + "/api/vision/inspect", files={"file": (image.name, image.getvalue(), image.type)}, timeout=15)
        r.raise_for_status()
        st.json(r.json())
    except requests.RequestException as exc:
        st.error(str(exc))
