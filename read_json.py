import json

with open("/Users/setti/Desktop/CompSci422/code_to_doc/qwen2.5_test_dataset.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():  # skip empty lines
            obj = json.loads(line)
            print(json.dumps(obj, indent=2))  # Pretty-print each object
