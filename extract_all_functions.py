import os
import ast
import json

# Change this to your repository directory
REPO_DIR = "/Users/setti/Desktop/CompSci422/code_to_doc/Repos"
OUTPUT_JSONL = "functions_raw.jsonl"

def extract_functions_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except Exception as e:
        print(f"⚠️ Failed to parse {filepath}: {e}")
        return []

    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):  # ✅ Removed parent filter
            func_code = ast.get_source_segment(source, node)
            functions.append({
                "filepath": filepath,
                "func_name": node.name,
                "func_code_string": func_code.strip() if func_code else ""
            })
    return functions


def set_parent_links(tree):
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node

def extract_all_functions(repo_dir):
    all_functions = []
    for root, _, files in os.walk(repo_dir):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        source = f.read()
                    tree = ast.parse(source)
                    set_parent_links(tree)
                    all_functions.extend(extract_functions_from_file(full_path))
                except Exception as e:
                    print(f"⚠️ Error reading {full_path}: {e}")
    return all_functions

def save_functions_to_jsonl(functions, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for func in functions:
            json.dump(func, f)
            f.write("\n")

if __name__ == "__main__":
    print(f"🔍 Scanning repo: {REPO_DIR}")
    functions = extract_all_functions(REPO_DIR)
    save_functions_to_jsonl(functions, OUTPUT_JSONL)
    print(f"✅ Extracted {len(functions)} functions. Saved to {OUTPUT_JSONL}")
