#!/usr/bin/env python3
"""
Walk the cleaned Project_891 repo and extract every function/class into JSONL.
"""
import os
import ast
import json

#  ─── CONFIGURATION ──────────────────────────────────────────
BASE_REPO_PATH = "../Repos/OCRmyPDF-main_clean"
OUTPUT_JSONL    = "OCRmyPDF-main_raw.jsonl"
REPO_NAME       = "OCRmyPDF-main"
LANGUAGE        = "python"
SPLIT           = "train"
# ────────────────────────────────────────────────────────────

def extract_nodes(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"⚠️ Skipping {file_path}: {e}")
        return []

    rel_path = os.path.relpath(file_path, BASE_REPO_PATH)
    entries = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            code_snip = ast.get_source_segment(source, node)
            entries.append({
                "repository_name": REPO_NAME,
                "func_path_in_repository": rel_path.replace(os.sep, "/"),
                "func_name": node.name,
                "whole_func_string": code_snip,
                "func_code_string": code_snip,
                "func_documentation_string": "",
                "func_code_url": "",
                "language": LANGUAGE,
                "split_name": SPLIT,
                "func_code_tokens": [],
                "func_documentation_tokens": [],
                "llm_used": ""
            })
    return entries

def main():
    all_entries = []
    for root, _, files in os.walk(BASE_REPO_PATH):
        for fn in files:
            if fn.endswith(".py"):
                path = os.path.join(root, fn)
                all_entries.extend(extract_nodes(path))

    with open(OUTPUT_JSONL, "w", encoding="utf-8") as out:
        for e in all_entries:
            json.dump(e, out)
            out.write("\n")
    print(f"✅ Extracted {len(all_entries)} entries → {OUTPUT_JSONL}")

if __name__ == "__main__":
    main()
