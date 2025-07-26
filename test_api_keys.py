#!/usr/bin/env python3
"""
API Key Test Script

This script tests if your API keys are working properly by making simple test requests.
Run this to verify your API keys before using them in the web app.

Usage:
    python test_api_keys.py
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env.local')
load_dotenv('.env')

def test_google_api_key():
    """Test Google Custom Search API key."""
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key or api_key == 'your_google_api_key':
        print("X Google API Key: Not found or not set")
        return False
    
    print(f"Google API Key: {api_key[:10]}...")
    
    try:
        # Test with Google Custom Search API
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'key': api_key,
            'cx': '017576662512468239146:omuauf_lfve',  # Default search engine ID
            'q': 'weather Boston',
            'num': 1
        }
        
        print("   Testing Google Custom Search API...", end=" ")
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'items' in data:
                print("✅ Working!")
                print(f"   Sample result: {data['items'][0]['title'][:50]}...")
                return True
            else:
                print("⚠️  API responded but no search results")
                return False
        else:
            print(f"❌ Failed (Status: {response.status_code})")
            if response.status_code == 403:
                print("   Error: API key may be invalid or quota exceeded")
            elif response.status_code == 400:
                print("   Error: Bad request - check search engine ID")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Timeout - API request took too long")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_firecrawl_api_key():
    """Test Firecrawl API key."""
    api_key = os.getenv('FIRECRAWL_API_KEY')
    
    if not api_key or api_key == 'your_firecrawl_api_key':
        print("❌ Firecrawl API Key: Not found or not set")
        return False
    
    print(f"🔑 Firecrawl API Key: {api_key[:10]}...")
    
    try:
        url = "https://api.firecrawl.dev/v0/scrape"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'url': 'https://example.com',
            'pageOptions': {
                'onlyMainContent': True
            }
        }
        
        print("   Testing Firecrawl scraping API...", end=" ")
        response = requests.post(url, headers=headers, json=data, timeout=15)
        
        if response.status_code in [200, 201, 202]:
            print("✅ Working!")
            result = response.json()
            if 'data' in result and 'content' in result['data']:
                content_preview = result['data']['content'][:100].replace('\n', ' ')
                print(f"   Sample content: {content_preview}...")
            return True
        else:
            print(f"❌ Failed (Status: {response.status_code})")
            if response.status_code == 401:
                print("   Error: Invalid API key")
            elif response.status_code == 429:
                print("   Error: Rate limit exceeded")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Timeout - API request took too long")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_openai_api_key():
    """Test OpenAI API key."""
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key or not api_key.startswith('sk-'):
        print("❌ OpenAI API Key: Not found or invalid format")
        return False
    
    print(f"🔑 OpenAI API Key: {api_key[:10]}...")
    
    try:
        url = "https://api.openai.com/v1/models"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        print("   Testing OpenAI API...", end=" ")
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("✅ Working!")
            data = response.json()
            model_count = len(data.get('data', []))
            print(f"   Available models: {model_count}")
            return True
        else:
            print(f"❌ Failed (Status: {response.status_code})")
            if response.status_code == 401:
                print("   Error: Invalid API key")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_groq_api_key():
    """Test Groq API key."""
    api_key = os.getenv('GROQ_API_KEY')
    
    if not api_key or not api_key.startswith('gsk_'):
        print("❌ Groq API Key: Not found or invalid format")
        return False
    
    print(f"🔑 Groq API Key: {api_key[:10]}...")
    
    try:
        url = "https://api.groq.com/openai/v1/models"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        print("   Testing Groq API...", end=" ")
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("✅ Working!")
            data = response.json()
            model_count = len(data.get('data', []))
            print(f"   Available models: {model_count}")
            return True
        else:
            print(f"❌ Failed (Status: {response.status_code})")
            if response.status_code == 401:
                print("   Error: Invalid API key")
            return False
            
    except Exception as e:
        print(f"X Error: {str(e)}")
        return False

def main():
    """Run all API key tests."""
    print("API Key Test Suite")
    print("=" * 50)
    print()
    
    # Test tool-specific API keys
    print("Testing Tool API Keys:")
    print("-" * 30)
    google_ok = test_google_api_key()
    print()
    firecrawl_ok = test_firecrawl_api_key()
    print()
    
    # Test LLM API keys
    print("Testing LLM API Keys:")
    print("-" * 30)
    openai_ok = test_openai_api_key()
    print()
    groq_ok = test_groq_api_key()
    print()
    
    # Summary
    print("Summary:")
    print("-" * 30)
    
    tool_results = {
        "Google Search": google_ok,
        "Firecrawl": firecrawl_ok
    }
    
    llm_results = {
        "OpenAI": openai_ok,
        "Groq": groq_ok
    }
    
    print("Tool APIs:")
    for name, status in tool_results.items():
        status_icon = "✅" if status else "❌"
        print(f"  {status_icon} {name}")
    
    print("\nLLM APIs:")
    for name, status in llm_results.items():
        status_icon = "✅" if status else "❌"
        print(f"  {status_icon} {name}")
    
    # Overall status
    working_tools = sum(tool_results.values())
    working_llms = sum(llm_results.values())
    
    print(f"\n🎯 Results: {working_tools}/2 tool APIs working, {working_llms}/2 LLM APIs working")
    
    if working_llms > 0:
        print("✅ Your Metis Agent should work with the available LLM APIs")
    else:
        print("❌ No working LLM APIs found - your agent may not function")
    
    if working_tools > 0:
        print(f"✅ {working_tools} tool(s) available for enhanced functionality")
    else:
        print("⚠️  No tool APIs working - basic functionality only")

if __name__ == "__main__":
    main()
