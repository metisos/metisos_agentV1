#!/usr/bin/env python3
"""
Quick Start Example - Metis Agent

This is the simplest possible example to get you started with Metis Agent.
Run this after setting up your API key to verify everything works.
"""

import os
import sys

# Add the parent directory to the path so we can import from templates
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def main():
    """Quick start example"""
    
    print("Metis Agent - Quick Start Example")
    print("=" * 40)
    
    # Check for API key
    api_key = os.getenv('GROQ_API_KEY') or os.getenv('OPENAI_API_KEY') or os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("[ERROR] No API key found!")
        print("\nPlease set an API key first:")
        print("  set GROQ_API_KEY=your_key_here  (Windows)")
        print("  export GROQ_API_KEY=your_key_here  (macOS/Linux)")
        print("\nGet a free Groq API key at: https://console.groq.com/")
        return
    
    try:
        # Import Metis Agent
        from metis_agent.core.agent import SingleAgent
        from metis_agent.core.agent_config import AgentConfig
        
        print("[OK] Metis Agent imported successfully")
        
        # Create configuration
        config = AgentConfig()
        
        # Set up LLM provider
        if os.getenv('GROQ_API_KEY'):
            config.set_api_key('groq', os.getenv('GROQ_API_KEY'))
            config.set_llm_provider('groq')
            print("[OK] Using Groq LLM provider")
        elif os.getenv('OPENAI_API_KEY'):
            config.set_api_key('openai', os.getenv('OPENAI_API_KEY'))
            config.set_llm_provider('openai')
            print("[OK] Using OpenAI LLM provider")
        elif os.getenv('ANTHROPIC_API_KEY'):
            config.set_api_key('anthropic', os.getenv('ANTHROPIC_API_KEY'))
            config.set_llm_provider('anthropic')
            print("[OK] Using Anthropic LLM provider")
        
        # Create agent
        agent = SingleAgent(config=config)
        print("[OK] Agent created successfully")
        
        # Get agent identity
        identity = agent.get_agent_identity()
        agent_name = identity.get('name', 'Assistant')
        print(f"[OK] Agent name: {agent_name}")
        
        # Test query
        print("\n" + "=" * 40)
        print("Testing agent with a simple query...")
        
        test_query = "Hello! Can you tell me what you can help me with?"
        print(f"Query: {test_query}")
        print("\nResponse:")
        print("-" * 40)
        
        response = agent.query(test_query)
        print(response)
        
        print("\n" + "=" * 40)
        print("[SUCCESS] Your Metis Agent is working perfectly!")
        print("\nNext steps:")
        print("1. Try the templates in the templates/ directory")
        print("2. Customize agents with different personalities")
        print("3. Create custom tools for your specific needs")
        print("4. Build web applications with the web template")
        
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        print("\nTroubleshooting:")
        print("1. Make sure you have installed metis-agent: pip install metis-agent")
        print("2. Verify your API key is set correctly")
        print("3. Check your internet connection")
        print("4. Try running: python verify_setup.py")

if __name__ == "__main__":
    main()
