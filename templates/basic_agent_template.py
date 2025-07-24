#!/usr/bin/env python3
"""
Basic Metis Agent Template

This template shows how to create and use a Metis Agent programmatically.
Perfect for simple chatbot applications or basic AI assistance.

Usage:
    python basic_agent_template.py
"""

from metis_agent import SingleAgent
from metis_agent.core.agent_config import AgentConfig
import os

def create_basic_agent():
    """
    Create a basic Metis Agent with default configuration.
    
    Returns:
        SingleAgent: Configured agent instance
    """
    # Initialize agent configuration
    config = AgentConfig()
    
    # Create the agent
    agent = SingleAgent(config)
    
    return agent

def setup_api_keys():
    """
    Setup API keys for LLM providers.
    
    Note: You can also set these via environment variables:
    - GROQ_API_KEY
    - OPENAI_API_KEY  
    - ANTHROPIC_API_KEY
    """
    print("Setting up API keys...")
    
    # Option 1: Set via environment variables (recommended)
    # os.environ['GROQ_API_KEY'] = 'your_groq_api_key_here'
    
    # Option 2: Set via agent configuration (programmatic)
    config = AgentConfig()
    # config.set_api_key('groq', 'your_groq_api_key_here')
    
    print("API keys configured. Make sure to set your actual keys!")

def main():
    """
    Main function demonstrating basic agent usage.
    """
    print("=== Basic Metis Agent Template ===")
    print()
    
    # Setup API keys (you need to configure these)
    setup_api_keys()
    
    # Create the agent
    print("Creating agent...")
    agent = create_basic_agent()
    
    # Get agent identity information
    identity = agent.get_agent_identity()
    print(f"Agent created successfully!")
    print(f"Agent Name: {identity.get('agent_name', 'Unknown')}")
    print(f"Agent ID: {identity.get('agent_id', 'Unknown')}")
    print()
    
    # Example conversation
    print("Starting conversation...")
    print("-" * 50)
    
    # Example queries
    queries = [
        "Hello! What's your name?",
        "What can you help me with?",
        "Can you explain what you are?",
    ]
    
    for query in queries:
        print(f"User: {query}")
        try:
            response = agent.process_query(query)
            print(f"Agent: {response}")
        except Exception as e:
            print(f"Error: {e}")
            print("Make sure you have configured your API keys!")
        print()
    
    print("-" * 50)
    print("Conversation complete!")

if __name__ == "__main__":
    main()
