"""
Coding Assistant Template

This template provides a specialized agent for code generation and explanation.
"""
import os
import re
from metis_agent import SingleAgent, BaseTool, register_tool

class CodeAnalysisTool(BaseTool):
    """Tool for analyzing code."""
    
    name = "code_analysis_tool"
    description = "Analyzes code and provides insights"
    
    def can_handle(self, task):
        """Determine if this tool can handle the task."""
        analysis_keywords = [
            "analyze code", "review code", "explain code", "understand code",
            "code analysis", "code review", "code explanation"
        ]
        return any(keyword in task.lower() for keyword in analysis_keywords)
        
    def execute(self, task):
        """Execute the code analysis task."""
        # Extract code from the task
        code = self._extract_code(task)
        
        if not code:
            return "No code found to analyze. Please provide code snippets enclosed in triple backticks."
        
        # Analyze the code
        analysis = self._analyze_code(code)
        
        return analysis
    
    def _extract_code(self, task):
        """Extract code from the task."""
        # Look for code blocks enclosed in triple backticks
        code_blocks = re.findall(r'```(?:\w+)?\n(.*?)```', task, re.DOTALL)
        
        if code_blocks:
            return code_blocks[0]
        
        return None
    
    def _analyze_code(self, code):
        """Analyze the code and provide insights."""
        # In a real implementation, this would use code analysis tools
        
        # Determine the language (simplified)
        language = self._detect_language(code)
        
        analysis = f"# Code Analysis\n\n"
        analysis += f"## Language: {language}\n\n"
        
        analysis += "## Structure\n\n"
        analysis += "The code consists of the following components:\n"
        
        # Count lines
        lines = code.split('\n')
        analysis += f"- {len(lines)} lines of code\n"
        
        # Count functions/methods (simplified)
        if language == "Python":
            functions = len(re.findall(r'def\s+\w+\s*\(', code))
            analysis += f"- {functions} functions/methods\n"
        elif language == "JavaScript":
            functions = len(re.findall(r'function\s+\w+\s*\(|const\s+\w+\s*=\s*\(', code))
            analysis += f"- {functions} functions/methods\n"
        
        analysis += "\n## Key Observations\n\n"
        analysis += "1. The code appears to be [purpose of the code]\n"
        analysis += "2. It uses [key libraries/frameworks/patterns]\n"
        analysis += "3. [Other observations]\n\n"
        
        analysis += "## Potential Improvements\n\n"
        analysis += "1. [Improvement suggestion]\n"
        analysis += "2. [Improvement suggestion]\n"
        analysis += "3. [Improvement suggestion]\n"
        
        return analysis
    
    def _detect_language(self, code):
        """Detect the programming language of the code."""
        # This is a simplified implementation
        if "def " in code and ":" in code:
            return "Python"
        elif "function " in code or "const " in code or "let " in code:
            return "JavaScript"
        elif "public class " in code or "private " in code:
            return "Java"
        elif "#include" in code:
            return "C/C++"
        else:
            return "Unknown"


