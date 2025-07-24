#!/usr/bin/env python3
"""
Simple Custom Tool Example - Metis Agent Framework

This is a minimal example showing how to create and use a custom tool
with the Metis Agent framework.

Author: Metis Agent Framework
Version: 1.0.0
"""

import os
import sys
from typing import Dict, Any

# Add the metis_agent directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'metis_agent'))

from metis_agent.core.agent import SingleAgent
from metis_agent.core.agent_config import AgentConfig
from metis_agent.tools.base import BaseTool


class SimpleMathTool(BaseTool):
    """A simple custom tool for basic math operations"""
    
    def __init__(self):
        super().__init__()
        self.name = "SimpleMathTool"
        self.description = "Perform basic mathematical calculations"
        self.version = "1.0.0"
    
    def can_handle(self, task: str) -> bool:
        """Check if this tool can handle math-related tasks"""
        math_keywords = ['calculate', 'compute', 'math', 'add', 'subtract', 'multiply', 'divide', '+', '-', '*', '/']
        task_lower = task.lower()
        return any(keyword in task_lower for keyword in math_keywords)
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        """Execute the math calculation"""
        try:
            # Simple expression evaluation (for demo purposes)
            # In production, use a proper math parser for security
            
            # Extract numbers and operation from task
            result = self._parse_and_calculate(task)
            
            return {
                "success": True,
                "data": {
                    "task": task,
                    "result": result,
                    "explanation": f"Calculated result: {result}"
                },
                "tool_used": self.name
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Math calculation failed: {str(e)}",
                "tool_used": self.name,
                "suggestion": "Please provide a clear math expression like '10 + 5' or 'calculate 20 * 3'"
            }
    
    def _parse_and_calculate(self, task: str) -> float:
        """Parse and calculate simple math expressions"""
        import re
        
        # Look for simple patterns like "10 + 5", "calculate 20 * 3", etc.
        patterns = [
            r'(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)',  # Addition
            r'(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)',   # Subtraction
            r'(\d+(?:\.\d+)?)\s*\*\s*(\d+(?:\.\d+)?)',  # Multiplication
            r'(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)',   # Division
        ]
        
        for pattern in patterns:
            match = re.search(pattern, task)
            if match:
                num1, num2 = float(match.group(1)), float(match.group(2))
                
                if '+' in task:
                    return num1 + num2
                elif '-' in task:
                    return num1 - num2
                elif '*' in task:
                    return num1 * num2
                elif '/' in task:
                    if num2 == 0:
                        raise ValueError("Cannot divide by zero")
                    return num1 / num2
        
        # If no pattern matched, try to find just numbers and assume addition
        numbers = re.findall(r'\d+(?:\.\d+)?', task)
        if len(numbers) >= 2:
            return sum(float(num) for num in numbers)
        
        raise ValueError("Could not parse mathematical expression from task")


def create_agent_with_custom_tool():
    """Create an agent with our custom math tool"""
    
    print("Creating Agent with Custom Math Tool...")
    print("=" * 50)
    
    # 1. Create agent configuration
    config = AgentConfig()
    
    # Set up LLM (optional - works without API key for tool testing)
    groq_key = os.getenv('GROQ_API_KEY')
    if groq_key:
        config.set_api_key('groq', groq_key)
        config.set_llm_provider('groq')
        config.set_llm_model('llama-3.1-70b-versatile')
        print("+ LLM configured with Groq")
    else:
        print("+ No API key found - agent will work with tools only")
    
    # 2. Create agent
    agent = SingleAgent(config=config)
    
    # 3. Customize agent identity
    agent.config.set_agent_name("MathBot")
    agent.config.set_personality(
        "You are MathBot, a helpful assistant specialized in mathematical calculations. "
        "You can perform basic arithmetic operations quickly and accurately."
    )
    
    # 4. Create and register custom tool
    math_tool = SimpleMathTool()
    
    # Add tool to agent's tool registry
    if hasattr(agent, 'tool_registry'):
        agent.tool_registry.tools[math_tool.name] = math_tool
        print(f"+ Integrated {math_tool.name} with agent")
    
    identity = agent.get_agent_identity()
    print(f"\nAgent created: {identity.get('name', 'Unknown')} ({identity.get('id', 'Unknown')})")
    print(f"Custom tool available: {math_tool.name}")
    
    return agent, math_tool


def test_custom_tool():
    """Test the custom math tool"""
    
    print("\n" + "=" * 50)
    print("Testing Custom Math Tool")
    print("=" * 50)
    
    # Create agent with custom tool
    agent, math_tool = create_agent_with_custom_tool()
    
    # Test scenarios
    test_queries = [
        "Calculate 15 + 25",
        "What is 100 - 37?",
        "Compute 8 * 9",
        "Divide 144 by 12",
        "Can you add 5.5 + 3.2?",
        "What's the weather like?"  # This should NOT be handled by math tool
    ]
    
    print("\nTesting tool with various queries:")
    print("-" * 40)
    
    for i, query in enumerate(test_queries, 1):
        print(f"\nTest {i}: '{query}'")
        
        # Check if tool can handle the query
        can_handle = math_tool.can_handle(query)
        print(f"Can handle: {can_handle}")
        
        if can_handle:
            # Execute the tool
            result = math_tool.execute(query)
            print(f"Success: {result.get('success', False)}")
            
            if result.get('success'):
                data = result.get('data', {})
                print(f"Result: {data.get('result')}")
                print(f"Explanation: {data.get('explanation')}")
            else:
                print(f"Error: {result.get('error')}")
                if result.get('suggestion'):
                    print(f"Suggestion: {result.get('suggestion')}")


def main():
    """Main execution function"""
    
    print("Simple Custom Tool Example - Metis Agent Framework")
    print("=" * 60)
    print("This example shows how to create a basic custom tool")
    print("and integrate it with a Metis Agent.")
    print()
    
    try:
        # Test the custom tool
        test_custom_tool()
        
        print("\n" + "=" * 60)
        print("Simple Custom Tool Example completed successfully!")
        print("=" * 60)
        print("\nWhat you learned:")
        print("+ How to create a custom tool by inheriting from BaseTool")
        print("+ How to implement can_handle() and execute() methods")
        print("+ How to integrate custom tools with agents")
        print("+ How to test tool functionality")
        print("+ How to handle errors and provide helpful responses")
        print("\nNext Steps:")
        print("1. Modify SimpleMathTool to add more operations")
        print("2. Create tools for your specific domain")
        print("3. Check out custom_tools_template.py for advanced examples")
        print("4. Read CUSTOM_TOOLS_GUIDE.md for detailed documentation")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Please check your setup and try again.")


if __name__ == "__main__":
    main()
