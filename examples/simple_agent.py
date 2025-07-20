"""
Simple Agent Example

This example demonstrates how to create and use a basic Metis Agent.
"""
import os
from dotenv import load_dotenv
from metis_agent import SingleAgent, configure_llm, APIKeyManager

# Load environment variables from .env files
load_dotenv()  # Load from .env
load_dotenv('.env.local')  # Load from .env.local (overrides .env)
load_dotenv('templates/.env.local')  # Load from templates/.env.local

def main():
    """Run a simple agent example."""
    print("=== API Key Setup ===")
    
    # Option 1: Use APIKeyManager to get API keys
    key_manager = APIKeyManager()
    groq_api_key = key_manager.get_key("groq")  # Checks env vars first, then secure storage
    
    # Option 2: Or get directly from environment (for comparison)
    env_key = os.environ.get("GROQ_API_KEY")
    
    if groq_api_key:
        if env_key:
            print("+ GROQ_API_KEY found in environment variables")
        else:
            print("+ GROQ_API_KEY found in secure storage")
        # Configure LLM to use Groq
        configure_llm("groq", "llama-3.1-8b-instant", groq_api_key)
    else:
        print("- GROQ_API_KEY not found in environment or secure storage")
        print("- Using mock mode for demonstration purposes")
        print("\nTip: Set up API keys using:")
        print("  1. Environment variables: GROQ_API_KEY=your-key")
        print("  2. APIKeyManager: key_manager.set_key('groq', 'your-key')")
        print("  3. See examples/api_key_management.py for full demo")

    
    # Create an agent
    agent = SingleAgent()
    
    # Process a simple question
    print("\n=== Processing a simple question ===")
    question = "What are the three laws of robotics?"
    print(f"Question: {question}")
    
    response = agent.process_query(question)
    print(f"Response:\n{response}")
    
    # Process a more complex task
    print("\n=== Processing a complex task ===")
    task = "Write a Python function to find the prime factors of a number"
    print(f"Task: {task}")
    
    response = agent.process_query(task)
    print(f"Response:\n{response}")
    
    # Using session context for follow-up questions
    print("\n=== Using session context ===")
    session_id = "demo_session"
    
    # First query
    query1 = "What is machine learning?"
    print(f"Query 1: {query1}")
    response1 = agent.process_query(query1, session_id=session_id)
    print(f"Response 1:\n{response1}")
    
    # Follow-up query (uses context from first query)
    query2 = "What are the main types?"
    print(f"Query 2: {query2}")
    response2 = agent.process_query(query2, session_id=session_id)
    print(f"Response 2:\n{response2}")
    
    print("\nSimple agent example completed!")

if __name__ == "__main__":
    main()