#!/usr/bin/env python3
"""
Basic Metis Agent Template - v0.6.0

This template demonstrates the core features of Metis Agent v0.6.0, including:
- Basic agent creation and configuration
- LLM provider setup (OpenAI, Groq, Anthropic, HuggingFace)
- E2B Code Sandbox integration for secure code execution
- Enhanced memory management with Titans memory
- Tool usage examples

Perfect for:
- Simple chatbot applications
- Basic AI assistance
- Learning Metis Agent fundamentals
- Quick prototyping

Usage:
    python basic_agent_template.py

Prerequisites:
    - pip install metis-agent
    - Set API keys via environment variables or in the script
"""

from metis_agent import SingleAgent
from metis_agent.core.agent_config import AgentConfig
from metis_agent.auth.api_key_manager import APIKeyManager
import os
import sys
from dotenv import load_dotenv

def create_basic_agent(use_titans_memory=True, llm_provider="groq"):
    """
    Create a basic Metis Agent with v0.6.0 features.
    
    Args:
        use_titans_memory (bool): Enable Titans memory for enhanced context management
        llm_provider (str): LLM provider to use (groq, openai, anthropic, huggingface)
    
    Returns:
        SingleAgent: Configured agent instance with v0.6.0 capabilities
    """
    print(f"Creating agent with {llm_provider} provider and Titans memory: {use_titans_memory}")
    
    # Initialize agent configuration
    config = AgentConfig()
    
    # Configure LLM provider
    if llm_provider == "groq":
        config.set_llm_provider("groq")
        config.set_llm_model("llama-3.1-8b-instant")  # Fast and free
    elif llm_provider == "openai":
        config.set_llm_provider("openai")
        config.set_llm_model("gpt-4o-mini")  # Cost-effective
    elif llm_provider == "anthropic":
        config.set_llm_provider("anthropic")
        config.set_llm_model("claude-3-haiku-20240307")  # Fast and efficient
    
    # Enable enhanced memory management
    config.set_memory_enabled(True)
    config.set_titans_memory(use_titans_memory)
    
    # Create the agent with enhanced capabilities
    agent = SingleAgent(
        config=config,
        use_titans_memory=use_titans_memory
    )
    
    return agent

def setup_api_keys():
    """
    Setup API keys for LLM providers and advanced tools.
    
    Supports multiple methods:
    1. Environment variables (recommended for security)
    2. APIKeyManager for programmatic setup
    3. Direct configuration
    
    Required environment variables:
    - GROQ_API_KEY (recommended - fast and free)
    - OPENAI_API_KEY (for OpenAI models)
    - ANTHROPIC_API_KEY (for Claude models)
    - E2B_API_KEY (for secure code execution)
    - FIRECRAWL_API_KEY (for web scraping)
    """
    print("Setting up API keys for v0.6.0...")
    
    # Check for required environment variables
    required_keys = {
        'GROQ_API_KEY': 'Groq (recommended - fast and free)',
        'OPENAI_API_KEY': 'OpenAI (GPT models)',
        'ANTHROPIC_API_KEY': 'Anthropic (Claude models)',
        'E2B_API_KEY': 'E2B Code Sandbox (secure code execution)',
    }
    
    optional_keys = {
        'FIRECRAWL_API_KEY': 'Firecrawl (advanced web scraping)',
        'GOOGLE_API_KEY': 'Google Search API',
    }
    
    print("\nChecking API key configuration:")
    print("=" * 40)
    
    # Check required keys
    missing_required = []
    for key, description in required_keys.items():
        if os.getenv(key):
            print(f"[OK] {key}: Configured ({description})")
        else:
            print(f"[MISSING] {key}: Missing ({description})")
            missing_required.append(key)
    
    # Check optional keys
    print("\nOptional API keys:")
    for key, description in optional_keys.items():
        if os.getenv(key):
            print(f"[OK] {key}: Configured ({description})")
        else:
            print(f"[NOT SET] {key}: Not set ({description})")
    
    if missing_required:
        print(f"\n[WARNING] Warning: {len(missing_required)} required API key(s) missing!")
        print("\nTo set API keys, use one of these methods:")
        print("\n1. Environment variables (recommended):")
        for key in missing_required:
            print(f"   export {key}='your_api_key_here'")
        
        print("\n2. Using APIKeyManager:")
        print("   from metis_agent.auth.api_key_manager import APIKeyManager")
        print("   key_manager = APIKeyManager()")
        for key in missing_required:
            service = key.replace('_API_KEY', '').lower()
            print(f"   key_manager.set_key('{service}', 'your_api_key_here')")
        
        print("\n3. CLI command:")
        for key in missing_required:
            service = key.replace('_API_KEY', '').lower()
            print(f"   metis auth set-key {service} your_api_key_here")
    else:
        print("\n[OK] All required API keys are configured!")
    
    print("=" * 40)

