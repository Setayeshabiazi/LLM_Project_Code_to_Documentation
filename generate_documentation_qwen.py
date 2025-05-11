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
#Chain of thought prompt
#   "You are an expert Python code documentation assistant. "
#     "Use Purpose-First Chain-of-Thought when generating documentation: "
#     "1. State the high-level purpose of the function or class. "
#     "2. Analyze its parameters, behavior, and edge cases. "
#     "3. Provide a concise Python docstring or summary."

#Chain of thought prompt
# You are a precise code‑documentation assistant. For the code below, think step by step—first identify its purpose, then list parameters and return values, then draft the docstring.
#
# Code:
# ```python
# def merge_dicts(a, b):
#     result = a.copy()
#     result.update(b)
#     return result
#

#Zero Shot prompt
# You are an expert code‑documentation assistant. For the following code snippet, produce:
#
# 1. A one‑sentence summary of what it does.
# 2. A fully formatted docstring (or code comment) including:
#    - Purpose
#    - Arguments (with types)
#    - Return value (with type)
#    - Side effects or exceptions (if any)
#
# Do **not** show your reasoning—only output the summary and the documentation.
#
# Code:
# ```python
#
#
# class SerialExecutor(Executor):
#
#     def _execute(
#             self,
#             *,
#             use_threads: bool,
#             max_workers: int,
#             progress_kwargs: dict,
#             worker_initializer: Callable,
#             task: Callable,
#             task_arguments: Iterable,
#             task_finished: Callable,
#     ):
#         with self.pbar_class(**progress_kwargs) as pbar:
#             for args in task_arguments:
#                 result = task(*args)
#                 task_finished(result, pbar)

# Zero Shot prompt
# You are an expert code‑documentation assistant. For the following code, output:
# 1. A one‑sentence summary.
# 2. A complete PEP‑257 docstring (with Args, Returns, Raises).
#
# Do not show your reasoning.
#
# Code:
# ```python
# def get_page_contexts(self) -> Iterator[PageContext]:
#     npages = len(self.pdfinfo)
#     for n in range(npages):
#         yield PageContext(self, n)


#Chain of Thought Edge Case Exploration Prompt
#
# Analyze potential edge cases for this code (e.g., empty inputs, negative numbers). List them, then generate a robust docstring covering those cases.
#
# Code:
# ```python
# def get_page_contexts(self) -> Iterator[PageContext]:
#     npages = len(self.pdfinfo)
#     for n in range(npages):
#         yield PageContext(self, n)


### Comparative Analysis CoT
#
# Compare this implementation to a simpler version (no defaults, no error checking). Note pros/cons in 3 steps. Then produce a full docstring.
#
# Code:
# ```python
# def get_page_contexts(self) -> Iterator[PageContext]:
#     npages = len(self.pdfinfo)
#     for n in range(npages):
#         yield PageContext(self, n)


### Combined Advanced CoT
#
# You’re a senior engineer documenting critical code. First:
# 1. Trace execution on sample inputs.
# 2. Enumerate edge cases.
# 3. Compare to a naïve version.
#
# Then write a Sphinx‑style docstring covering all insights.
#
# Code:
# ```python
# def get_page_contexts(self) -> Iterator[PageContext]:
#     npages = len(self.pdfinfo)
#     for n in range(npages):
#         yield PageContext(self, n)

### Function Tracing Prompt
#
# Before you document, trace the function’s behavior on sample inputs. Then write the docstring.
#
# Code:
# ```python
# def get_page_contexts(self) -> Iterator[PageContext]:
#     npages = len(self.pdfinfo)
#     for n in range(npages):
#         yield PageContext(self, n)

## Chain‑of‑Thought
#
# You are a meticulous docstring writer. Think step-by-step:
#
# 1. Identify purpose.
# 2. List parameters and types.
# 3. Determine return and exceptions.
# 4. Draft the docstring.
#
# Code:
# ```python
# def get_page_contexts(self) -> Iterator[PageContext]:
#     npages = len(self.pdfinfo)
#     for n in range(npages):
#         yield PageContext(self, n)


# Few‑Shot
#
# You are a Python documentation generator. Follow the style of the examples:
#
# ### Example 1
# ```python
# def inc(x):
#     return x + 1
# def inc(x: int) -> int:
#     """
#     Increment an integer by one.
#
#     Args:
#         x (int): Input integer.
#     Returns:
#         int: x plus one.
#     """



# Generate a Markdown API reference for this function:
# - Title
# - Description
# - Parameters (with types)
# - Return type
# - Example usage
#
# Code:
# ```python
# def get_page_contexts(self) -> Iterator[PageContext]:
#     npages = len(self.pdfinfo)
#     for n in range(npages):
#         yield PageContext(self, n)

#Produce concise inline `#` comments explaining each block of logic in the code below.
# Code:
# ```python
# def get_page_contexts(self) -> Iterator[PageContext]:
#     npages = len(self.pdfinfo)
#     for n in range(npages):
#         yield PageContext(self, n)

### Combined CoT
# You’re a senior Python engineer. Do the following:
# 1. Run a quick manual trace on inputs.
# 2. Enumerate edge cases.
# 3. Compare to a simpler variant.
# 4. Write a comprehensive Google‑style docstring.
#
# Code:
# ```python
# def get_page_contexts(self) -> Iterator[PageContext]:
#     npages = len(self.pdfinfo)
#     for n in range(npages):
#         yield PageContext(self, n)


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
