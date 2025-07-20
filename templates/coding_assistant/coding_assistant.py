"""
Coding Assistant Template

This template provides a specialized agent for code generation and explanation.
It leverages the built-in tools from the Metis Agent framework.
"""
import os
from metis_agent import SingleAgent, get_tool, configure_llm

class CodingAssistant:
    """Specialized agent for code generation and explanation."""
    
    def __init__(self, api_key=None, use_titans_memory=True):
        """Initialize the coding assistant."""
        # Create the agent
        self.agent = SingleAgent(
            use_titans_memory=use_titans_memory,
            llm_provider="openai",
            llm_model="gpt-4o"
        )
        
        # Set API keys if provided
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
        
        print("Coding Assistant initialized")
    
    def generate_code(self, requirements, language=None, session_id=None):
        """Generate code based on requirements."""
        # Format the code generation query
        if language:
            query = f"Generate {language} code for: {requirements}"
        else:
            query = f"Generate code for: {requirements}"
        
        # Process the query using the CodeGenerationTool
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="CodeGenerationTool"
        )
        
        return response
    
    def analyze_code(self, code, session_id=None):
        """Analyze the given code."""
        # Format the code analysis query
        query = f"Analyze the following code:\n\n```\n{code}\n```"
        
        # Process the query
        response = self.agent.process_query(
            query,
            session_id=session_id
        )
        
        return response
    
    def explain_code(self, code, session_id=None):
        """Explain the given code."""
        # Format the code explanation query
        query = f"Explain the following code in simple terms:\n\n```\n{code}\n```"
        
        # Process the query
        response = self.agent.process_query(
            query,
            session_id=session_id
        )
        
        return response
    
    def refactor_code(self, code, requirements=None, session_id=None):
        """Refactor the given code."""
        # Format the code refactoring query
        if requirements:
            query = f"Refactor the following code according to these requirements: {requirements}\n\n```\n{code}\n```"
        else:
            query = f"Refactor the following code to improve its quality:\n\n```\n{code}\n```"
        
        # Process the query using the CodeGenerationTool
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="CodeGenerationTool"
        )
        
        return response
    
    def debug_code(self, code, error_message=None, session_id=None):
        """Debug the given code."""
        # Format the debugging query
        if error_message:
            query = f"Debug the following code that produces this error: {error_message}\n\n```\n{code}\n```"
        else:
            query = f"Debug the following code and fix any issues:\n\n```\n{code}\n```"
        
        # Process the query using the CodeGenerationTool
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="CodeGenerationTool"
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
    
    # Refactor code
    print("\nCode Refactoring Request:")
    refactored_code = assistant.refactor_code(sample_code, "Make it more efficient", session_id=session_id)
    print(f"Refactored Code:\n{refactored_code}")

if __name__ == "__main__":
    main()