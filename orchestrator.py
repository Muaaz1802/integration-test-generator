import argparse
from agents.story_agent import analyze_story
from agents.api_agent import parse_openapi
from agents.scenario_agent import expand_scenarios
from agents.validation_agent import validate_scenarios
from agents.synthesis_agent import synthesize_tests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stories", required=True)
    parser.add_argument("--openapi", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    story_data = analyze_story(args.stories)
    api_data = parse_openapi(args.openapi)
    scenarios_text = expand_scenarios(story_data, api_data)
    approved = validate_scenarios(scenarios_text, api_data)
    tests = synthesize_tests(approved)

    print("Generated Integration Tests:")
    for t in tests:
        print(t)

if __name__ == "__main__":
    main()
