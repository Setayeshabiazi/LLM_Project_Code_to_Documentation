import os

def save_to_markdown(documentation, model_name, source_file, output_dir="docs"):
    """
    Saves the generated documentation to a markdown file.

    Args:
        documentation (str): The LLM-generated documentation.
        model_name (str): Name of the model used to generate the doc.
        source_file (str): Name of the original .py file.
        output_dir (str): Output folder for markdown files.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Generate output file name
    base_name = os.path.splitext(source_file)[0]
    filename = f"{base_name}_{model_name}.md"
    output_path = os.path.join(output_dir, filename)

    # Write just the documentation
    with open(output_path, "w") as f:
        f.write(f"# Documentation for `{source_file}` using `{model_name}`\n\n")
        f.write(documentation.strip())

    print(f"✅ Saved to {output_path}")
def read_full_script(file_path):
    """
    Reads and returns the full content of a Python file.

    Args:
        file_path (str): The path to the .py file.

    Returns:
        str: The contents of the script as a string.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"❌ Failed to read {file_path}: {e}")
        return ""
