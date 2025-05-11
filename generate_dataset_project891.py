#!/usr/bin/env python3
"""
For each raw entry, build a structured prompt, invoke Ollama qwen2.5-coder:7b,
and save {prompt,response} back into a final JSONL. Auto-installs `requests` if missing.
Supports resuming by skipping already-processed entries.
"""
import sys
import subprocess
import os
import json
import time

# -- Ensure requests is available --------------------------------------------
try:
    import requests
except ImportError:
    print("🔧 Installing missing dependency: requests")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "requests"])
    try:
        import requests
    except ImportError:
        print("❌ Failed to install 'requests'. Please install manually.")
        sys.exit(1)

# -- Configuration ----------------------------------------------------------
INPUT_JSONL  = "project891_raw.jsonl"
OUTPUT_JSONL = "project891_final.jsonl"
OLLAMA_API   = "https://uwvhfyzzyo5gpf-11434.proxy.runpod.net/api/generate"
MODEL_NAME   = "qwen2.5-coder:7b"

# -- System prompt (with chain-of-thought) ----------------------------------
SYSTEM_MSG = """
You are an expert Python analyst.

First, think through this code step by step—explain your reasoning for each part before you produce the final write-up:
1. Identify the function or class signature and list its parameters.
2. Summarize the high-level purpose.
3. Analyze each logical block or statement, describing data and control flow.
4. Note any assumptions and how errors are handled.
5. Conclude with a summary of behavior.

Once you’ve worked through those steps, provide a Markdown-formatted explanation with these sections:

## Overview
- A one-sentence description.

## Interface
- Exact signature.
- Parameter table with types and descriptions.

## Inner Workings
- Narrative of the code flow.

## Edge Cases & Preconditions
- Assumptions and potential failures.

## Result Synopsis
- What the code returns or its side effects.

## Docstring Draft
```python
\"\"\"Brief summary.

Args:
    foo (int): ...
Returns:
    bool: ...
Raises:
    ValueError: ...
"""

# -- Helpers -----------------------------------------------------------------
def load_processed_keys(output_file):
    """Return a set of 'path::name' for entries already in output_file."""
    seen = set()
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    e = json.loads(line)
                    seen.add(f"{e['func_path_in_repository']}::{e['func_name']}")
                except Exception:
                    continue
    return seen

# -- Prompt builder ----------------------------------------------------------
def build_prompt(code_str, name, path):
    return json.dumps({
        'system': SYSTEM_MSG,
        'user': f"File: {path}\nFunction/Class: {name}\n```python\n{code_str}\n```",
        'assistant': ''
    })

# -- Ollama query -----------------------------------------------------------
def query_ollama(prompt: str) -> str:
    payload = {'model': MODEL_NAME, 'prompt': prompt, 'stream': False}
    res = requests.post(OLLAMA_API, json=payload)
    res.raise_for_status()
    return res.json().get('response', '')

# -- Main execution ---------------------------------------------------------
def main():
    processed = load_processed_keys(OUTPUT_JSONL)
    added = 0
    try:
        with open(INPUT_JSONL, 'r', encoding='utf-8') as inp, open(OUTPUT_JSONL, 'a', encoding='utf-8') as out:
            for idx, line in enumerate(inp):
                entry = json.loads(line)
                key = f"{entry['func_path_in_repository']}::{entry['func_name']}"
                if key in processed:
                    print(f"⏭️ Skipping: {key}")
                    continue
                prompt = build_prompt(entry['func_code_string'], entry['func_name'], entry['func_path_in_repository'])
                print(f"🧠 [{idx+1}] {entry['func_name']} @ {entry['func_path_in_repository']}")
                try:
                    answer = query_ollama(prompt)
                except Exception as e:
                    print(f"❌ Error on {key}: {e}")
                    break
                entry['prompt']   = prompt
                entry['response'] = answer.strip()
                entry['llm_used'] = MODEL_NAME
                json.dump(entry, out)
                out.write("\n")
                out.flush()
                processed.add(key)
                added += 1
                time.sleep(0.5)
    except FileNotFoundError:
        print(f"❌ Missing {INPUT_JSONL}. Run extraction first.")
        sys.exit(1)
    print(f"✅ Appended {added} entries to {OUTPUT_JSONL}")

if __name__ == '__main__':
    main()
