#!/usr/bin/env python3
"""
For each raw entry, build a chain-of-thought prompt, invoke Ollama qwen2.5-coder:7b,
and save {prompt,response} back into a final JSONL. Auto-installs `requests` if missing.
Supports resume: skips entries already processed in the final JSONL.
"""
import sys
import subprocess
import os
import json
import time

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

# ─── CONFIGURATION ──────────────────────────────────────────
INPUT_JSONL  = "OCRmyPDF-main_raw.jsonl"
OUTPUT_JSONL = "OCRmyPDF-main_final.jsonl"
OLLAMA_API   = "https://uwvhfyzzyo5gpf-11434.proxy.runpod.net/api/generate"
MODEL_NAME   = "qwen2.5-coder:7b"
# ────────────────────────────────────────────────────────────

SYSTEM_MSG = (
    "You are an expert Python code documentation assistant. "
    "Use Purpose-First Chain-of-Thought when generating documentation: "
    "1. State the high-level purpose of the function or class. "
    "2. Analyze its parameters, behavior, and edge cases. "
    "3. Provide a concise Python docstring or summary."
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


def load_processed_keys(output_file):
    """
    Load the set of (path::name) keys already processed in the final JSONL.
    """
    processed = set()
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    e = json.loads(line)
                    key = f"{e.get('func_path_in_repository')}::{e.get('func_name')}"
                    processed.add(key)
                except Exception:
                    continue
    return processed


def main():
    processed = load_processed_keys(OUTPUT_JSONL)
    total = 0

    try:
        with open(INPUT_JSONL, 'r', encoding='utf-8') as inp, \
             open(OUTPUT_JSONL, 'a', encoding='utf-8') as out:

            for idx, line in enumerate(inp):
                entry = json.loads(line)
                path = entry.get('func_path_in_repository')
                name = entry.get('func_name')
                key = f"{path}::{name}"

                if key in processed:
                    print(f"⏭️ Skipping already-processed: {name} ({path})")
                    continue

                code = entry.get('func_code_string')
                prompt = build_prompt(code, name, path)
                print(f"🧠 [{idx+1}] Prompting: {name} ({path})")
                try:
                    resp = query_ollama(prompt)
                except Exception as e:
                    print(f"❌ Error on {name}: {e}")
                    # Do not exit—allow resume later
                    break

                entry['prompt']   = prompt
                entry['response'] = resp.strip()
                entry['llm_used'] = MODEL_NAME

                json.dump(entry, out)
                out.write('\n')
                out.flush()

                processed.add(key)
                total += 1
                time.sleep(0.5)

    except FileNotFoundError:
        print(f"❌ Input file {INPUT_JSONL} not found. Please run the extraction step first.")
        sys.exit(1)

    print(f"✅ Added {total} new entries to {OUTPUT_JSONL}")

if __name__ == '__main__':
    main()
