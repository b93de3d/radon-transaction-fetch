import json

try:
    with open("config.json") as f:
        CONFIG = json.loads(f.read())
except FileNotFoundError:
    print(f"Please ensure config.json exists in project root. (You may need to `cp example_config.json config.json`)")