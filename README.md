
# Integration Test Case Generator (Google ADK + Gemma)

## Overview
This project automatically generates integration test cases from:
- User Stories
- OpenAPI / Swagger API contracts

It uses **Google ADK (Agent Development Kit)** for orchestration and **Gemma:2b model** only for ambiguity resolution and scenario expansion.

## Architecture
- Deterministic parsing first
- Gemini-assisted reasoning only where needed
- Multi-agent execution using ADK

## Tech Stack
- Python 3.11
- Google ADK
- Ollama backend(gemma:2b)
- FastAPI (optional extension)
- OpenAPI tools

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Execution

```bash
python orchestrator.py       --stories samples/user_stories.txt       --openapi samples/openapi.yaml       --output out/
```

## Output
- Abstract integration test cases
- Framework exporters can be added (Postman, PyTest, Karate)
