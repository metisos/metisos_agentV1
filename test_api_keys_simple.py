#!/usr/bin/env python3
"""
API Key Test Script - Simple Version

This script tests if your API keys are working properly.
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
        print("Google API Key: NOT FOUND")
        return False
    
    print(f"Google API Key: {api_key[:10]}...")
    
    try:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'key': api_key,
            'cx': '53433d9e4d284403e',
            'q': 'weather Boston',
            'num': 1
        }
        
        print("  Testing Google Search API...", end=" ")
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'items' in data:
                print("SUCCESS!")
                print(f"  Sample result: {data['items'][0]['title'][:50]}...")
                return True
            else:
                print("API responded but no results")
                return False
        else:
            print(f"FAILED (Status: {response.status_code})")
            return False
            
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False

def test_firecrawl_api_key():
    """Test Firecrawl API key."""
    api_key = os.getenv('FIRECRAWL_API_KEY')
    
    if not api_key or api_key == 'your_firecrawl_api_key':
        print("Firecrawl API Key: NOT FOUND")
        return False
    
    print(f"Firecrawl API Key: {api_key[:10]}...")
    
    try:
        url = "https://api.firecrawl.dev/v0/scrape"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {'url': 'https://example.com'}
        
        print("  Testing Firecrawl API...", end=" ")
        response = requests.post(url, headers=headers, json=data, timeout=15)
        
        if response.status_code in [200, 201, 202]:
            print("SUCCESS!")
            return True
        else:
            print(f"FAILED (Status: {response.status_code})")
            return False
            
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False

def test_openai_api_key():
    """Test OpenAI API key."""
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key or not api_key.startswith('sk-'):
        print("OpenAI API Key: NOT FOUND or invalid format")
        return False
    
    print(f"OpenAI API Key: {api_key[:10]}...")
    
    try:
        url = "https://api.openai.com/v1/models"
        headers = {'Authorization': f'Bearer {api_key}'}
        
        print("  Testing OpenAI API...", end=" ")
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("SUCCESS!")
            return True
        else:
            print(f"FAILED (Status: {response.status_code})")
            return False
            
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False

def main():
    print("API Key Test Results")
    print("=" * 40)
    print()
    
    print("Testing Tool APIs:")
    print("-" * 20)
    google_ok = test_google_api_key()
    print()
    firecrawl_ok = test_firecrawl_api_key()
    print()
    
    print("Testing LLM APIs:")
    print("-" * 20)
    openai_ok = test_openai_api_key()
    print()
    
    print("Summary:")
    print("-" * 20)
    print(f"Google Search: {'WORKING' if google_ok else 'FAILED'}")
    print(f"Firecrawl: {'WORKING' if firecrawl_ok else 'FAILED'}")
    print(f"OpenAI: {'WORKING' if openai_ok else 'FAILED'}")
    
    working_count = sum([google_ok, firecrawl_ok, openai_ok])
    print(f"\nTotal working APIs: {working_count}/3")

if __name__ == "__main__":
    main()
