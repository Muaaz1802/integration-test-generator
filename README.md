
# Integration Test Case Generator (Google ADK + Gemini)

## Overview
This project automatically generates integration test cases from:
- User Stories
- OpenAPI / Swagger API contracts

It uses **Google ADK (Agent Development Kit)** for orchestration and **Gemini** only for ambiguity resolution and scenario expansion.

## Architecture
- Deterministic parsing first
- Gemini-assisted reasoning only where needed
- Multi-agent execution using ADK

## Tech Stack
- Python 3.11
- Google ADK
- Gemini 1.5 Pro / Flash
- FastAPI (optional extension)
- OpenAPI tools

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Environment Variables

Create `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

## Execution

```bash
python orchestrator.py       --stories samples/user_stories.txt       --openapi samples/openapi.yaml       --output out/
```

## Output
- Abstract integration test cases
- Framework exporters can be added (Postman, PyTest, Karate)

## Notes
- Gemini never parses OpenAPI
- All hallucinations are rejected via validation gates
