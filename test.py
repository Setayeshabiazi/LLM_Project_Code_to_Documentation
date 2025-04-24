import json

with open("code2doc_raw_dataset.jsonl", "r", encoding="utf-8") as f:
    for _ in range(5):
        line = f.readline()
        if not line:
            break
        entry = json.loads(line)
        print(entry.get("filepath", "NO FILEPATH FOUND"))
