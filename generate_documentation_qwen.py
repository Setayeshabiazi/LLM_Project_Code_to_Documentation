
import json
import requests
import time
import os

start_time = time.time()

# File paths
INPUT_JSONL = "code2doc_raw_dataset.jsonl"
OUTPUT_JSONL = "code2doc_qwen2.5_dataset.jsonl"

# Model & API
OLLAMA_API_URL = "https://0lzebkg5kcob7y-11434.proxy.runpod.net/api/generate"
MODEL_NAME = "qwen2.5-coder:7b"

# Restrict to specific files or directories
TARGET_REPOS = [
    "/Users/setti/Desktop/CompSci422/code_to_doc/Repos/discord.py-master/examples"
]

def is_from_target_repo(path):
    return any(path.startswith(repo) for repo in TARGET_REPOS)

# Few-shot examples with chain-of-thought
FEW_SHOT_EXAMPLE = """ 
You are a Python code explainer. When presented with code, analyze it step by step:
1. Identify the function signature and parameters
2. Explain the overall purpose
3. Walk through the implementation line by line
4. Identify any assumptions or failure conditions (e.g., null inputs, incorrect types, or division by zero), and note whether the function validates inputs.
5. Summarize what the function accomplishes
6. Provide a Google-style docstring that includes:
   - A short summary
   - An `Args:` section listing each parameter, its type, and purpose
   - A `Returns:` section describing the return type and value
   - Optional: `Raises:` section if the function raises exceptions
7. Format all output using markdown, and use bullet points where appropriate.
Output should include a step-by-step explanation, a summary, a Google-style docstring, and an example of usage.

### Example 1:

Function:
```python
def greet_user(name):
    print(f"Hello, {name}!")
```
Step-by-step explanation:

- The function is named greet_user and takes one parameter: name (a string).
- It prints a greeting message using the provided name.
- It uses an f-string to format the message: Hello, <name>!.
- Assumes name is a valid string. No return value—this is for side-effect (printing).

In summary, it greets the user with their name.

Docstring:
```python
Prints a greeting message to the user.

Args:
    name (str): The user's name.

Returns:
    None
```

Example:
```python
greet_user("Alice")  # Output: Hello, Alice!
```

### Example 2:

Function:
```python
def calculate_area(radius):
    import math
    return math.pi * radius ** 2
```
Step-by-step explanation:

- The function calculate_area takes one parameter: radius.
- It calculates the area of a circle using the formula: π * r².
- Uses the math.pi constant for better precision.
- Assumes radius is a non-negative number (int or float).
- Does not validate input type or value — passing a string or negative value could raise an error or return a misleading result.

In summary, it returns the area of a circle.

Docstring:
```python
Calculates the area of a circle given its radius.

Args:
    radius (float): The radius of the circle. Must be a non-negative number.

Returns:
    float: The area of the circle.

Raises:
    TypeError: If radius is not a number.
    ValueError: If radius is negative.
```

Example:
```python
calculate_area(3)  # Output: 28.27 (approx)
```

### Example 3:

Function:
```python
def __str__(self) -> str:
    if self.animated:
        return f'<a:{self.name}:{self.id}>'
    return f'<:{self.name}:{self.id}>'
```

Step-by-step explanation:

- This is a special method __str__, which defines how an instance of the class will be represented as a string (e.g., when passed to print()).
- It checks whether the emoji is animated using the self.animated boolean attribute.
- If animated is True, it returns a string in the format <a:name:id>—Discord's syntax for animated emojis.
- If animated is False, it returns the regular emoji format <:name:id>.
- Assumes that self.name and self.id are properly set attributes of the Emoji object.

In summary, this method provides the correct Discord-rendered string representation of an emoji.

Docstring:
```python
Returns the Discord-formatted string for this emoji.

Returns:
    str: The rendered emoji string, using Discord's syntax.
         Animated emojis use the format `<a:name:id>`, while regular ones use `<:name:id>`.
```

Example:
```python
emoji = Emoji()
emoji.name = "wave"
emoji.id = 123456789
emoji.animated = False
print(str(emoji))  # Output: <:wave:123456789>
```
"""

# Build the final prompt for each function
def build_prompt(code_str, file_name, model_name="qwen2.5-coder:7b"):
    return f"""Documenting: {file_name}
Model Used: {model_name}
Instruction:
Please follow the style shown in the examples below to document the provided Python function.

{FEW_SHOT_EXAMPLE}

Input Python Function:
```python
{code_str}
```
"""


# Send the prompt to the LLM
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

# Process entries from the input JSONL file
updated_entries = []
with open(INPUT_JSONL, "r", encoding="utf-8") as infile:
    for line in infile:
        entry = json.loads(line)

        if "filepath" not in entry or "func_name" not in entry or "func_code_string" not in entry:
            print(f"⚠️ Skipping incomplete entry: {entry}")
            continue

        filepath = entry["filepath"]
        print(f"🔎 Checking file: {filepath}")
        print(f"✅ Match? {is_from_target_repo(filepath)}")

        if not is_from_target_repo(filepath):
            print(f"⛔ Skipped: {filepath}")
            continue

        matched_repo = next((repo for repo in TARGET_REPOS if filepath.startswith(repo)), None)
        if matched_repo is None:
            print(f"❌ No matching repo found for: {filepath}")
            continue

        repo_name = os.path.basename(matched_repo)
        func_path_in_repo = os.path.relpath(filepath, matched_repo)
        func_code_url = f"https://github.com/your-org/{repo_name}/blob/main/{func_path_in_repo}"

        prompt = build_prompt(entry["func_code_string"], entry["func_name"])
        print(f"🧠 Generating doc for: {entry['func_name']}")
        doc = query_qwen(prompt)

        filtered_entry = {
            "repository_name": repo_name,
            "func_path_in_repository": func_path_in_repo,
            "func_name": entry["func_name"],
            "whole_func_string": entry.get("whole_func_string", ""),
            "func_code_string": entry["func_code_string"],
            "func_documentation_string": doc.strip(),
            "func_code_url": func_code_url
        }

        updated_entries.append(filtered_entry)
        time.sleep(1)  # Avoid rate limiting

# Write results to output file
with open(OUTPUT_JSONL, "w", encoding="utf-8") as out:
    for item in updated_entries:
        json.dump(item, out)
        out.write("\n")

print(f"✅ Documentation generation complete. Output written to {OUTPUT_JSONL}")
end_time = time.time()
print(f"⏱️ Total time: {round((end_time - start_time) / 60, 2)} minutes")
