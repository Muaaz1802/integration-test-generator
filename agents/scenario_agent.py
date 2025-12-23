# agents/scenario_agent.py

import json
import subprocess
import hashlib
from typing import Dict, Any, List


def _stable_story_id(raw: str) -> str:
    return "US-" + hashlib.md5(raw.encode()).hexdigest()[:8]


def _parse_endpoint(ep: str) -> Dict[str, str]:
    method, path = ep.split(" ", 1)
    return {"method": method, "path": path}


def _fallback_scenarios(story: Dict[str, Any], api: Dict[str, Any]) -> List[Dict[str, Any]]:
    scenarios = []
    story_id = story.get("id") or _stable_story_id(story["raw"])

    for ep in api.get("endpoints", []):
        endpoint = _parse_endpoint(ep)

        scenarios.append({
            "story_id": story_id,
            "type": "happy_path",
            "endpoint": endpoint,
            "expected_status": 200
        })

        scenarios.append({
            "story_id": story_id,
            "type": "unauthorized",
            "endpoint": endpoint,
            "expected_status": 401
        })

    return scenarios


def _call_ollama(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", "gemma:2b"],
        input=prompt,
        text=True,
        capture_output=True,
        timeout=60
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    return result.stdout.strip()


def expand_scenarios(story: Dict[str, Any], api: Dict[str, Any]):
    payload = {
        "story_id": story.get("id"),
        "user_story": story["raw"],
        "allowed_endpoints": api.get("endpoints", [])
    }

    prompt = f"""
You generate integration test scenarios.

Rules:
- Use ONLY these endpoints: {payload["allowed_endpoints"]}
- Do NOT invent endpoints
- Return STRICT JSON ARRAY only

User story:
{payload["user_story"]}
"""

    try:
        output = _call_ollama(prompt)
        parsed = json.loads(output)

        if not isinstance(parsed, list):
            raise ValueError("Model output is not a list")

        return parsed

    except Exception:
        return _fallback_scenarios(story, api)
