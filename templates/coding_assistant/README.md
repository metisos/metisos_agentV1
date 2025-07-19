# Coding Assistant Template

This template provides a specialized agent for code generation and explanation. It includes custom tools for code analysis and generation.

## Features

- Code generation based on requirements
- Code analysis and explanation
- Language detection
- Structured output with explanations

## Usage

```python
from coding_assistant import CodingAssistant

# Create the coding assistant
assistant = CodingAssistant(api_key="your_api_key")

# Define a session ID
session_id = "coding_session"

# Generate code
requirements = "Write a Python function to find the nth Fibonacci number using dynamic programming"
generated_code = assistant.generate_code(requirements, session_id=session_id)

# Sample code for analysis
sample_code = """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
"""

# Analyze code
code_analysis = assistant.analyze_code(sample_code, session_id=session_id)

# Explain code
code_explanation = assistant.explain_code(sample_code, session_id=session_id)
```

## Customization

You can customize the coding assistant by:

1. Modifying the `CodeAnalysisTool` class to change how code is analyzed
2. Adjusting the `CodeGenerationTool` class to change how code is generated
3. Adding additional tools for specific coding tasks (e.g., refactoring, optimization)

## Example

See the `coding_assistant.py` file for a complete example of how to use this template.