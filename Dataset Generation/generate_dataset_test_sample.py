import json
import requests
import time
import random

# Configuration
INPUT_JSONL = "functions_raw.jsonl"
OUTPUT_JSONL = "qwen2.5_test_dataset.jsonl"
OLLAMA_API_URL = "https://0lzebkg5kcob7y-11434.proxy.runpod.net/api/generate"
MODEL_NAME = "qwen2.5-coder:7b"
SAMPLE_SIZE = 100

# Few-shot examples to guide LLM
FEW_SHOT_EXAMPLE = '''
### Example 1:

def greet_user(name):
    """
    Prints a greeting message to the user.

    Args:
        name (str): The user's name.

    Returns:
        None
    """
    print(f"Hello, {name}!")

### Example 2:

def calculate_area(radius):
    """
    Calculates the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    import math
    return math.pi * radius ** 2
'''

def build_prompt(code_str, func_name):
    return f'''
# Documenting: `{func_name}`
# Model Used: `{MODEL_NAME}`

## Instruction:
Please follow the style shown in the examples below to document the provided Python function.

{FEW_SHOT_EXAMPLE}

## Input Python Function:
```python
{code_str}
```'''

def query_qwen(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        print(f"❌ Error querying Qwen: {e}")
        return ""

# Main execution
start_time = time.time()

# Load and sample
with open(INPUT_JSONL, "r", encoding="utf-8") as f:
    all_entries = [json.loads(line) for line in f if line.strip()]

sampled_entries = random.sample(all_entries, min(SAMPLE_SIZE, len(all_entries)))
updated_entries = []

# Process each sampled function
for i, entry in enumerate(sampled_entries):
    code = entry.get("func_code_string")
    name = entry.get("func_name")

    if not code or not name:
        continue

    print(f"🧠 [{i+1}/{len(sampled_entries)}] Generating doc for: {name}")
    prompt = build_prompt(code, name)
    doc = query_qwen(prompt)

    entry["func_documentation_string"] = doc.strip()
    entry["llm_used"] = MODEL_NAME
    updated_entries.append(entry)

    time.sleep(1)  # prevent rate-limiting

# Save to output
with open(OUTPUT_JSONL, "w", encoding="utf-8") as out:
    for item in updated_entries:
        json.dump(item, out)
        out.write("\n")

end_time = time.time()
print(f"✅ Sample documentation generation complete. Output written to {OUTPUT_JSONL}")
print(f"⏱️ Total time: {round((end_time - start_time) / 60, 2)} minutes")
