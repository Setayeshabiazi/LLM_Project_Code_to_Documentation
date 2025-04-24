import os
import ast
import json

BASE_REPO_PATH = "/Users/setti/Desktop/CompSci422/code_to_doc/Repos"  # Modify if needed
REPO_NAME = "setti/code_to_doc"  # Modify if needed
OUTPUT_JSONL = "code2doc_raw_dataset.jsonl"

def extract_function_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"⚠️ Skipping {file_path} due to syntax error: {e}")
        return []
    rel_path = os.path.relpath(file_path, start=BASE_REPO_PATH)

    functions = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            func_code = ast.get_source_segment(source, node)
            name = node.name
            url = f"https://github.com/{REPO_NAME}/blob/main/{rel_path}#L{node.lineno}"

            functions.append({
                "repository_name": REPO_NAME,
                "func_path_in_repository": rel_path,
                "func_name": name,
                "whole_func_string": func_code,
                "func_code_string": func_code,
                "func_documentation_string": "",  # To be filled later
                "func_code_url": url,
                "language": "python",
                "split_name": "train",
                "func_code_tokens": [],
                "func_documentation_tokens": [],
                "llm_used": ""
            })
    return functions

all_entries = []
for root, _, files in os.walk(BASE_REPO_PATH):
    for file in files:
        if file.endswith(".py"):
            full_path = os.path.join(root, file)
            all_entries.extend(extract_function_data(full_path))

with open(OUTPUT_JSONL, "w", encoding="utf-8") as out:
    for entry in all_entries:
        json.dump(entry, out)
        out.write("\n")

print(f"✅ Extracted {len(all_entries)} functions/classes to {OUTPUT_JSONL}")
