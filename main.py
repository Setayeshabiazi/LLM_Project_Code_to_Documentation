#!/usr/bin/env python3
"""
Master launcher for the Project_891 documentation pipeline.
This script sequentially invokes:
  1) remove_comments.py
  2) extract_to_jsonl_project891.py
  3) generate_dataset_project891.py

Usage:
  python run_pipeline.py [--src SRC_DIR] [--clean CLEAN_DIR] [--raw RAW_JSONL] [--out FINAL_JSONL]
"""
import subprocess
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description='Run full Project_891 documentation pipeline via auxiliary scripts.'
    )
    parser.add_argument(
        '--src',   default='Repos/Project_891',
        help='Original Project_891 repo directory'
    )
    parser.add_argument(
        '--clean', default='Repos/Project_891_clean',
        help='Directory for cleaned Python files'
    )
    parser.add_argument(
        '--raw',   default='project891_raw.jsonl',
        help='Output path for raw extraction JSONL'
    )
    parser.add_argument(
        '--out',   default='project891_final.jsonl',
        help='Output path for final documentation JSONL'
    )
    args = parser.parse_args()

    # 1. Strip comments & docstrings
    print("\n=== Step 1: Removing comments & docstrings ===")
    ret = subprocess.run([
        sys.executable,
        'remove_comments.py',
        args.src,
        args.clean
    ], check=False)
    if ret.returncode != 0:
        print('❌ remove_comments.py failed. Aborting.')
        sys.exit(ret.returncode)

    # 2. Extract functions & classes
    print("\n=== Step 2: Extracting functions/classes to raw JSONL ===")
    ret = subprocess.run([
        sys.executable,
        'extract_to_jsonl_project891.py'
    ], check=False)
    if ret.returncode != 0:
        print('❌ extract_to_jsonl_project891.py failed. Aborting.')
        sys.exit(ret.returncode)

    # 3. Generate CoT prompts & collect docs
    print("\n=== Step 3: Generating CoT documentation ===")
    ret = subprocess.run([
        sys.executable,
        'generate_dataset_project891.py'
    ], check=False)
    if ret.returncode != 0:
        print('❌ generate_dataset_project891.py failed. Aborting.')
        sys.exit(ret.returncode)

    print("\n✅ Pipeline complete. Final output in {}".format(args.out))


if __name__ == '__main__':
    main()
