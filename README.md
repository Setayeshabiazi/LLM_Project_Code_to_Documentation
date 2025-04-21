<<<<<<< HEAD
# LLM-Based Code-to-Documentation Generator for Enhanced Code Comprehension

## Overview

The **LLM-Based Code-to-Documentation Generator** is a web-based tool designed to automate the creation of documentation for Python codebases using large language models (LLMs). This tool is particularly beneficial for legacy projects where documentation is often outdated or missing, significantly reducing the time required for new developers to understand, maintain, and extend existing code.

## Problem Statement

In many software projects, especially those managing legacy code, documentation is either inadequate or outdated. This leads to:

- **Delayed Onboarding:** New developers may spend days or weeks reverse engineering over 5,000 lines of uncommented code.
- **Increased Error Risk:** Without proper documentation, there's a higher likelihood of introducing bugs due to misinterpretation or assumptions.
- **Reduced Productivity:** Manual documentation is tedious and often neglected, especially during high-pressure development phases or team transitions.

Addressing these issues can greatly improve code maintainability and overall project efficiency.

## Proposed Solution

The tool leverages an LLM to analyze Python code—inferring functionality through variable names, logical patterns, and usage contexts—to generate:

- **Function-level Documentation:** Docstrings and inline comments explaining the purpose and logic of functions.
- **Module-level Summaries:** High-level overviews of code modules rendered in Markdown or plain text.

This approach not only speeds up the documentation process but also enhances clarity for future maintainers.

## Objectives

- **Web-Based Interface:** Build a user-friendly interface (using Streamlit) that accepts raw Python code and displays side-by-side generated documentation.
- **Automated Documentation Generation:** Convert code segments into clear, technically accurate documentation.
- **Enhanced Coverage:** Achieve at least an 80% documentation coverage in legacy codebases with minimal developer input.
- **Reduced Onboarding Time:** Provide new developers with immediate, AI-generated explanations of code.
- **Export Capabilities:** Allow users to download the documentation in Markdown (.md) or text (.txt) formats.

## Scope

**Included:**
- Documentation generation for Python code input.
- LLM-generated outputs such as docstrings, Markdown summaries, and inline comments.
- A Streamlit-based interface for demo and testing purposes.

**Excluded:**
- Support for languages beyond Python (e.g., Java, C++).
- Deep code analysis features like data flow or test generation.
- Integration into CI/CD pipelines for the MVP.


## Dataset Selection & Evaluation

**Dataset Sources:**
- [discord.py](https://github.com/Rapptz/discord.py) – A Python wrapper for the Discord API
- [Django](https://github.com/django/django) – A high-level Python web framework
- [Flask](https://github.com/pallets/flask) – A lightweight Python web application framework
- [Requests](https://github.com/psf/requests) – A popular Python HTTP library
- [scikit-learn](https://github.com/scikit-learn/scikit-learn) – A machine learning library for Python

These open-source repositories were downloaded and used to extract various Python scripts for testing the documentation generation tool.

**Evaluation Criteria:**
- **Completeness:** Each file or function should receive corresponding documentation.
- **Clarity:** Documentation should be understandable by developers with basic Python knowledge.
- **Accuracy:** Generated content must precisely reflect the code's purpose and structure.
- **Consistency:** Maintain a uniform output style, whether as docstrings, comments, or high-level summaries.

## Architecture & Implementation

- **Frontend:** Built with Streamlit for an interactive web experience that accepts code input and displays LLM-generated documentation.
- **Backend:** Integrates with OpenAI's GPT model to process input code and produce documentation.
- **Export Options:** Documentation can be downloaded as Markdown (.md) or plain text (.txt) files for seamless integration into project wikis or documentation repositories.

## Deliverables

- **Working Web Tool:** An interactive application that accepts Python code snippets or files and displays generated documentation side-by-side.
- **Evaluation Dataset:** A curated set of Python code samples sourced from well-known repositories for robust testing.
- **Evaluation Report:** A comparative analysis between human-written and LLM-generated documentation, highlighting time savings and improved clarity.
- **Export Capability:** Functionality to download the generated documentation for further use.

## Usage

1. **Input Your Code:** Paste your Python code or upload a Python file via the Streamlit interface.
2. **Generate Documentation:** The LLM will process the code and generate corresponding documentation automatically.
3. **Review Side-by-Side:** Compare the original code and the AI-generated documentation in the interface.
4. **Export Documentation:** Download the generated documentation as a `.md` or `.txt` file for inclusion in project docs or wikis.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/LLM-Code-to-Documentation.git
   cd LLM-Code-to-Documentation
