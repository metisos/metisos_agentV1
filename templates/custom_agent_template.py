#!/usr/bin/env python3
"""
Custom Metis Agent Template

This template shows how to create a customized Metis Agent with:
- Custom agent identity and personality
- Specific LLM provider configuration
- Memory and tool settings
- Enhanced processing options

Usage:
    python custom_agent_template.py
"""

from metis_agent import SingleAgent
from metis_agent.core.agent_config import AgentConfig
import os

def create_custom_agent(
    agent_name="CodeMentor",
    personality="You are a senior software engineer and coding mentor. You specialize in helping developers write clean, efficient code and solve complex programming problems. You provide detailed explanations and best practices.",
    llm_provider="groq",
    llm_model="llama-3.1-8b-instant",
    enable_memory=True,
    enable_titans=True
):
    """
    Create a customized Metis Agent with specific configuration.
    
    Args:
        agent_name (str): Custom name for the agent
        personality (str): Custom personality/role for the agent
        llm_provider (str): LLM provider ('groq', 'openai', 'anthropic')
        llm_model (str): Specific model to use
        enable_memory (bool): Enable conversation memory
        enable_titans (bool): Enable Titans memory enhancement
    
    Returns:
        SingleAgent: Configured custom agent
    """
    # Initialize configuration
    config = AgentConfig()
    
    # Configure LLM provider
    config.set_llm_provider(llm_provider)
    if llm_model:
        config.set_llm_model(llm_model)
    
    # Configure memory settings
    config.set_memory_enabled(enable_memory)
    config.set_titans_memory(enable_titans)
    
    # Customize agent identity before creating agent
    if agent_name != config.get_agent_name():
        config.set_agent_name(agent_name)
    
    # Set custom personality
    if personality:
        config.set_personality(personality)
    
    # Create the agent with the configured identity
    agent = SingleAgent(
        use_titans_memory=enable_titans,
        llm_provider=llm_provider,
        llm_model=llm_model,
        enhanced_processing=True,
        config=config
    )
    
    return agent

def create_specialized_agents():
    """
    Create multiple specialized agents for different use cases.
    
    Returns:
        dict: Dictionary of specialized agents
    """
    agents = {}
    
    # Code Assistant Agent
    agents['code_assistant'] = create_custom_agent(
        agent_name="CodeWizard",
        personality="You are an expert software developer specializing in Python, JavaScript, and system architecture. You provide clean, well-documented code solutions and explain complex programming concepts clearly.",
        llm_provider="groq",
        llm_model="llama-3.1-8b-instant"
    )
    
    # Data Analysis Agent
    agents['data_analyst'] = create_custom_agent(
        agent_name="DataSage",
        personality="You are a data scientist and analytics expert. You help with data analysis, visualization, statistical modeling, and machine learning. You provide insights and actionable recommendations from data.",
        llm_provider="groq",
        llm_model="llama-3.1-8b-instant"
    )
    
    # Writing Assistant Agent
    agents['writer'] = create_custom_agent(
        agent_name="WordSmith",
        personality="You are a professional writer and editor. You help with content creation, editing, proofreading, and improving writing style. You provide clear, engaging, and well-structured text.",
        llm_provider="groq",
        llm_model="llama-3.1-8b-instant"
    )
    
    # Research Assistant Agent
    agents['researcher'] = create_custom_agent(
        agent_name="Scholar",
        personality="You are a research assistant with expertise in academic research, fact-checking, and information synthesis. You help gather, analyze, and present information from multiple sources.",
        llm_provider="groq",
        llm_model="llama-3.1-8b-instant",
        enable_titans=True  # Enhanced memory for research context
    )
    
    return agents

def demonstrate_custom_agent():
    """
    Demonstrate custom agent capabilities.
    """
    print("=== Custom Metis Agent Template ===")
    print()
    
    # Create a custom coding assistant
    print("Creating custom coding assistant...")
    agent = create_custom_agent(
        agent_name="PythonMentor",
        personality="You are a Python expert and mentor. You help developers learn Python best practices, debug code, and build efficient applications. You always provide working code examples.",
        llm_provider="groq",
        llm_model="llama-3.1-8b-instant"
    )
    
    # Display agent info
    identity = agent.get_agent_identity()
    print(f"Agent Name: {identity.get('name')}")
    print(f"Agent ID: {identity.get('agent_id')}")
    print(f"LLM Provider: {agent.config.get_llm_provider()}")
    print(f"Memory Enabled: {agent.config.is_memory_enabled()}")
    print()
    
    # Test the custom agent
    queries = [
        "What's your name and what do you specialize in?",
        "Can you help me write a Python function to calculate fibonacci numbers?",
        "What are some Python best practices for error handling?"
    ]
    
    print("Testing custom agent...")
    print("-" * 60)
    
    for query in queries:
        print(f"User: {query}")
        try:
            response = agent.process_query(query)
            print(f"Agent: {response}")
        except Exception as e:
            print(f"Error: {e}")
            print("Make sure you have configured your API keys!")
        print()

def demonstrate_specialized_agents():
    """
    Demonstrate multiple specialized agents.
    """
    print("=== Specialized Agents Demo ===")
    print()
    
    # Create specialized agents
    print("Creating specialized agents...")
    agents = create_specialized_agents()
    
    # Display all agents
    for role, agent in agents.items():
        identity = agent.get_agent_identity()
        print(f"{role.title()}: {identity.get('name')} ({identity.get('agent_id')})")
    print()
    
    # Test each agent with role-specific queries
    test_cases = {
        'code_assistant': "Can you help me optimize this Python code for better performance?",
        'data_analyst': "How would you approach analyzing customer churn data?",
        'writer': "Can you help me improve the clarity of this technical documentation?",
        'researcher': "What are the latest trends in artificial intelligence research?"
    }
    
    print("Testing specialized agents...")
    print("-" * 60)
    
    for role, query in test_cases.items():
        if role in agents:
            agent = agents[role]
            identity = agent.get_agent_identity()
            print(f"Testing {identity.get('name')} ({role}):")
            print(f"Query: {query}")
            try:
                response = agent.process_query(query)
                print(f"Response: {response[:200]}...")  # Truncate for demo
            except Exception as e:
                print(f"Error: {e}")
            print()

def main():
    """
    Main function demonstrating custom agent creation.
    """
    # Set up environment (you need to configure API keys)
    print("Note: Make sure to set your API keys via environment variables:")
    print("- GROQ_API_KEY")
    print("- OPENAI_API_KEY")
    print("- ANTHROPIC_API_KEY")
    print()
    
    # Demonstrate single custom agent
    demonstrate_custom_agent()
    
    print("\n" + "="*60 + "\n")
    
    # Demonstrate multiple specialized agents
    demonstrate_specialized_agents()

if __name__ == "__main__":
    main()
