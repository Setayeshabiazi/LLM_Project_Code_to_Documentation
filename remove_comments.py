#!/usr/bin/env python3
"""
Recursively strip comments and docstrings from all .py files in a directory.
"""
import os
import io
import tokenize


def strip_comments_and_docstrings(source: str) -> str:
    """
    Remove comments and docstrings from Python source code using the tokenize module.
    """
    io_obj = io.StringIO(source)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0

    try:
        tokens = tokenize.generate_tokens(io_obj.readline)
    except Exception as e:
        return source

    for tok in tokens:
        tok_type, tok_string, (srow, scol), (erow, ecol), _ = tok
        # Skip comments
        if tok_type == tokenize.COMMENT:
            continue
        # Skip docstrings: STRING token at module or def/class level
        if tok_type == tokenize.STRING and prev_toktype == tokenize.INDENT:
            prev_toktype = tok_type
            continue
        # Add spacing if needed
        if srow > last_lineno:
            last_col = 0
        if scol > last_col:
            out += " " * (scol - last_col)
        out += tok_string
        prev_toktype = tok_type
        last_lineno = erow
        last_col = ecol

    return out


def process_directory(src_dir: str, dst_dir: str):
    os.makedirs(dst_dir, exist_ok=True)
    for root, dirs, files in os.walk(src_dir):
        rel = os.path.relpath(root, src_dir)
        tgt_root = os.path.join(dst_dir, rel)
        os.makedirs(tgt_root, exist_ok=True)
        for fname in files:
            if fname.endswith('.py'):
                src_f = os.path.join(root, fname)
                dst_f = os.path.join(tgt_root, fname)
                with open(src_f, 'r', encoding='utf-8') as f:
                    src = f.read()
                cleaned = strip_comments_and_docstrings(src)
                with open(dst_f, 'w', encoding='utf-8') as f:
                    f.write(cleaned)
                print(f"Stripped comments: {src_f} → {dst_f}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: python remove_comments.py <src_dir> <dst_dir>')
        sys.exit(1)
    process_directory(sys.argv[1], sys.argv[2])
