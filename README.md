# Enterprise RAG with Multi-Agent Orchestration

Open-source **research-grade RAG starter** with source citations, specialist-agent routing, an image interface, FastAPI backend, Streamlit frontend, Docker, pytest, GitHub Actions and Azure Terraform example.

> **What is implemented:** TF-IDF retrieval with source references, deterministic router to research/platform/safety agents, extractive answers, image metadata inspection, UI, API and local containers. **Not yet implemented:** generative LLM inference, autonomous multi-agent collaboration, semantic VLM captions, distributed Spark/Delta pipelines, cloud deployment or production authentication. The project intentionally does not mislabel these as complete.

## Architecture

```text
Open original corpus → paragraph extraction → TF-IDF search → cited snippets
                                                     |
Question → FastAPI /api/ask → specialist agent router ┘ → Streamlit interface
Image → FastAPI /api/vision/inspect → validated image metadata → Streamlit
CI: tests and Docker build | Azure: Terraform ADLS Gen2 example only
```

## Dataset

The committed [open knowledge corpus](data/public/open_knowledge.txt) is original public educational text under **CC0**. [Provenance and expansion options](data/public/README.md) explain how to add appropriately licensed open NASA or public-government documents. The current corpus is intentionally small and not a benchmark.

## Run on Windows (PowerShell)

```powershell
git clone https://github.com/Khadija162/Enterprise-level-RAG-with-multi-agent-orchestration.git
cd Enterprise-level-RAG-with-multi-agent-orchestration
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
```

Backend, terminal 1:

```powershell
.\.venv\Scripts\python.exe -m uvicorn backend.main:app --reload
```

Frontend, terminal 2:

```powershell
.\.venv\Scripts\python.exe -m streamlit run frontend/app.py
```

- Backend API docs: http://localhost:8000/docs
- Web frontend: http://localhost:8501

Or run both in Docker Desktop:

```powershell
docker compose up --build
```

Neither service exposes ports beyond localhost in the example Compose configuration.

## API

- `GET /health`: liveness
- `POST /api/ask`: `{"question":"How can Azure storage support data pipelines?"}`
- `POST /api/vision/inspect`: PNG/JPEG/WebP image upload; returns **metadata only**, not semantics

The RAG response gives source filenames and chunk IDs. Agent selection is simple deterministic routing, not an independent autonomous AI framework.

## Production roadmap

1. Add publicly licensed source connectors, document provenance checks and Parquet Bronze/Silver/Gold ingestion.
2. Add Azure AI Search hybrid/vector indexing or a local pgvector alternative.
3. Add an actual open-weight LLM adapter with source-constrained synthesis and independent hallucination evaluation.
4. Add an open-weight VLM for **semantic** image understanding and grounded image/document evidence.
5. Add human-reviewed multi-agent orchestration, access isolation and tool restrictions.
6. Deploy authenticated FastAPI and frontend to Azure Container Apps with managed identities, Key Vault and Azure Monitor.
7. Expand Terraform beyond the resource group and ADLS Gen2 starter.

**Status:** GitHub source is committed but the CI run, Docker runtime and Azure deployment have not been independently verified. No Azure services were provisioned. Azure resources can incur charges when deployed.

See [architecture notes](docs/architecture.md).
