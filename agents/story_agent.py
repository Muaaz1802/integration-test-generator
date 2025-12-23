
def analyze_story(path):
    with open(path) as f:
        stories = f.read()
    return {
        "actors": ["user"],
        "actions": ["create", "fetch"],
        "raw": stories
    }
