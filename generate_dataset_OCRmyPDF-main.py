#!/usr/bin/env python3
"""
For each raw entry, build a chain-of-thought prompt, invoke Ollama qwen2.5-coder:7b,
and save {prompt,response} back into a final JSONL. Auto-installs `requests` if missing.
"""
import sys
import subprocess
import os

# Ensure `requests` is installed
try:
    import requests
except ImportError:
    print("🔧 Installing missing dependency: requests")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "requests"])
    try:
        import requests
    except ImportError:
        print("❌ Failed to install 'requests'. Please install manually and re-run.")
        sys.exit(1)

import json
import time

# ─── CONFIGURATION ──────────────────────────────────────────
INPUT_JSONL   = "OCRmyPDF-main_raw.jsonl"
OUTPUT_JSONL  = "OCRmyPDF-main_final.jsonl"
base = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434").rstrip('/')
OLLAMA_API = f"{base}/api/generate"
MODEL_NAME    = "qwen2.5-coder:7b"
# ────────────────────────────────────────────────────────────

SYSTEM_MSG = (
    "You are a helpful Python code explainer. "
    "Explain the code below step by step (chain of thought), then provide a concise summary."
)

def build_prompt(code_str, name, path):
    return json.dumps({
        'system': SYSTEM_MSG,
        'user': f"File: {path}\nFunction/Class: {name}\n```python\n{code_str}\n```",
        'assistant': ''
    })

def query_ollama(prompt: str) -> str:
    res = requests.post(OLLAMA_API, json={
        'model': MODEL_NAME,
        'prompt': prompt,
        'stream': False
    })
    res.raise_for_status()
    return res.json().get('response', '')

def main():
    out_entries = []
    try:
        with open(INPUT_JSONL, 'r', encoding='utf-8') as inp:
            for idx, line in enumerate(inp):
                entry = json.loads(line)
                code = entry.get('func_code_string')
                name = entry.get('func_name')
                path = entry.get('func_path_in_repository')

                prompt = build_prompt(code, name, path)
                print(f"🧠 [{idx+1}] Prompting: {name} ({path})")
                resp = query_ollama(prompt)

                entry['prompt']   = prompt
                entry['response'] = resp.strip()
                entry['llm_used'] = MODEL_NAME
                out_entries.append(entry)

                time.sleep(0.5)
    except FileNotFoundError:
        print(f"❌ Input file {INPUT_JSONL} not found. Please run extraction first.")
        sys.exit(1)

    with open(OUTPUT_JSONL, 'w', encoding='utf-8') as out:
        for e in out_entries:
            json.dump(e, out)
            out.write('\n')
    print(f"✅ Finished → {OUTPUT_JSONL}")

if __name__ == '__main__':
    main()
