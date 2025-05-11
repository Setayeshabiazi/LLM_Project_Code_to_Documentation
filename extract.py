import os
import ast

def get_function_args(node):
    return [arg.arg for arg in node.args.args]

def extract_structure_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
    except Exception as e:
        print(f"⚠️ Skipping {file_path}: {e}")
        return None

    structure = {
        "file": file_path,
        "docstring": ast.get_docstring(tree),
        "classes": [],
        "functions": []
    }

    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef):
            methods = []
            for n in node.body:
                if isinstance(n, ast.FunctionDef):
                    methods.append({
                        "name": n.name,
                        "args": get_function_args(n),
                        "doc": ast.get_docstring(n)
                    })
            structure["classes"].append({
                "name": node.name,
                "doc": ast.get_docstring(node),
                "methods": methods
            })
        elif isinstance(node, ast.FunctionDef):
            structure["functions"].append({
                "name": node.name,
                "args": get_function_args(node),
                "doc": ast.get_docstring(node)
            })

    return structure

def extract_all_py_files(base_dir):
    all_structures = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                result = extract_structure_from_file(full_path)
                if result:
                    all_structures.append(result)
    return all_structures

def print_structures(structures):
    for s in structures:
        print(f"\n📄 {s['file']}")
        if s['docstring']:
            print(f"  📘 Module Docstring: {s['docstring'][:80]}...")
        for func in s["functions"]:
            print(f"  🔹 def {func['name']}({', '.join(func['args'])})")
            if func["doc"]:
                print(f"     📘 {func['doc'][:80]}...")
        for cls in s["classes"]:
            print(f"  🔸 class {cls['name']}:")
            if cls["doc"]:
                print(f"     📘 {cls['doc'][:80]}...")
            for method in cls["methods"]:
                print(f"      • def {method['name']}({', '.join(method['args'])})")
                if method["doc"]:
                    print(f"         📘 {method['doc'][:80]}...")


import json
from collections import Counter


def save_to_markdown(structures, filename="structure.md"):
    stats = Counter(files=0, functions=0, classes=0, methods=0)

    with open(filename, "w", encoding="utf-8") as f:
        for s in structures:
            stats["files"] += 1
            stats["functions"] += len(s["functions"])
            stats["classes"] += len(s["classes"])
            f.write(f"### 📄 `{s['file']}`\n")
            if s['docstring']:
                f.write(f"> 📘 **Module Docstring**: {s['docstring'][:200]}\n\n")
            for func in s["functions"]:
                f.write(f"- 🔹 `def {func['name']}({', '.join(func['args'])})`\n")
                if func["doc"]:
                    f.write(f"  - 📘 {func['doc'][:200]}\n")
            for cls in s["classes"]:
                f.write(f"- 🔸 `class {cls['name']}`\n")
                if cls["doc"]:
                    f.write(f"  - 📘 {cls['doc'][:200]}\n")
                for method in cls["methods"]:
                    stats["methods"] += 1
                    f.write(f"  - • `def {method['name']}({', '.join(method['args'])})`\n")
                    if method["doc"]:
                        f.write(f"    - 📘 {method['doc'][:200]}\n")
            f.write("\n---\n")

        # Summary section
        f.write("\n## 📊 Summary Stats\n")
        f.write(f"- 🗂️ Total Python Files: {stats['files']}\n")
        f.write(f"- 🔹 Total Functions: {stats['functions']}\n")
        f.write(f"- 🔸 Total Classes: {stats['classes']}\n")
        f.write(f"- • Total Methods: {stats['methods']}\n")


def save_to_json(structures, filename="structure.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(structures, f, indent=2)


'''def save_to_markdown(structures, filename="structure.md"):
    with open(filename, "w", encoding="utf-8") as f:
        for s in structures:
            f.write(f"### 📄 `{s['file']}`\n")
            if s['docstring']:
                f.write(f"> 📘 **Module Docstring**: {s['docstring'][:200]}\n\n")
            for func in s["functions"]:
                f.write(f"- 🔹 `def {func['name']}({', '.join(func['args'])})`\n")
                if func["doc"]:
                    f.write(f"  - 📘 {func['doc'][:200]}\n")
            for cls in s["classes"]:
                f.write(f"- 🔸 `class {cls['name']}`\n")
                if cls["doc"]:
                    f.write(f"  - 📘 {cls['doc'][:200]}\n")
                for method in cls["methods"]:
                    f.write(f"  - • `def {method['name']}({', '.join(method['args'])})`\n")
                    if method["doc"]:
                        f.write(f"    - 📘 {method['doc'][:200]}\n")
            f.write("\n---\n")
'''
if __name__ == "__main__":
    base_repo_dir = "/Users/setti/Desktop/CompSci422/code_to_doc/Repos"
    output = extract_all_py_files(base_repo_dir)
    print_structures(output)
    save_to_markdown(output, filename="docs/structure.md")