def demonstrate_v6_features(agent):
    """
    Demonstrate key v0.6.0 features including E2B code execution,
    advanced tools, and enhanced memory management.
    """
    print("\n[DEMO] Demonstrating Metis Agent v0.6.0 Features")
    print("=" * 50)
    
    # Feature 1: E2B Code Sandbox (secure code execution)
    print("\n1. [E2B] Code Sandbox - Secure Code Execution")
    print("-" * 30)
    code_query = """
Execute this Python code securely:
```python
import pandas as pd
import numpy as np

# Create sample data
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'salary': [50000, 60000, 70000, 55000]
}

df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
print(f"\nAverage salary: ${df['salary'].mean():,.2f}")
print(f"Age range: {df['age'].min()} - {df['age'].max()}")
```
"""
    
    try:
        print(f"User: {code_query[:100]}...")
        response = agent.process_query(code_query)
        print(f"Agent: {response[:500]}..." if len(response) > 500 else f"Agent: {response}")
    except Exception as e:
        print(f"Error: {e}")
        print("Note: E2B requires API key configuration")
    
    # Feature 2: Advanced Research
    print("\n\n2. [RESEARCH] Advanced Research Capabilities")
    print("-" * 30)
    research_query = "Research the latest developments in quantum computing and provide a summary with key points"
    
    try:
        print(f"User: {research_query}")
        response = agent.process_query(research_query)
        print(f"Agent: {response[:500]}..." if len(response) > 500 else f"Agent: {response}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Feature 3: Code Generation with Best Practices
    print("\n\n3. [CODE] Advanced Code Generation")
    print("-" * 30)
    code_gen_query = "Generate a Python class for a simple task manager with methods to add, remove, and list tasks. Include type hints and docstrings."
    
    try:
        print(f"User: {code_gen_query}")
        response = agent.process_query(code_gen_query)
        print(f"Agent: {response[:500]}..." if len(response) > 500 else f"Agent: {response}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Feature 4: Memory and Context
    print("\n\n4. [MEMORY] Enhanced Memory Management")
    print("-" * 30)
    
    # First query to establish context
    context_query1 = "I'm working on a machine learning project about image classification"
    try:
        print(f"User: {context_query1}")
        response = agent.process_query(context_query1, session_id="demo_session")
        print(f"Agent: {response[:300]}..." if len(response) > 300 else f"Agent: {response}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Follow-up query using context
    context_query2 = "What are the best practices for data preprocessing in this context?"
    try:
        print(f"\nUser: {context_query2}")
        response = agent.process_query(context_query2, session_id="demo_session")
        print(f"Agent: {response[:300]}..." if len(response) > 300 else f"Agent: {response}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 50)

def main():
    """
    Main function demonstrating Metis Agent v0.6.0 capabilities.
    """
    # Load environment variables from .env.local file
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env.local')
    if os.path.exists(env_path):
        load_dotenv(env_path)
        print(f"[ENV] Loaded environment variables from {env_path}")
    else:
        print(f"[ENV] No .env.local file found at {env_path}")
    
    print("[METIS] Agent v0.6.0 - Basic Template")
    print("Enterprise-Grade AI Agent Framework")
    print("=" * 50)
    
    # Setup and check API keys
    setup_api_keys()
    
    # Check if we have at least one LLM provider configured
    llm_providers = ['GROQ_API_KEY', 'OPENAI_API_KEY', 'ANTHROPIC_API_KEY']
    configured_provider = None
    
    for provider_key in llm_providers:
        if os.getenv(provider_key):
            configured_provider = provider_key.replace('_API_KEY', '').lower()
            break
    
    if not configured_provider:
        print("\n[ERROR] No LLM provider configured! Please set at least one API key.")
        print("\nQuick setup:")
        print("export GROQ_API_KEY='your_groq_api_key_here'  # Recommended - fast and free")
        print("\nGet your Groq API key at: https://console.groq.com/keys")
        sys.exit(1)
    
    print(f"\n[OK] Using {configured_provider.upper()} as LLM provider")
    
    # Create the agent with v0.6.0 features
    print("\n[AGENT] Creating enhanced agent...")
    try:
        agent = create_basic_agent(use_titans_memory=True, llm_provider=configured_provider)
        
        # Get agent identity information
        identity = agent.get_agent_identity()
        print(f"\n[OK] Agent created successfully!")
        print(f"Agent Name: {identity.get('agent_name', 'Unknown')}")
        print(f"Agent ID: {identity.get('agent_id', 'Unknown')}")
        
        # Basic conversation examples
        print("\n[CHAT] Basic Conversation Examples")
        print("-" * 30)
        
        basic_queries = [
            "Hello! What's your name and what can you help me with?",
            "What are the key features of Metis Agent v0.6.0?",
            "How many tools do you have access to?",
        ]
        
        for query in basic_queries:
            print(f"\nUser: {query}")
            try:
                response = agent.process_query(query)
                print(f"Agent: {response[:400]}..." if len(response) > 400 else f"Agent: {response}")
            except Exception as e:
                print(f"Error: {e}")
        
        # Demonstrate advanced features
        demonstrate_v6_features(agent)
        
        # Memory insights (if Titans memory is enabled)
        try:
            insights = agent.get_memory_insights()
            if insights:
                print("\n[MEMORY] Memory Insights:")
                print(f"Total memories: {insights.get('total_memories', 'N/A')}")
                print(f"Memory usage: {insights.get('memory_usage', 'N/A')}")
        except Exception as e:
            print(f"\nMemory insights not available: {e}")
        
        print("\n[COMPLETE] Template demonstration complete!")
        print("\n[INFO] Next steps:")
        print("- Explore other templates in the templates/ directory")
        print("- Check out the Metis Starter repository for more examples")
        print("- Visit the documentation for advanced usage patterns")
        
    except Exception as e:
        print(f"\n[ERROR] Error creating agent: {e}")
        print("\nTroubleshooting:")
        print("1. Verify your API keys are correctly set")
        print("2. Check your internet connection")
        print("3. Ensure metis-agent is properly installed: pip install --upgrade metis-agent")
        sys.exit(1)

if __name__ == "__main__":
    main()
