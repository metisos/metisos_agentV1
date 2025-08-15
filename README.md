# Metis Agent Framework

[![PyPI version](https://badge.fury.io/py/metis-agent.svg)](https://badge.fury.io/py/metis-agent)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](https://opensource.org/licenses/Apache-2.0)
[![Downloads](https://pepy.tech/badge/metis-agent)](https://pepy.tech/project/metis-agent)

A comprehensive, enterprise-grade framework for building intelligent AI agents with advanced security, memory management, and a rich ecosystem of tools.

**Latest Release: v0.14.0** - Security-hardened enterprise framework with 36+ tools and military-grade encryption.

## What's New in v0.14.0

### Enterprise Security (v0.13.0-0.14.0)
- **Military-Grade Encryption**: AES-256-GCM with PBKDF2 key derivation
- **Command Injection Prevention**: Whitelist-only command execution with comprehensive sanitization
- **Path Traversal Protection**: Advanced directory traversal attack prevention
- **Input Validation Framework**: Multi-layer protection against SQL injection, XSS, and template injection
- **OWASP Compliance**: Enterprise-ready security with comprehensive audit logging

### Advanced AI Capabilities
- **Smart Orchestrator**: LLM-powered intelligent tool selection and execution strategies
- **Titans Memory System**: Adaptive memory with surprise detection and token awareness
- **Multi-LLM Support**: OpenAI, Anthropic, Groq, HuggingFace, and Ollama integration
- **Blueprint Automation**: Workflow definition and execution system
- **Query Analysis**: Complexity-based routing with performance optimization

### Comprehensive Tool Ecosystem (36+ Tools)
- **E2B Code Sandbox**: Secure cloud code execution environment
- **Development Tools**: Git integration, project management, unit test generation
- **Research & Analysis**: Deep research, web scraping, data analysis
- **Content Generation**: Multi-format content creation and processing
- **Security Tools**: Vulnerability assessment and secure operations

## Installation

### Quick Install
```bash
pip install metis-agent
```




## Quick Start

### 1. Set Up API Keys
Create a `.env` file or set environment variables:
```bash
# Choose your preferred LLM provider
GROQ_API_KEY=your_groq_key_here          # Recommended: Fast and free
OPENAI_API_KEY=your_openai_key_here      # GPT models  
ANTHROPIC_API_KEY=your_anthropic_key_here # Claude models

# Optional: Additional tool APIs
GOOGLE_API_KEY=your_google_key_here      # For search functionality
E2B_API_KEY=your_e2b_key_here           # For code sandbox
FIRECRAWL_API_KEY=your_firecrawl_key_here # For web scraping
```

Get your free API keys:
- **Groq**: https://console.groq.com/keys (Fastest, free tier)
- **OpenAI**: https://platform.openai.com/api-keys  
- **Anthropic**: https://console.anthropic.com/

### 2. Basic Usage
```python
from metis_agent import SingleAgent

# Create and use agent in seconds
agent = SingleAgent()

response = agent.process_query("Hello! What can you help me with?") 
print(response)
```

### 3. Agent Configuration & Customization
```python
from metis_agent import SingleAgent
from metis_agent.core.agent_config import AgentConfig
from metis_agent.memory.enhanced_memory_manager import MemoryConfig

# Create custom agent configuration
config = AgentConfig()
config.set_agent_name("CodeExpert")  # Custom agent name
config.set_llm_provider("groq")      # Choose LLM provider
config.set_llm_model("llama-3.1-8b-instant")

# Configure memory settings
memory_config = MemoryConfig(
    max_context_tokens=4000,
    max_interactions_per_session=50,
    enable_cost_tracking=True
)

# Create specialized agent
agent = SingleAgent(
    config=config,
    memory_config=memory_config,
    use_titans_memory=True,
    enhanced_processing=True
)

# Your agent now has custom identity and advanced memory
response = agent.process_query("What's your name and what can you do?")
print(f"Agent: {response}")
```

## Core Features

### Intelligent Agent Architecture
- **Query Analysis**: LLM-powered complexity assessment and optimal routing
- **Smart Orchestration**: Multi-strategy execution (single, sequential, parallel)
- **Memory Management**: Token-aware context with intelligent summarization
- **Session Persistence**: Maintain conversations across interactions

### Comprehensive Tool Suite

#### Security & Execution
- **E2B Code Sandbox**: Secure Python execution in isolated cloud environments
- **Bash Tool**: Safe system command execution with comprehensive sanitization
- **Input Validation**: Multi-layer protection against injection attacks

#### Development Tools
- **Git Integration**: Complete workflow management (clone, commit, push, merge)
- **Code Generation**: Multi-language code creation with best practices
- **Unit Test Generator**: Automated test creation with comprehensive coverage
- **Project Management**: Full lifecycle management with validation
- **Dependency Analyzer**: Project dependency analysis and optimization

#### Research & Analysis
- **Deep Research**: Multi-source research with citation management
- **Web Scraping**: Advanced content extraction with Firecrawl integration
- **Data Analysis**: Statistical analysis and visualization capabilities
- **Text Analysis**: Sentiment analysis, readability assessment, keyword extraction

#### Content Generation
- **Content Creation**: Multi-format content generation (articles, documentation, reports)
- **Template Processing**: Dynamic template rendering and customization
- **Documentation**: Automatic documentation generation from code

### Advanced Memory System

#### Titans-Inspired Memory
```python
from metis_agent.memory.titans import TitansMemoryAdapter

# Enable Titans memory for adaptive learning
agent = SingleAgent(
    use_titans_memory=True,
    memory_config={
        "surprise_threshold": 0.7,
        "short_term_capacity": 15,
        "long_term_capacity": 1000
    }
)
```

#### Enhanced Memory Manager
```python
from metis_agent.memory import EnhancedMemoryManager, MemoryConfig

# Configure memory with token awareness
memory_config = MemoryConfig(
    max_context_tokens=4000,
    max_interactions_per_session=20,
    enable_summarization=True
)

agent = SingleAgent(memory_config=memory_config)
```

### Multi-LLM Support

```python
# OpenAI GPT models
config.set_llm_provider('openai')
config.set_llm_model('gpt-4o-mini')

# Anthropic Claude models  
config.set_llm_provider('anthropic')
config.set_llm_model('claude-3-haiku-20240307')

# Groq (fastest, free tier available)
config.set_llm_provider('groq')
config.set_llm_model('llama-3.1-8b-instant')

# Local HuggingFace models
config.set_llm_provider('huggingface_local')
config.set_llm_model('microsoft/DialoGPT-medium')

# Ollama local models
config.set_llm_provider('ollama')
config.set_llm_model('llama3.1:8b')
```

## Examples & Tutorials

Check out our comprehensive examples in the `examples/` directory:

### Example Files
- **`quick_start.py`** - Get started in seconds with a working agent
- **`configure_agnet.py`** - Full agent customization with names, memory, and LLM settings  
- **`custom_tools.py`** - Create custom tools and specialized agents

### CLI Interface
Metis Agent also includes a powerful command-line interface:

```bash
# Install and access CLI
pip install metis-agent
metis --help

# Interactive chat
metis chat

# Agent management
metis agent create "MyAgent"
metis agent list
```

See `CLI_Documentation.md` for complete command documentation.

### Running the Examples

```bash
# Clone or download the examples
cd metis_agent_public/examples

# Quick start - minimal setup
python quick_start.py

# Advanced configuration - custom agent setup  
python advanced_configuration.py

# Custom tools - build specialized agents
python custom_tools.py
```

### Basic Agent Creation
```python
from metis_agent import SingleAgent

# Create and use agent
agent = SingleAgent()
response = agent.process_query("Explain quantum computing in simple terms")
print(response)
```

### Custom Agent Configuration
```python
from metis_agent import SingleAgent
from metis_agent.core.agent_config import AgentConfig
from metis_agent.memory.enhanced_memory_manager import MemoryConfig

# Create specialized agent
config = AgentConfig()
config.set_agent_name("DataAnalyst")
config.set_llm_provider("groq")
config.set_personality("You are a data analysis expert specializing in Python and statistics.")

memory_config = MemoryConfig(
    max_context_tokens=4000,
    max_interactions_per_session=50
)

agent = SingleAgent(
    config=config,
    memory_config=memory_config,
    enhanced_processing=True
)

# Agent now has custom identity and advanced memory
response = agent.process_query("What's your name and expertise?")
print(response)
```

### Custom Tool Development
```python
from metis_agent import BaseTool, SingleAgent
from metis_agent.tools.registry import register_tool

class CalculatorTool(BaseTool):
    """Custom calculator tool"""
    
    def get_description(self) -> str:
        return "Perform mathematical calculations"
    
    def get_parameters(self) -> dict:
        return {
            "expression": {"type": "string", "required": True, "description": "Math expression"}
        }
    
    def can_handle(self, query: str) -> bool:
        math_keywords = ['calculate', 'compute', 'math', 'add', 'multiply']
        return any(keyword in query.lower() for keyword in math_keywords)
    
    def execute(self, **kwargs) -> dict:
        expression = kwargs.get('expression', '')
        try:
            result = eval(expression)  # Use safely in production
            return {
                "success": True,
                "data": {"result": result, "expression": expression},
                "message": f"Calculation: {expression} = {result}"
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

# Register and use custom tool
register_tool("calculator", CalculatorTool)
agent = SingleAgent()
response = agent.process_query("Calculate 15 * 7 + 23")
print(response)
```

## Architecture Overview

### Core Components

```
metis_agent/
├── core/                    # Core agent functionality
│   ├── agent.py            # SingleAgent main class
│   ├── smart_orchestrator.py # Intelligent tool coordination
│   ├── advanced_analyzer.py  # Query complexity analysis
│   └── response_synthesizer.py # Response generation
├── tools/                   # Tool ecosystem
│   ├── base.py             # BaseTool interface
│   ├── registry.py         # Tool discovery and loading
│   ├── core_tools/         # Essential tools
│   ├── advanced_tools/     # Specialized tools
│   └── utility_tools/      # Helper utilities
├── memory/                  # Memory management
│   ├── enhanced_memory_manager.py # Token-aware memory
│   ├── titans/             # Adaptive memory system
│   └── sqlite_store.py     # Persistent storage
├── llm/                    # Multi-LLM support
│   ├── factory.py          # Provider factory
│   └── [provider]_llm.py   # Provider implementations
├── cli/                    # Command-line interface
├── auth/                   # Secure credential management
└── utils/                  # Security and validation utilities
```

## Security Features

### Enterprise-Grade Protection
- **AES-256-GCM Encryption**: Military-grade API key storage
- **PBKDF2 Key Derivation**: 100,000+ iterations for key security
- **Command Injection Prevention**: Whitelist-only execution with comprehensive sanitization
- **Path Traversal Protection**: Advanced directory traversal attack prevention
- **Input Validation**: Multi-layer protection against injection attacks

### Security Configuration
```python
from metis_agent.utils.input_validator import validate_input
from metis_agent.utils.path_security import SecurePathValidator

# Input validation
try:
    safe_input = validate_input(user_input, "string", max_length=1000, context="general")
except ValidationError as e:
    print(f"Invalid input: {e}")

# Path security
path_validator = SecurePathValidator()
if path_validator.is_safe_path("/path/to/file"):
    # Proceed with file operation
    pass
```





### Example Test
```python
#!/usr/bin/env python3
"""
Test Metis Agent Functionality
"""
import pytest
from metis_agent import SingleAgent

def test_basic_agent_creation():
    """Test basic agent creation and configuration"""
    agent = SingleAgent()
    assert agent is not None
    
def test_query_processing():
    """Test basic query processing"""
    agent = SingleAgent()
    response = agent.process_query("Hello!")
    assert isinstance(response, str)
    assert len(response) > 0

def test_memory_system():
    """Test memory system functionality"""
    agent = SingleAgent(use_titans_memory=True)
    
    # First interaction
    response1 = agent.process_query("My name is Alice")
    
    # Second interaction - should remember
    response2 = agent.process_query("What's my name?")
    assert "alice" in response2.lower()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

## Configuration

### Environment Configuration
```bash
# .env file
GROQ_API_KEY=your_groq_key_here
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GOOGLE_API_KEY=your_google_key_here
E2B_API_KEY=your_e2b_key_here
FIRECRAWL_API_KEY=your_firecrawl_key_here
```

### Agent Configuration
```python
from metis_agent.core.agent_config import AgentConfig

config = AgentConfig()

# LLM Configuration
config.set_llm_provider('groq')
config.set_llm_model('llama-3.1-8b-instant')

# Memory Configuration
config.set_memory_enabled(True)
config.set_titans_memory(True)
config.set_max_context_length(4000)

# Session Configuration
config.set_session_timeout(3600)
config.set_auto_save(True)

# Security Configuration
config.set_secure_mode(True)
```

## Documentation


## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
```bash
# Clone repository
git clone https://github.com/metisos/metis-agent.git
cd metis-agent

# Install in development mode
pip install -e .[dev,security]

# Run tests
python -m pytest tests/ -v

# Format code
black metis_agent/
isort metis_agent/
flake8 metis_agent/
```

## License

Apache License 2.0 - see [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [GitHub Wiki](https://github.com/metisos/metis-agent/wiki)
- **Issues**: [GitHub Issues](https://github.com/metisos/metis-agent/issues)
- **Discussions**: [GitHub Discussions](https://github.com/metisos/metis-agent/discussions)
- **Email**: support@metisos.com

## Roadmap

### Upcoming Features (v0.15.0+)
- **Enhanced Security**: Advanced threat detection and prevention
- **Multi-Agent Orchestration**: Coordinate multiple specialized agents
- **Plugin Ecosystem**: Marketplace for community tools and extensions
- **GUI Interface**: Desktop and web-based management interfaces
- **Enterprise Features**: RBAC, audit trails, compliance reporting
- **Performance Optimization**: Faster execution and reduced memory usage

---

**Metis Agents v0.14.0** - Building the future of AI agent development with security, intelligence, and enterprise-grade reliability.