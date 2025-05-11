import requests
import os
import random
import time
from utils import read_full_script, save_to_markdown

# === Constants ===
OLLAMA_API_URL = "http://localhost:11434/api/generate"
PY_REPO_DIR = "/Users/setti/Desktop/CompSci422/code_to_doc/Repos"  # <-- Set this to the root of your Python repo
MODELS_TO_COMPARE = ["qwen2.5-coder:7b", "codellama:latest", "codegemma:7b", "qwen2.5-coder:0.5b"]

# === Few-Shot Prompt Example ===
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

# === Prompt Builder ===
def create_script_documentation_prompt(script_code, file_name, model_name):
    """Creates a few-shot prompt for LLM-based Python script documentation."""
    user_msg = f"""
# Documenting: `{file_name}`
# Model Used: `{model_name}`

## Instruction:
Please follow the style shown in the examples below to document the provided Python script.

{FEW_SHOT_EXAMPLE}

## Audience:
- Professional developers, software engineers, and technical leads.

## Documentation Goals:
- Provide a clear and concise **high-level summary** of what the script does.
- Highlight any key components such as APIs, GUIs, or custom classes/functions.
- Add detailed **inline comments** and section headers where necessary.
- Ensure **parameter and return descriptions** for each function/class.
- Include **usage examples**, if possible.
- Note any **dependencies** or critical **edge cases**.

## Format Requirements:
- Use **Google-style docstrings** inside functions and classes.
- Provide a structured overview at the top in markdown.
- Include code blocks using markdown backticks where helpful.
- Keep documentation **concise but complete**.

Important: Do NOT repeat the code. Just provide clean, well-structured documentation that explains the overall functionality, all classes, functions, and methods clearly. Do not include the original code or prompt in your output.

## Input Python Script:
```python
{script_code}
"""
    return user_msg.strip()

# === API Caller ===
def query_ollama(model, prompt):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        start_time = time.time()
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        elapsed_time = time.time() - start_time
        return response.json().get("response", None), elapsed_time
    except Exception as e:
        print(f"❌ Failed to get response from {model}: {e}")
        return None, 0

# === File Utility ===
def get_random_python_file(repo_dir):
    py_files = []
    for root, _, files in os.walk(repo_dir):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return random.choice(py_files) if py_files else None

# === Comparison Runner ===
def run_comparison_on_random_script():
    script_path = get_random_python_file(PY_REPO_DIR)
    if not script_path:
        print("⚠️ No Python files found in the repository.")
        return

    script_code = read_full_script(script_path)
    if not script_code:
        print("⚠️ Script is empty or unreadable.")
        return

    file_name = os.path.basename(script_path)
    print(f"\n🎯 Selected File: {file_name}\n")

    for model in MODELS_TO_COMPARE:
        print(f"🧠 Documenting with {model}...")
        prompt = create_script_documentation_prompt(script_code, file_name, model)
        result, duration = query_ollama(model, prompt)
        if not result:
            print(f"⚠️ {model} returned no response.")
            continue

        print(f"⏱️ Time taken with {model}: {round(duration, 2)} seconds")

        save_to_markdown(
            documentation=result,
            model_name=model,
            source_file=file_name,
            output_dir="../docs"
        )


# === Entrypoint ===
if __name__ == "__main__":
    run_comparison_on_random_script()
