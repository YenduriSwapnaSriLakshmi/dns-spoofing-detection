import json
from datetime import datetime

def print_result(data):
    print("\n--- DNS Analysis ---")
    for key, value in data.items():
        print(f"{key}: {value}")


def save_log(data, filename="data/sample_logs.json"):
    try:
        data["timestamp"] = str(datetime.now())

        try:
            with open(filename, "r") as f:
                logs = json.load(f)
        except:
            logs = []

        logs.append(data)

        with open(filename, "w") as f:
            json.dump(logs, f, indent=4)

    except Exception as e:
        print("Error saving log:", e)