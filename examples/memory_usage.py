"""
Memory Usage Example

This example demonstrates how to use different memory systems with Metis Agent.
"""
import os
from dotenv import load_dotenv
from metis_agent import SingleAgent, configure_llm

# Load environment variables from .env files
load_dotenv()  # Load from .env
load_dotenv('.env.local')  # Load from .env.local (overrides .env)
load_dotenv('templates/.env.local')  # Load from templates/.env.local

def demonstrate_basic_memory():
    """Demonstrate basic SQLite memory usage."""
    print("\n=== Basic Memory Example ===")
    
    # Create an agent with default SQLite memory
    agent = SingleAgent()
    
    # Use a consistent session ID for this conversation
    session_id = "memory_demo_basic"
    
    # First query to establish context
    query1 = "My name is Alice and I'm a software engineer."
    print(f"Query 1: {query1}")
    
    response1 = agent.process_query(query1, session_id=session_id)
    print(f"Response 1:\n{response1}")
    
    # Second query that refers to information from the first query
    query2 = "What is my name and profession?"
    print(f"Query 2: {query2}")
    
    response2 = agent.process_query(query2, session_id=session_id)
    print(f"Response 2:\n{response2}")
    
    # Third query to test memory retention
    query3 = "Can you recommend some programming languages that would be useful for me?"
    print(f"Query 3: {query3}")
    
    response3 = agent.process_query(query3, session_id=session_id)
    print(f"Response 3:\n{response3}")

def demonstrate_titans_memory():
    """Demonstrate Titans-inspired adaptive memory usage."""
    print("\n=== Titans Memory Example ===")
    
    # Create an agent with Titans memory
    agent = SingleAgent(use_titans_memory=True)
    
    # Use a consistent session ID for this conversation
    session_id = "memory_demo_titans"
    
    # First query to establish context
    query1 = "I'm working on a project using Python and TensorFlow for image recognition."
    print(f"Query 1: {query1}")
    
    response1 = agent.process_query(query1, session_id=session_id)
    print(f"Response 1:\n{response1}")
    
    # Second query that builds on the context
    query2 = "What are some best practices for this kind of project?"
    print(f"Query 2: {query2}")
    
    response2 = agent.process_query(query2, session_id=session_id)
    print(f"Response 2:\n{response2}")
    
    # Third query that's somewhat related but different
    query3 = "I'm also interested in natural language processing. How does that compare?"
    print(f"Query 3: {query3}")
    
    response3 = agent.process_query(query3, session_id=session_id)
    print(f"Response 3:\n{response3}")
    
    # Fourth query that refers back to the original context
    query4 = "Going back to my image recognition project, what preprocessing techniques should I consider?"
    print(f"Query 4: {query4}")
    
    response4 = agent.process_query(query4, session_id=session_id)
    print(f"Response 4:\n{response4}")
    
    # Get memory insights
    print("\n=== Memory Insights ===")
    insights = agent.get_memory_insights()
    
    if insights["adaptive_memory"]["enabled"]:
        if "insights" in insights["adaptive_memory"]:
            memory_stats = insights["adaptive_memory"]["insights"]["memory_statistics"]
            print(f"Short-term memories: {memory_stats['short_term_count']}")
            print(f"Long-term memories: {memory_stats['long_term_count']}")
            print(f"Contexts: {memory_stats['context_count']}")
            print(f"Adaptations: {memory_stats['adaptation_count']}")
            print(f"Average surprise: {memory_stats['avg_surprise_recent']:.2f}")
    else:
        print("Titans memory insights not available.")

def demonstrate_multiple_sessions():
    """Demonstrate handling multiple conversation sessions."""
    print("\n=== Multiple Sessions Example ===")
    
    # Create an agent
    agent = SingleAgent()
    
    # Session 1: Talking about programming
    session1_id = "session_programming"
    
    query1_1 = "I want to learn a new programming language. I already know Python and JavaScript."
    print(f"Session 1, Query 1: {query1_1}")
    
    response1_1 = agent.process_query(query1_1, session_id=session1_id)
    print(f"Session 1, Response 1:\n{response1_1}")
    
    # Session 2: Talking about cooking
    session2_id = "session_cooking"
    
    query2_1 = "I'm planning to cook Italian food tonight. What's a good pasta recipe?"
    print(f"Session 2, Query 1: {query2_1}")
    
    response2_1 = agent.process_query(query2_1, session_id=session2_id)
    print(f"Session 2, Response 1:\n{response2_1}")
    
    # Back to Session 1
    query1_2 = "Which one would you recommend for backend development?"
    print(f"Session 1, Query 2: {query1_2}")
    
    response1_2 = agent.process_query(query1_2, session_id=session1_id)
    print(f"Session 1, Response 2:\n{response1_2}")
    
    # Back to Session 2
    query2_2 = "What wine would pair well with that pasta?"
    print(f"Session 2, Query 2: {query2_2}")
    
    response2_2 = agent.process_query(query2_2, session_id=session2_id)
    print(f"Session 2, Response 2:\n{response2_2}")

def main():
    """Run the memory usage examples."""
    # Get Groq API key from environment variable
    groq_api_key = os.environ.get("GROQ_API_KEY")
    if not groq_api_key:
        print("Warning: GROQ_API_KEY environment variable not set.")
        print("Using mock mode for demonstration purposes.")
        return
    
    # Configure LLM to use Groq
    configure_llm("groq", "llama-3.1-8b-instant", groq_api_key)
    
    # Run the examples
    demonstrate_basic_memory()
    demonstrate_titans_memory()
    demonstrate_multiple_sessions()
    
    print("\nMemory usage examples completed!")

if __name__ == "__main__":
    main()