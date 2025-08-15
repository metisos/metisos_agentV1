#!/usr/bin/env python3
"""
Quick Start - Metis Agent

Get up and running with Metis Agent in seconds.
"""

import os
import sys
import io
from pathlib import Path
from contextlib import redirect_stderr, redirect_stdout

def main():
    # Load environment variables if .env file exists
    try:
        from dotenv import load_dotenv
        if Path('.env').exists():
            load_dotenv()
    except ImportError:
        pass
    
    # Import and create agent
    from metis_agent import SingleAgent
    
    # Create agent (suppress initialization output)
    with redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()):
        agent = SingleAgent()
    
    print("Metis Agent - Ready!")
    print("=" * 25)
    
    # Ask the agent something
    query = "Hello! What can you help me with?"
    print(f"You: {query}")
    print()
    
    response = agent.process_query(query)
    print("Agent:", response['response'] if isinstance(response, dict) else response)

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("Install Metis Agent: pip install metis-agent")
    except Exception as e:
        print("Need API key in .env file:")
        print("GROQ_API_KEY=your_key_here")
        print("Get free key at: https://console.groq.com/keys")