#!/usr/bin/env python3
"""
Quick Start Example - Metis Agent v0.6.0

This is the simplest possible example to get you started with Metis Agent v0.6.0.
Run this after setting up your API key to verify everything works.

Features demonstrated:
- Basic agent creation and configuration
- Multi-provider LLM support (Groq, OpenAI, Anthropic)
- Environment variable loading
- Simple query processing
"""

import os
import sys
from dotenv import load_dotenv

# Add the metis_agent directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'metis_agent'))

def main():
    """Quick start example"""
    
    # Load environment variables from .env.local file
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env.local')
    if os.path.exists(env_path):
        load_dotenv(env_path)
        print(f"[ENV] Loaded environment variables from {env_path}")
    else:
        print(f"[ENV] No .env.local file found at {env_path}")
    
    print("[METIS] Agent v0.6.0 - Quick Start Example")
    print("=" * 50)
    
    # Check for API key
    api_key = os.getenv('GROQ_API_KEY') or os.getenv('OPENAI_API_KEY') or os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("[ERROR] No API key found!")
        print("\nPlease set an API key first:")
        print("  Option 1: Add to .env.local file (recommended)")
        print("    GROQ_API_KEY=your_key_here")
        print("  Option 2: Set environment variable")
        print("    set GROQ_API_KEY=your_key_here  (Windows)")
        print("    export GROQ_API_KEY=your_key_here  (macOS/Linux)")
        print("\nGet a free Groq API key at: https://console.groq.com/")
        return
    
    try:
        # Import Metis Agent
        from metis_agent import SingleAgent
        from metis_agent.core.agent_config import AgentConfig
        
        print("[OK] Metis Agent v0.6.0 imported successfully")
        
        # Create configuration with v0.6.0 enhancements
        config = AgentConfig()
        
        # Enable enhanced memory features
        config.set_memory_enabled(True)
        config.set_titans_memory(True)
        print("[OK] Enhanced memory and Titans memory enabled")
        
        # Set up LLM provider with optimal models
        if os.getenv('GROQ_API_KEY'):
            config.set_api_key('groq', os.getenv('GROQ_API_KEY'))
            config.set_llm_provider('groq')
            config.set_llm_model('llama-3.1-8b-instant')  # Fast and efficient
            print("[OK] Using Groq LLM provider (llama-3.1-8b-instant)")
        elif os.getenv('OPENAI_API_KEY'):
            config.set_api_key('openai', os.getenv('OPENAI_API_KEY'))
            config.set_llm_provider('openai')
            config.set_llm_model('gpt-4o-mini')  # Cost-effective
            print("[OK] Using OpenAI LLM provider (gpt-4o-mini)")
        elif os.getenv('ANTHROPIC_API_KEY'):
            config.set_api_key('anthropic', os.getenv('ANTHROPIC_API_KEY'))
            config.set_llm_provider('anthropic')
            config.set_llm_model('claude-3-haiku-20240307')  # Fast and efficient
            print("[OK] Using Anthropic LLM provider (claude-3-haiku)")
        
        # Create agent
        agent = SingleAgent(config=config)
        print("[OK] Agent created successfully")
        
        # Get agent identity
        identity = agent.get_agent_identity()
        agent_name = identity.get('name', 'Assistant')
        agent_id = identity.get('agent_id', 'unknown')
        print(f"[OK] Agent name: {agent_name}")
        print(f"[OK] Agent ID: {agent_id}")
        print(f"[OK] Memory enabled: {config.is_memory_enabled()}")
        print(f"[OK] Titans memory: {config.is_titans_memory_enabled()}")
        
        # Test query
        print("\n" + "=" * 50)
        print("Testing agent with a simple query...")
        
        test_query = "Hello! Can you tell me what you can help me with in v0.6.0?"
        print(f"Query: {test_query}")
        print("\nResponse:")
        print("-" * 50)
        
        response = agent.process_query(test_query)
        print(response)
        
        print("\n" + "=" * 50)
        print("[SUCCESS] Your Metis Agent v0.6.0 is working perfectly!")
        print("\n[INFO] Next steps:")
        print("1. Try the templates in the templates/ directory:")
        print("   - basic_agent_template.py - Enhanced agent with v0.6.0 features")
        print("   - custom_agent_template.py - Specialized agents and multi-agent workflows")
        print("   - custom_tools_template.py - Create your own custom tools")
        print("   - web_app_template.py - Build web applications")
        print("2. Explore v0.6.0 features:")
        print("   - E2B Code Sandbox for secure code execution")
        print("   - 36+ built-in tools for development and research")
        print("   - Enhanced memory with Titans integration")
        print("   - Multi-provider LLM support")
        print("3. Customize for your needs:")
        print("   - Create custom tools for domain-specific tasks")
        print("   - Build specialized agent personalities")
        print("   - Integrate with your existing systems")
        
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        print("\n[TROUBLESHOOTING] Common issues:")
        print("1. Make sure you have installed metis-agent: pip install metis-agent")
        print("2. Verify your API key is set correctly in .env.local or environment")
        print("3. Check your internet connection")
        print("4. Try running other templates: python basic_agent_template.py")
        print("5. Check the Custom Tools Guide for detailed setup instructions")
        print("\n[SUPPORT] For help:")
        print("- Review the templates in the templates/ directory")
        print("- Check the documentation and examples")
        print("- Ensure you're using the latest version of metis-agent")

if __name__ == "__main__":
    main()
