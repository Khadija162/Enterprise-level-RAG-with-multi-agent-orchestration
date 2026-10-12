# Architecture and maturity

## Implemented
- A small original open-licensed corpus.
- TF-IDF citation-aware retrieval with abstention on no matching evidence.
- Deterministic safety/platform/research agent routing (NOT autonomous agents).
- FastAPI question answering and image metadata endpoints.
- Streamlit frontend, Docker Compose, tests, GitHub Actions CI.
- Azure Terraform resource group + ADLS Gen2 starter.

## Future integrations (not yet implemented)
- Azure AI Search hybrid vector retrieval, ingestion jobs and incremental indexing.
- Open-weight LLM with guarded agent tool calls, structured planning, evaluation and human approval.
- Open-weight VLM for semantic image understanding. Current image endpoint computes metadata only.
- Azure Container Apps production hosting, Entra ID, Key Vault, monitoring and rate limits.
- Delta Lake Bronze/Silver/Gold document processing using Spark/Databricks.

## Safety
Treat retrieved documents as untrusted. Require human authorization for side effects. Never accept raw credentials or sensitive documents in this public demo. Implement per-tenant document ACLs before indexing restricted documents. No claims of production-grade security.
