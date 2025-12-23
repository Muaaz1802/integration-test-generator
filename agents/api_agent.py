
import yaml

def parse_openapi(path):
    with open(path) as f:
        spec = yaml.safe_load(f)
    endpoints = []
    for p, methods in spec.get("paths", {}).items():
        for m in methods.keys():
            endpoints.append(f"{m.upper()} {p}")
    return {"endpoints": endpoints}
