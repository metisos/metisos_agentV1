"""
Simple Agent Example

This example demonstrates how to create and use a basic Metis Agent.
"""
import os
from metis_agent import SingleAgent, configure_llm

def main():
    """Run a simple agent example."""
    # Get API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Warning: OPENAI_API_KEY environment variable not set.")
        print("Using mock mode for demonstration purposes.")
    
    # Configure LLM (optional, will use default OpenAI if not specified)
    configure_llm("openai", "gpt-4o", api_key)
    
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