# LLM-Based Code-to-Documentation Generator for Enhanced Code Comprehension

## Overview

The **LLM-Based Code-to-Documentation Generator** is a script-based tool designed to automate the creation of documentation for Python codebases using large language models (LLMs). This tool is particularly beneficial for legacy projects where documentation is often outdated or missing, significantly reducing the time required for new developers to understand, maintain, and extend existing code.

## Problem Statement

In many software projects, especially those managing legacy code, documentation is either inadequate or outdated. This leads to:

- **Delayed Onboarding:** New developers may spend days or weeks reverse engineering over 5,000 lines of uncommented code.
- **Increased Error Risk:** Without proper documentation, there's a higher likelihood of introducing bugs due to misinterpretation or assumptions.
- **Reduced Productivity:** Manual documentation is tedious and often neglected, especially during high-pressure development phases or team transitions.

Addressing these issues can greatly improve code maintainability and overall project efficiency.

## Proposed Solution

The tool leverages LLMs to analyze Python code—inferring functionality through variable names, logical patterns, and usage contexts—to generate:

- **Function-level Documentation:** Docstrings and inline comments explaining the purpose and logic of functions.
- **Module-level Summaries:** High-level overviews of code modules rendered in Markdown or plain text.

This approach not only speeds up the documentation process but also enhances clarity for future maintainers.

## Objectives

- **Automated Documentation Generation:** Convert code segments into clear, technically accurate documentation.
- **Enhanced Coverage:** Achieve at least an 80% documentation coverage in legacy codebases with minimal developer input.
- **Reduced Onboarding Time:** Provide new developers with immediate, AI-generated explanations of code.
- **Export Capabilities:** Allow users to download the documentation in Markdown (.md) or text (.txt) formats.
- **Model Comparison:** Benchmark multiple LLMs for documentation quality.

## Scope

**Included:**
- Documentation generation for Python code input.
- LLM-generated outputs such as docstrings, Markdown summaries.

**Excluded:**
- Support for languages beyond Python (e.g., Java, C++).
- Deep code analysis features like data flow or test generation.
- Integration into CI/CD pipelines.

## Dataset Selection & Evaluation

**Dataset Sources:**
- [discord.py](https://github.com/Rapptz/discord.py)
- [Django](https://github.com/django/django)
- [Flask](https://github.com/pallets/flask)
- [Requests](https://github.com/psf/requests)
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)

**Evaluation Criteria:**
- **Completeness:** Each file or function should receive corresponding documentation.
- **Clarity:** Documentation should be understandable by developers with basic Python knowledge.
- **Accuracy:** Generated content must precisely reflect the code's purpose and structure.
- **Consistency:** Maintain a uniform output style, whether as docstrings, comments, or high-level summaries.

## Architecture & Implementation

- **Backend:** Integrates with Ollama's local models to process Python scripts and produce documentation.
- **Model Comparison:** The script tests four different LLMs:
  - `qwen2.5-coder:7b`
  - `codellama:latest`
  - `codegemma:7b`
  - `qwen2.5-coder:0.5b`
- **File Selection:** The tool randomly selects a `.py` file from a set of local repositories and generates documentation.

## Deliverables

- **Working Script:** CLI-based tool that generates documentation from Python code using multiple models.
- **Evaluation Dataset:** Curated Python scripts for documentation testing.
- **Evaluation Report:** Analysis comparing human-written and LLM-generated documentation.
- **Export Capability:** Documentation is saved in the `docs/` folder for further use.

## Usage

1. **Prepare Repositories:**
   - Clone or download Python repositories you'd like to document.
   - Place them inside the `Repos/` directory in the root folder.

2. **Run the Tool:**
   - The script randomly selects one `.py` file from your `Repos/` folder.
   - It sends the file to each model and collects documentation.

3. **Compare Outputs:**
   - Documentation is saved in `docs/`, one file per model in Markdown format.

4. **Example Command:**
   ```bash
   python new_generator.py
## Installation

1. **Clone the Repository:**
bash
   git clone https://github.com/yourusername/LLM-Code-to-Documentation.git
   cd LLM-Code-to-Documentation