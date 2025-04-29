#!/usr/bin/env python3
"""
Generate Markdown documentation for all Python functions/classes in a cleaned TA-Scheduling-Application repo
using Purpose-First Chain-of-Thought prompts.
"""
import os
import ast
import json
import requests
import time

# ─── CONFIGURATION ──────────────────────────────────────────
REPO_PATH = "/Users/jiahuiyang/PycharmProjects/LLM_Project_Code_to_Documentation/Repos/TA-Scheduling-Application-main_clean"
OUTPUT_MD = "TA-Scheduling-Application-main_clean_documentation.md"
OLLAMA_API_URL = "https://8apzscny2b8q3e-11434.proxy.runpod.net/api/generate"
MODEL_NAME = "qwen2.5-coder:7b"
# ────────────────────────────────────────────────────────────

# Purpose-First Chain-of-Thought system message
SYSTEM_MSG = """
You are an expert Python code documentation assistant and analyst.
Use Purpose-First Chain-of-Thought to guide your reasoning:
1. Identify the function or class signature and list its parameters.
2. Summarize the high-level purpose.
3. Analyze each logical block or statement, describing data and control flow.
4. Note any assumptions and how errors are handled.
5. Conclude with a concise behavior summary.

Once you’ve worked through those steps, produce a Markdown-formatted explanation with these sections:

## Overview
- A one-sentence description of what this code does.

## Interface
- **Signature**: the exact function or class signature.
- **Parameters**: a table listing name, type, and purpose.

## Inner Workings
- Narrative of the code’s data flow and control flow, in bullet points or short paragraphs.

## Edge Cases & Preconditions
- Any assumptions, potential failure modes, and error-handling logic.

## Result Synopsis
- What the code returns or its side effects.

## Docstring Draft
```python
\"\"\"Brief summary.

Args:
    foo (int): Description of `foo`.
    bar (str): Description of `bar`.

Returns:
    bool: What the function returns.

Raises:
    ValueError: When `foo` is negative.
\"\"\"
```"""

# Build the prompt for a given code snippet
def build_prompt(code_str: str, name: str, path: str) -> str:
    return f"""{SYSTEM_MSG}

File path: {path}
Function/Class: {name}
```python
{code_str}
```"""

# Query Ollama HTTP API
def query_ollama(prompt: str) -> str:
    payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
    resp = requests.post(OLLAMA_API_URL, json=payload)
    resp.raise_for_status()
    return resp.json().get("response", "").strip()

# Extract functions and classes from a Python file
def extract_defs_from_file(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        source = f.read()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    entries = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            code_snip = ast.get_source_segment(source, node) or ''
            entries.append((node.name, code_snip))
    return entries

# Main: walk repo, generate docs, write markdown
def main():
    docs_md = []
    start = time.time()

    for root, _, files in os.walk(REPO_PATH):
        for fn in files:
            if not fn.endswith('.py'):
                continue
            filepath = os.path.join(root, fn)
            relpath = os.path.relpath(filepath, REPO_PATH)
            defs = extract_defs_from_file(filepath)
            if not defs:
                continue
            for name, code in defs:
                prompt = build_prompt(code, name, relpath)
                print(f"🧠 Documenting {name} in {relpath}")
                doc = query_ollama(prompt)
                # Build markdown section
                docs_md.append(f"## {name}  \n``/{relpath}``  \n```{code}```  \n")
                docs_md.append("**Documentation:**")
                docs_md.append(f"```python{doc}```\n")
                time.sleep(0.5)

    # Write to markdown file
    with open(OUTPUT_MD, 'w', encoding='utf-8') as mdfile:
        mdfile.write("# TA-Scheduling-Application-main Cleaned Repo Documentation\n\n")
        mdfile.write("\n".join(docs_md))

    elapsed = round((time.time() - start)/60, 2)
    print(f"✅ Documentation written to {OUTPUT_MD} in {elapsed} minutes.")

if __name__ == '__main__':
    main()
