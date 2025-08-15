#!/usr/bin/env python3
"""
Advanced Configuration - Metis Agent

Shows how to configure agents programmatically with custom settings,
memory configuration, LLM providers, and tools.
"""

import os
import io
from pathlib import Path
from contextlib import redirect_stderr, redirect_stdout

def main():
    # Load environment variables if available
    try:
        from dotenv import load_dotenv
        if Path('.env').exists():
            load_dotenv()
    except ImportError:
        pass
    
    from metis_agent import SingleAgent
    from metis_agent.memory.enhanced_memory_manager import MemoryConfig
    from metis_agent.core.agent_config import AgentConfig
    
    print("Metis Agent - Advanced Configuration")
    print("=" * 40)
    
    # 1. Create Agent Configuration
    print("\n1. Agent Configuration Setup")
    config = AgentConfig()
    
    # Configure LLM settings
    config.set_llm_provider("groq")
    config.set_llm_model("llama-3.1-8b-instant")
    
    # Configure agent identity
    config.set_agent_name("CodeMasterPro")
    print(f"   Agent Name: {config.get_agent_name()}")
    print(f"   Agent ID: {config.get_agent_id()}")
    
    # 2. Configure Memory Settings  
    print("\n2. Custom Memory Configuration")
    memory_config = MemoryConfig(
        max_context_tokens=4000,        # More context memory
        max_interactions_per_session=50, # More interactions
        summarization_threshold=15,     # When to summarize
        session_timeout_hours=48,       # 2-day sessions
        enable_cost_tracking=True,      # Track API costs
        enable_summarization=True       # Auto-summarize long conversations
    )
    print(f"   Max context: {memory_config.max_context_tokens} tokens")
    print(f"   Session length: {memory_config.max_interactions_per_session} interactions")
    
    # 3. Create Agent with Full Configuration
    print("\n3. Creating Fully Configured Agent")
    with redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()):
        agent = SingleAgent(
            config=config,                    # Full agent configuration
            use_titans_memory=True,           # Advanced memory
            enhanced_processing=True,         # Enhanced features
            memory_config=memory_config,      # Custom memory settings
            memory_path="./my_agent_memory"   # Custom memory location
        )
    
    print("   > Agent created with full configuration")
    print(f"   > Name: {config.get_agent_name()}")
    print(f"   > ID: {config.get_agent_id()}")
    print(f"   > LLM: {config.get_llm_provider()} ({config.get_llm_model()})")
    
    # Set custom personality using config
    custom_personality = """
    You are an expert Python developer and mentor specializing in:
    - Clean, readable code with best practices
    - Modern Python frameworks (Flask, FastAPI, Django)
    - Code review and optimization
    - Testing strategies and implementation
    - API design and development
    
    Your communication style is encouraging, practical, and detail-oriented.
    Always provide working examples and explain the reasoning behind recommendations.
    """
    
    config.set_personality(custom_personality)
    print("   > Custom personality configured")
    
    # Test agent identity
    response = agent.process_query("What's your name, ID, and what do you specialize in?")
    if isinstance(response, dict):
        print(f"   > Agent response: {response['response'][:120]}...")
    
    # 5. Test Advanced Features
    print("\n5. Testing Advanced Configuration")
    
    # Test memory persistence
    agent.process_query("Remember that I'm working on a Flask web application")
    
    # Test memory recall
    recall = agent.process_query("What am I working on?")
    if isinstance(recall, dict):
        print(f"   Memory test: {recall['response'][:80]}...")
    
    # Test with coding task
    coding_query = """
    Can you create a simple Flask route that handles user authentication?
    Include error handling and best practices.
    """
    
    print(f"\n6. Specialized Task Test")
    print("   Query: Create Flask auth route with best practices")
    
    coding_response = agent.process_query(coding_query)
    if isinstance(coding_response, dict):
        response_text = coding_response['response']
        print(f"   Response length: {len(response_text)} characters")
        # Show just first few lines of code if present
        if 'def ' in response_text or '@app.route' in response_text:
            print("   > Generated code with Flask route")
        else:
            print("   > Generated detailed response")
    
    # 7. Show Full Configuration Summary
    print("\n7. Configuration Summary")
    print("=" * 40)
    print(f"Agent Name: {config.get_agent_name()}")
    print(f"Agent ID: {config.get_agent_id()}")
    print(f"LLM Provider: {config.get_llm_provider()}")
    print(f"LLM Model: {config.get_llm_model()}")
    print(f"Memory Enabled: {config.is_memory_enabled()}")
    print(f"Titans Memory: {config.is_titans_memory_enabled()}")
    print(f"Max Context: {memory_config.max_context_tokens} tokens")
    print(f"Max Interactions: {memory_config.max_interactions_per_session}")
    print(f"Memory Path: ./my_agent_memory")
    
    print("\n> Advanced configuration complete!")
    print("\nYour agent is fully configured with:")
    print("- Custom name and persistent ID")
    print("- Specialized personality and expertise")
    print("- Advanced memory management")
    print("- Specific LLM provider and model")
    print("- Enhanced processing capabilities")

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("Install: pip install metis-agent python-dotenv")
    except Exception as e:
        print(f"Configuration error: {e}")
        print("\nEnsure you have GROQ_API_KEY in your environment")
        print("Get free key: https://console.groq.com/keys")