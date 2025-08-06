# Metis Agents

[![PyPI version](https://badge.fury.io/py/metis-agent.svg)](https://badge.fury.io/py/metis-agent)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](https://opensource.org/licenses/Apache-2.0)
[![Downloads](https://pepy.tech/badge/metis-agent)](https://pepy.tech/project/metis-agent)

A powerful, modular framework for building AI agents with intelligent memory management and minimal boilerplate code. Metis Agent provides a comprehensive toolkit for creating intelligent agents that can understand user queries, plan and execute complex tasks, and maintain persistent conversations.

**Latest Release: v0.6.0** - Major expansion with secure code execution, advanced tools, and enterprise-grade capabilities.

### What's New in v0.6.0
- ** E2B Code Sandbox** - Secure Python code execution in isolated cloud environments
- ** 36+ Advanced Tools** - Comprehensive toolkit for development, research, and analysis
- ** Smart Orchestrator** - Intelligent tool selection with parameter extraction
- ** Enhanced Analytics** - Advanced memory management with Titans-inspired system
- ** Enterprise Ready** - MCP integration, blueprint system, and production APIs
- ** Performance Optimized** - Improved query analysis and execution strategies
- ** Developer Focused** - Git integration, project management, and automated workflows

## Features

###  **Core Architecture**
- **Smart Orchestrator**: Intelligent tool selection with parameter extraction and execution strategies
- **Enhanced Memory System**: Titans-inspired adaptive memory with token-aware context management
- **Query Analyzer**: LLM-powered complexity analysis for optimal tool routing
- **Session Management**: Persistent conversations with automatic context preservation

###  **LLM Integration**
- **Multiple Providers**: OpenAI, Groq, Anthropic, HuggingFace (API & Local), Ollama with seamless switching
- **Local Model Support**: Run HuggingFace models locally with transformers library (no API keys required)
- **Model Flexibility**: Support for GPT-4, Claude, Llama, Mixtral, GPT-2, DialoGPT, and custom models
- **Device Optimization**: Automatic device selection (CUDA, MPS, CPU) with quantization support
- **Secure Authentication**: Encrypted API key management with environment fallback

###  **Advanced Tool Suite (36+ Tools)**

#### ** Security & Execution**
- **E2B Code Sandbox**: Secure Python execution in isolated cloud environments
- **Bash Tool**: Safe system command execution with output capture

#### ** Development Tools**
- **Git Integration**: Complete workflow management (clone, commit, push, merge, etc.)
- **Code Generation**: Multi-language code creation with best practices
- **Unit Test Generator**: Automated test creation with comprehensive coverage
- **Dependency Analyzer**: Project dependency analysis and optimization
- **Project Management**: Full lifecycle management with validation

#### ** Research & Analysis**
- **Deep Research**: Multi-source research with citation management
- **Data Analysis**: Advanced analytics with pandas, numpy, visualization
- **Web Scraper**: Intelligent content extraction with Firecrawl integration
- **Google Search**: Real-time web search with result processing

#### ** Content & Communication**
- **Content Generation**: Multi-format content creation (blogs, docs, emails)
- **Text Analyzer**: Advanced NLP analysis with sentiment and entity recognition
- **Blueprint Execution**: Automated workflow and process execution

#### ** File & System Operations**
- **File Manager**: Complete file system operations with safety checks
- **Read/Write Tools**: Intelligent file handling with format detection
- **Grep Tool**: Advanced search with regex and pattern matching

###  **Enterprise Features**
- **MCP Integration**: Model Context Protocol server support
- **Blueprint System**: Workflow automation and process management
- **CLI Interface**: Comprehensive command-line tools for all operations
- **Web API**: RESTful endpoints for integration and automation
- **Memory Analytics**: Real-time performance monitoring and insights
- **Tool Registry**: Dynamic tool discovery and registration system

## Installation

```bash
pip install metis-agent
```

## Starter Templates

Get started quickly with our comprehensive collection of templates and examples:

**[Metis Agent Starter Templates](https://github.com/metis-analytics/metis-starter)** - A complete collection of templates for different use cases:

- **Basic Agent Template** - Simple agent for beginners and quick prototypes
- **Custom Agent Template** - Specialized agents with custom personalities
- **Web App Template** - Flask-based web chat interface
- **Advanced Integration Template** - Enterprise multi-agent systems
- **Custom Tools Template** - Examples for extending agent capabilities
- **Simple Custom Tool Example** - Step-by-step tool development guide

```bash
# Clone the starter templates
git clone https://github.com/metis-analytics/metis-starter.git
cd metis-starter

# Run your first agent
python templates/basic_agent_template.py
```

Each template includes:
- Complete working examples
- Detailed documentation
- Setup instructions
- Customization guides
- Best practices

## Quick Start

### Basic Usage

```python
from metis_agent import SingleAgent

# Create an agent
agent = SingleAgent()

# Process a query
response = agent.process_query("Write a Python function to calculate Fibonacci numbers")
print(response)
```

### Using Different LLM Providers

```python
from metis_agent import SingleAgent, configure_llm

# Configure cloud-based LLM (OpenAI, Groq, Anthropic)
configure_llm("groq", "llama-3.1-8b-instant", "your-api-key")

# Configure local HuggingFace model (no API key required)
configure_llm("huggingface", "gpt2")

# Configure Ollama local model (no API key required)
configure_llm("ollama", "tinydolphin")

# Create an agent
agent = SingleAgent()

# Process a query
response = agent.process_query("Explain quantum computing in simple terms")
print(response)
```

### Secure Code Execution with E2B

```python
from metis_agent import SingleAgent

# Create an agent (E2B tool auto-detected)
agent = SingleAgent()

# Execute Python code securely in cloud sandbox
response = agent.process_query("""
Execute this Python code:
```python
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]}
df = pd.DataFrame(data)

# Create visualization
plt.figure(figsize=(8, 6))
plt.plot(df['x'], df['y'], marker='o')
plt.title('Sample Data Visualization')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()

print(f"Data shape: {df.shape}")
print(df.describe())
```
""")

print(response)
```

### Creating Custom Tools

```python
from metis_agent import SingleAgent, BaseTool, register_tool

class MyCustomTool(BaseTool):
    name = "custom_tool"
    description = "A custom tool for specialized tasks"
    
    def can_handle(self, task):
        return "custom task" in task.lower()
        
    def execute(self, task):
        return f"Executed custom tool on: {task}"

# Register the tool
register_tool("custom_tool", MyCustomTool)

# Create an agent
agent = SingleAgent()

# Process a query
response = agent.process_query("Perform a custom task")
print(response)
```

### Using Titans Memory

```python
from metis_agent import SingleAgent

# Create an agent with Titans memory
agent = SingleAgent(use_titans_memory=True)

# Process queries with memory
result1 = agent.process_query("What is machine learning?", session_id="user123")
result2 = agent.process_query("How does it relate to AI?", session_id="user123")
```

## Command Line Interface

Metis Agent provides a comprehensive command-line interface for all operations:

### Core Commands

```bash
# Interactive chat mode
metis chat

# Single query with chat
metis chat "Write a Python function to calculate Fibonacci numbers"

# Code generation for specific tasks
metis code "Write a Python function to calculate Fibonacci numbers"

# Chat with session context
metis chat "What did we discuss earlier?" --session user123
```

### Basic Usage

```bash
# Interactive chat for debugging
metis chat "Help me debug this code"

# Code generation for specific tasks
metis code "Create a debugging function for Python"

# Interactive code session
metis code --interactive
```

### API Key Management

```bash
# Set API keys for different providers
metis auth set openai sk-your-openai-key
metis auth set groq gsk_your-groq-key
metis auth set anthropic your-anthropic-key
metis auth set e2b your-e2b-api-key

# List configured API keys (shows providers only, not keys)
metis auth list

# Remove an API key
metis auth remove openai

# Test API key connectivity
metis auth test openai
```

### Local Model Setup

#### HuggingFace Local Models

```bash
# Install required dependencies
pip install transformers torch

# Configure for local HuggingFace models
metis config set llm_provider huggingface
metis config set llm_model gpt2

# Configure device preference
metis config hf-device auto    # auto-detect best device
metis config hf-device cpu     # force CPU
metis config hf-device cuda    # force CUDA (if available)
metis config hf-device mps     # force MPS (macOS)

# Configure quantization for memory efficiency
metis config hf-quantization none   # no quantization
metis config hf-quantization 8bit   # 8-bit quantization
metis config hf-quantization 4bit   # 4-bit quantization

# Set maximum sequence length
metis config hf-max-length 512
metis config hf-max-length 1024

# View available model recommendations
metis config list-models
```

#### Ollama Local Models

```bash
# Install Ollama from https://ollama.ai
# Pull a model
ollama pull tinydolphin

# Configure Metis to use Ollama
metis config set llm_provider ollama
metis config set llm_model tinydolphin

# Set custom Ollama server URL (if needed)
metis config ollama-url http://localhost:11434

# List available Ollama models
metis config list-models
```

#### Local Model Advantages

**Privacy & Security:**
- No data sent to external APIs
- Complete control over your conversations
- Offline operation capability

**Cost Efficiency:**
- No API usage fees
- One-time setup cost only
- Unlimited usage

**Customization:**
- Fine-tune models for specific domains
- Control generation parameters
- Optimize for your hardware

**Performance:**
- No network latency
- Consistent response times
- Hardware-optimized inference

### E2B Code Sandbox Setup

```bash
# Set E2B API key for secure code execution
metis auth set e2b your-e2b-api-key

# Test E2B connectivity
metis auth test e2b

# Execute code in sandbox via CLI
metis chat "Execute this Python code: print('Hello from E2B sandbox!')"
```

### Code Generation

```bash
# Generate code using natural language
metis code "Write a hello world function in Python"

# Interactive code generation
metis code --interactive

# Generate code with specific requirements
metis code "Create a REST API with FastAPI and authentication"
```

### Interactive Chat

```bash
# Start interactive chat session
metis chat

# Single query with session context
metis chat "What is machine learning?" --session user123

# Ask follow-up questions in the same session
metis chat "Can you explain neural networks?" --session user123
```

### Configuration Management

```bash
# Show current configuration
metis config show

# Set LLM provider
metis config set llm_provider openai
metis config set llm_provider groq
metis config set llm_provider anthropic
metis config set llm_provider huggingface  # for local models
metis config set llm_provider ollama       # for Ollama models

# Set specific model (optional)
metis config set llm_model gpt-4o
metis config set llm_model llama-3.1-8b-instant
metis config set llm_model claude-3-opus-20240229
metis config set llm_model gpt2                    # HuggingFace local
metis config set llm_model microsoft/DialoGPT-small # HuggingFace local
metis config set llm_model tinydolphin              # Ollama local

# Configure memory settings
metis config set memory_enabled true
metis config set titans_memory true

# Set session and context limits
metis config set session_timeout 3600
metis config set max_context_length 4000

# Reset configuration to defaults
metis config reset

# Local model configuration
# HuggingFace specific settings
metis config hf-device auto|cpu|cuda|mps
metis config hf-quantization none|8bit|4bit
metis config hf-max-length 512

# Ollama specific settings
metis config ollama-url http://localhost:11434

# List available models for current provider
metis config list-models
```

### Agent Identity Management

```bash
# Show agent identity
metis config identity

# Set agent name
metis config set-name "MyAgent"

# Set agent personality (interactive - type 'END' when finished)
metis config set-personality --interactive

# Set agent personality from file
metis config set-personality --file personality.txt

# Set system message (base or custom layer - type 'END' when finished)
metis config system-message --interactive --layer custom
metis config system-message --file system.txt --layer base

# Regenerate agent identity
metis config regenerate-identity
```





## Python API Usage

Metis Agent can be used directly in Python applications:

```python
from metis_agent import SingleAgent

# Initialize agent
agent = SingleAgent()

# Process a query
response = agent.process_query("Write a Python function to calculate Fibonacci numbers")
print(response)
```

For web applications, you can integrate the agent into your existing Flask/FastAPI server.

## Detailed Documentation

### Core Components

#### SingleAgent

The main agent class that orchestrates all components:

```python
from metis_agent import SingleAgent

agent = SingleAgent(
    use_titans_memory=False,  # Enable/disable Titans memory
    tools=None,               # Custom tools (uses all available if None)
    llm_provider="openai",    # LLM provider
    llm_model=None,           # LLM model (uses default if None)
    memory_path=None,         # Path to memory database
    task_file=None            # Path to task file
)
```

#### Intent Router

Determines whether a user query is a question or a task:

```python
from metis_agent.core.intent_router import IntentRouter

router = IntentRouter()
intent = router.classify("What is the capital of France?")  # Returns "question"
intent = router.classify("Create a Python script to sort a list")  # Returns "task"
```

#### Task Manager

Manages tasks and their status:

```python
from metis_agent.core.task_manager import TaskManager

task_manager = TaskManager()
task_manager.add_task("Write a function to calculate Fibonacci numbers")
task_manager.mark_complete("Write a function to calculate Fibonacci numbers")
tasks = task_manager.get_all_tasks()
```

#### Memory Systems

SQLite-based memory:

```python
from metis_agent.memory.sqlite_store import SQLiteMemory

memory = SQLiteMemory("memory.db")
memory.store_input("user123", "What is machine learning?")
memory.store_output("user123", "Machine learning is...")
context = memory.get_context("user123")
```

Titans-inspired adaptive memory:

```python
from metis_agent.memory.titans.titans_memory import TitansInspiredMemory

memory = TitansInspiredMemory("memory_dir")
memory.store_memory("Machine learning is...", "ai_concepts")
relevant_memories = memory.retrieve_relevant_memories("What is deep learning?")
```

### LLM Providers

Configure and use different LLM providers:

```python
from metis_agent.core.llm_interface import configure_llm, get_llm

# Configure cloud-based LLMs
configure_llm("openai", "gpt-4o")  # OpenAI
configure_llm("groq", "llama-3.1-8b-instant")  # Groq
configure_llm("anthropic", "claude-3-opus-20240229")  # Anthropic

# Configure local HuggingFace models (no API key required)
configure_llm("huggingface", "gpt2")  # Small model
configure_llm("huggingface", "microsoft/DialoGPT-small")  # Chat model
configure_llm("huggingface", "TinyLlama/TinyLlama-1.1B-Chat-v1.0")  # Larger model

# Configure Ollama local models (no API key required)
configure_llm("ollama", "tinydolphin")  # Ollama model

# Get configured LLM
llm = get_llm()
response = llm.chat([{"role": "user", "content": "Hello!"}])
```

#### Popular Local Models

**HuggingFace Models (Small - < 1GB):**
- `gpt2` - OpenAI's GPT-2 base model
- `distilgpt2` - Distilled version of GPT-2
- `microsoft/DialoGPT-small` - Conversational model

**HuggingFace Models (Medium - 1-5GB):**
- `microsoft/DialoGPT-medium` - Better conversational model
- `TinyLlama/TinyLlama-1.1B-Chat-v1.0` - Efficient chat model
- `QuixiAI/TinyDolphin-2.8-1.1b` - Instruction-tuned model

**HuggingFace Models (Large - 5GB+):**
- `microsoft/DialoGPT-large` - High-quality conversations
- `EleutherAI/gpt-neo-2.7B` - Large generative model

**Ollama Models:**
- `tinydolphin` - Small, efficient model (default)
- `llama2` - Meta's Llama 2 model
- `codellama` - Code-specialized model
- `mistral` - Mistral 7B model

### Tools

Available tools (36+ advanced tools):

#### **Security & Execution**
- `E2BCodeSandboxTool`: Secure Python code execution in isolated cloud environments
- `BashTool`: Safe system command execution with output capture

#### **Development & Code**
- `GitIntegrationTool`: Complete Git workflow management
- `CodeGenerationTool`: Multi-language code generation with best practices
- `PythonCodeTool`: Python-specific code analysis and execution
- `UnitTestGeneratorTool`: Automated test creation with comprehensive coverage
- `DependencyAnalyzerTool`: Project dependency analysis and optimization
- `EditTool`: Intelligent code editing with context awareness

#### **Research & Analysis**
- `DeepResearchTool`: Multi-source research with citation management
- `DataAnalysisTool`: Advanced analytics with pandas, numpy, visualization
- `GoogleSearchTool`: Real-time web search with result processing
- `WebScraperTool`: Intelligent content extraction
- `FirecrawlTool`: Advanced web scraping and content analysis
- `TextAnalyzerTool`: NLP analysis with sentiment and entity recognition

#### **Content & Communication**
- `ContentGenerationTool`: Multi-format content creation (blogs, docs, emails)
- `ConversationManagerTool`: Advanced dialogue management

#### **Project & Workflow Management**
- `ProjectManagementTool`: Full project lifecycle management
- `ProjectValidationTool`: Automated project validation and quality checks
- `BlueprintExecutionTool`: Workflow automation and process execution
- `RequirementsAnalysisTool`: Automated requirements gathering and analysis
- `ToolGeneratorTool`: Dynamic tool creation and customization

#### **File & System Operations**
- `FileManagerTool`: Complete file system operations with safety checks
- `FilesystemTool`: Advanced file system navigation and management
- `ReadTool`: Intelligent file reading with format detection
- `WriteTool`: Smart file writing with backup and validation
- `GrepTool`: Advanced search with regex and pattern matching

#### **Mathematical & Scientific**
- `AdvancedMathTool`: Complex mathematical computations and analysis
- `CalculatorTool`: Mathematical calculations with expression parsing

Creating custom tools:

```python
from metis_agent.tools.base import BaseTool
from metis_agent.tools.registry import register_tool

class MyTool(BaseTool):
    name = "my_tool"
    description = "Custom tool for specific tasks"
    
    def can_handle(self, task):
        # Determine if this tool can handle the task
        return "specific task" in task.lower()
        
    def execute(self, task):
        # Execute the task
        return f"Task executed: {task}"

# Register the tool
register_tool("my_tool", MyTool)
```

### API Key Management

Secure storage and retrieval of API keys:

```python
from metis_agent.auth.api_key_manager import APIKeyManager

key_manager = APIKeyManager()
key_manager.set_key("openai", "your-api-key")
api_key = key_manager.get_key("openai")
services = key_manager.list_services()
```

## Testing

Run the comprehensive test suite:

```bash
# Run system tests
python metis_agent/test_system.py

# Run CLI tests
python metis_agent/test_cli.py
```

## Advanced Usage

### Session Management

Maintain context across multiple interactions:

```python
agent = SingleAgent()

# First query
response1 = agent.process_query(
    "What are the main types of machine learning?",
    session_id="user123"
)

# Follow-up query (uses context from first query)
response2 = agent.process_query(
    "Can you explain supervised learning in more detail?",
    session_id="user123"
)
```

### Tool Selection

Specify which tool to use for a query:

```python
agent = SingleAgent()

# Use a specific tool
response = agent.process_query(
    "Generate a Python function to sort a list",
    tool_name="CodeGenerationTool"
)
```

### Memory Insights

Get insights about the agent's memory:

```python
agent = SingleAgent(use_titans_memory=True)

# Process some queries
agent.process_query("What is machine learning?", session_id="user123")
agent.process_query("Explain neural networks", session_id="user123")

# Get memory insights
insights = agent.get_memory_insights()
print(insights)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contact & Links

- **PyPI Package**: [https://pypi.org/project/metis-agent/](https://pypi.org/project/metis-agent/)
- **Starter Templates**: [https://github.com/metis-analytics/metis-starter](https://github.com/metis-analytics/metis-starter)
- **Documentation**: [https://github.com/metis-analytics/metis-agent/wiki](https://github.com/metis-analytics/metis-agent/wiki)
- **Issues & Support**: [https://github.com/metis-analytics/metis-agent/issues](https://github.com/metis-analytics/metis-agent/issues)
- **Discussions**: [https://github.com/metis-analytics/metis-agent/discussions](https://github.com/metis-analytics/metis-agent/discussions)

---

<p align="center">
  <strong>Metis Agent - Building Intelligent AI Systems</strong>
</p>