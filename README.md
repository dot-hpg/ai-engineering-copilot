# AI Engineering Copilot

A production-oriented Agentic AI backend that uses routing, RAG retrieval,
evidence evaluation, answer evaluation, retry-based self-correction,
observability metadata, and API-level reliability controls.

## Architecture

```text
User Question
      ↓
FastAPI API
      ↓
Query Classifier
      ↓
Technical / General Route
      ↓
Embedding Generation
      ↓
Qdrant Vector Retrieval
      ↓
Evidence Evaluation
      ↓
 ┌───────────────┐
 │ Evidence OK?  │
 └───────┬───────┘
         │
    Yes  │  No
         ↓   ↓
 Answer LLM   Stop
 Generation
      ↓
 Answer Evaluation
      ↓
 ┌──────────────────┐
 │ Answer Supported?│
 └────────┬─────────┘
          │
     Yes  │  No
          ↓   ↓
        Finish
             ↓
          Retry
             ↓
          Finish / Reject