class CodeGenerationTool(BaseTool):
    """Tool for generating code."""
    
    name = "code_generation_tool"
    description = "Generates code based on requirements"
    
    def can_handle(self, task):
        """Determine if this tool can handle the task."""
        generation_keywords = [
            "generate code", "write code", "create code", "implement",
            "code for", "function for", "program for"
        ]
        return any(keyword in task.lower() for keyword in generation_keywords)
        
    def execute(self, task):
        """Execute the code generation task."""
        # Extract requirements from the task
        language = self._extract_language(task)
        
        # Generate code based on requirements
        code = self._generate_code(task, language)
        
        return code
    
    def _extract_language(self, task):
        """Extract the programming language from the task."""
        # This is a simplified implementation
        task_lower = task.lower()
        
        languages = {
            "python": ["python", "py"],
            "javascript": ["javascript", "js", "node"],
            "java": ["java"],
            "c++": ["c++", "cpp"],
            "c#": ["c#", "csharp"],
            "go": ["go", "golang"],
            "ruby": ["ruby"],
            "php": ["php"],
            "swift": ["swift"],
            "typescript": ["typescript", "ts"]
        }
        
        for lang, keywords in languages.items():
            if any(keyword in task_lower for keyword in keywords):
                return lang
        
        # Default to Python if no language is specified
        return "python"
    
    def _generate_code(self, task, language):
        """Generate code based on requirements and language."""
        # In a real implementation, this would use the LLM to generate code
        
        response = f"# Generated {language.capitalize()} Code\n\n"
        response += "```" + language.lower() + "\n"
        
        if language.lower() == "python":
            response += "def main():\n"
            response += "    # TODO: Implement the functionality based on requirements\n"
            response += "    print('Hello, world!')\n\n"
            response += "if __name__ == '__main__':\n"
            response += "    main()\n"
        elif language.lower() == "javascript":
            response += "function main() {\n"
            response += "    // TODO: Implement the functionality based on requirements\n"
            response += "    console.log('Hello, world!');\n"
            response += "}\n\n"
            response += "main();\n"
        else:
            response += "// Generated code for " + language + "\n"
            response += "// TODO: Implement the functionality based on requirements\n"
        
        response += "```\n\n"
        
        response += "## Explanation\n\n"
        response += "This code provides a basic structure for the requested functionality. Here's how it works:\n\n"
        response += "1. [Explanation of the code structure]\n"
        response += "2. [Explanation of key components]\n"
        response += "3. [Explanation of how to use/extend the code]\n"
        
        return response


class CodingAssistant:
    """Specialized agent for code generation and explanation."""
    
    def __init__(self, api_key=None, use_titans_memory=True):
        """Initialize the coding assistant."""
        # Register the coding tools
        register_tool("code_analysis_tool", CodeAnalysisTool)
        register_tool("code_generation_tool", CodeGenerationTool)
        
        # Create the agent
        self.agent = SingleAgent(
            use_titans_memory=use_titans_memory,
            llm_provider="openai",
            llm_model="gpt-4o"
        )
        
        print("Coding Assistant initialized")
    
    def generate_code(self, requirements, session_id=None):
        """Generate code based on requirements."""
        # Process the requirements
        response = self.agent.process_query(
            f"Generate code for: {requirements}",
            session_id=session_id,
            tool_name="code_generation_tool"
        )
        
        return response
    
    def analyze_code(self, code, session_id=None):
        """Analyze the given code."""
        # Process the code analysis request
        response = self.agent.process_query(
            f"Analyze the following code:\n\n```\n{code}\n```",
            session_id=session_id,
            tool_name="code_analysis_tool"
        )
        
        return response
    
    def explain_code(self, code, session_id=None):
        """Explain the given code."""
        # Process the code explanation request
        response = self.agent.process_query(
            f"Explain the following code in simple terms:\n\n```\n{code}\n```",
            session_id=session_id
        )
        
        return response


def main():
    """Run a demonstration of the coding assistant."""
    # Get API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    
    # Create the coding assistant
    assistant = CodingAssistant(api_key=api_key)
    
    # Define a session ID
    session_id = "coding_session"
    
    # Generate code
    requirements = "Write a Python function to find the nth Fibonacci number using dynamic programming"
    print(f"Code Generation Request: {requirements}")
    
    generated_code = assistant.generate_code(requirements, session_id=session_id)
    print(f"Generated Code:\n{generated_code}")
    
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
    print("\nCode Analysis Request:")
    code_analysis = assistant.analyze_code(sample_code, session_id=session_id)
    print(f"Code Analysis:\n{code_analysis}")
    
    # Explain code
    print("\nCode Explanation Request:")
    code_explanation = assistant.explain_code(sample_code, session_id=session_id)
    print(f"Code Explanation:\n{code_explanation}")

if __name__ == "__main__":
    main()