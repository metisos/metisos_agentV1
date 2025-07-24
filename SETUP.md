# Metis Agent Setup Guide

This guide will help you get started with Metis Agent templates in just a few minutes.

## Quick Setup (5 minutes)

### Step 1: Install Python
Make sure you have Python 3.8 or higher:
```bash
python --version
```

### Step 2: Install Metis Agent
```bash
pip install metis-agent
```

### Step 3: Get API Key
Choose one provider and get a free API key:

#### Option A: Groq (Recommended - Fast & Free)
1. Go to [console.groq.com](https://console.groq.com/)
2. Sign up for a free account
3. Create an API key
4. Set environment variable:
   ```bash
   # Windows
   set GROQ_API_KEY=your_api_key_here
   
   # macOS/Linux
   export GROQ_API_KEY=your_api_key_here
   ```

#### Option B: OpenAI
1. Go to [platform.openai.com](https://platform.openai.com/api-keys)
2. Create an API key
3. Set environment variable:
   ```bash
   # Windows
   set OPENAI_API_KEY=your_api_key_here
   
   # macOS/Linux
   export OPENAI_API_KEY=your_api_key_here
   ```

### Step 4: Test Your Setup
```bash
python templates/basic_agent_template.py
```

If you see agent responses, you're ready to go!

## Detailed Setup

### Prerequisites
- Python 3.8+
- pip package manager
- Internet connection
- API key from supported provider

### Installation Options

#### Option 1: Minimal Installation
```bash
pip install metis-agent
```

#### Option 2: Full Installation (with all dependencies)
```bash
pip install -r requirements.txt
```

#### Option 3: Development Installation
```bash
git clone https://github.com/metisos/metisos_agentV1
cd metisos_agentV1
pip install -e .
```

### Environment Variables

Create a `.env` file in your project root:
```env
# Choose one or more providers
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Optional: Custom configuration
METIS_CONFIG_DIR=/path/to/config
METIS_LOG_LEVEL=INFO
```

### Verification

Run this test script to verify your setup:

```python
#!/usr/bin/env python3
"""Setup verification script"""

import os
import sys

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"[OK] Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"[ERROR] Python {version.major}.{version.minor}.{version.micro} - Need 3.8+")
        return False

def check_metis_agent():
    """Check Metis Agent installation"""
    try:
        import metis_agent
        print("[OK] Metis Agent - Installed")
        return True
    except ImportError:
        print("[ERROR] Metis Agent - Not installed")
        print("   Run: pip install metis-agent")
        return False

def check_api_keys():
    """Check API key configuration"""
    providers = {
        'GROQ_API_KEY': 'Groq',
        'OPENAI_API_KEY': 'OpenAI', 
        'ANTHROPIC_API_KEY': 'Anthropic'
    }
    
    found_keys = []
    for key, name in providers.items():
        if os.getenv(key):
            print(f"[OK] {name} API Key - Found")
            found_keys.append(name)
        else:
            print(f"[WARNING] {name} API Key - Not found")
    
    if found_keys:
        print(f"[OK] Ready to use: {', '.join(found_keys)}")
        return True
    else:
        print("[ERROR] No API keys found - Set at least one")
        return False

def main():
    """Main verification"""
    print("Metis Agent Setup Verification")
    print("=" * 40)
    
    checks = [
        check_python_version(),
        check_metis_agent(),
        check_api_keys()
    ]
    
    if all(checks):
        print("\n[SUCCESS] Setup complete! Ready to run templates.")
        print("Try: python templates/basic_agent_template.py")
    else:
        print("\n[ERROR] Setup incomplete. Please fix the issues above.")

if __name__ == "__main__":
    main()
```

Save this as `verify_setup.py` and run:
```bash
python verify_setup.py
```

## Template-Specific Setup

### Basic Agent Template
No additional setup required.

### Custom Agent Template
No additional setup required.

### Web App Template
Install Flask:
```bash
pip install flask flask-cors
```

### Advanced Integration Template
Install additional dependencies:
```bash
pip install pandas numpy psutil
```

### Custom Tools Template
Install requests for API tools:
```bash
pip install requests
```

## Configuration

### Agent Configuration
Agents use configuration files stored in `~/.metis_agent/config.json`:

```json
{
  "llm_provider": "groq",
  "llm_model": "llama-3.1-70b-versatile",
  "memory_enabled": true,
  "titans_memory": true,
  "session_timeout": 3600,
  "max_context_length": 4000,
  "auto_save": true
}
```

### Custom Configuration
```python
from metis_agent.core.agent_config import AgentConfig

config = AgentConfig()
config.set_llm_provider('groq')
config.set_llm_model('llama-3.1-70b-versatile')
config.set_memory_enabled(True)
```

## Troubleshooting

### Common Issues

#### "ModuleNotFoundError: No module named 'metis_agent'"
**Solution**: Install the package
```bash
pip install metis-agent
```

#### "API key not found" or "Authentication failed"
**Solution**: Check your environment variables
```bash
# Check if set (Windows)
echo %GROQ_API_KEY%

# Check if set (macOS/Linux)
echo $GROQ_API_KEY

# Set if missing
set GROQ_API_KEY=your_key_here  # Windows
export GROQ_API_KEY=your_key_here  # macOS/Linux
```

#### "Connection timeout" or "Network error"
**Solution**: Check internet connection and API service status
- Verify internet connectivity
- Check provider status pages
- Try a different provider

#### Templates not working
**Solution**: Verify file paths and permissions
```bash
# Check if templates exist
ls templates/

# Check if executable
python templates/basic_agent_template.py
```

#### Import errors in templates
**Solution**: Check Python path and dependencies
```bash
# Install missing dependencies
pip install -r requirements.txt

# Check Python path
python -c "import sys; print(sys.path)"
```

### Advanced Troubleshooting

#### Debug Mode
Enable debug logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### Configuration Issues
Reset configuration:
```python
from metis_agent.core.agent_config import AgentConfig
config = AgentConfig()
config.reset_to_defaults()
```

#### Memory Issues
Clear agent memory:
```bash
# Remove memory files
rm -rf ~/.metis_agent/memory/
```

## Getting Help

### Documentation
- Check template comments for implementation details
- Review `CUSTOM_TOOLS_GUIDE.md` for tool development
- Read the main `README.md` for overview

### Community
- Report issues on GitHub
- Join community discussions
- Share your templates and tools

### Support Channels
- GitHub Issues for bugs
- Discussions for questions
- Documentation for guides

## Next Steps

Once setup is complete:

1. **Start Simple**: Run `basic_agent_template.py`
2. **Explore Features**: Try `custom_agent_template.py`
3. **Build Tools**: Study `custom_tools_template.py`
4. **Create Apps**: Deploy `web_app_template.py`
5. **Go Advanced**: Implement `advanced_integration_template.py`

Happy coding!
