# Metis Agent CLI Reference

The Metis Agent CLI provides a comprehensive command-line interface for interacting with the framework. This reference covers all available commands, options, and usage patterns.

## Installation & Setup

### Install Metis Agent
```bash
pip install metis-agent
```

### Verify Installation
```bash
metis --help
```

### Set API Key (Required)
```bash
# Set Groq API key (recommended - free tier available)
metis auth set groq YOUR_GROQ_API_KEY

# Or set OpenAI API key
metis auth set openai YOUR_OPENAI_API_KEY

# Or set Anthropic API key
metis auth set anthropic YOUR_ANTHROPIC_API_KEY
```

## Main Commands Overview

```bash
metis [COMMAND] [OPTIONS] [ARGS]
```

### Available Commands

| Command | Description |
|---------|-------------|
| `chat` | Interactive chat mode or single query processing |
| `code` | Natural language coding assistant with development tools |
| `todo` | Task management and workflow organization |
| `agents` | Multi-agent system management |
| `config` | Configuration and settings management |
| `auth` | API key and authentication management |

## Command Reference

### 1. Chat Command

Start interactive conversations or process single queries.

**Usage:**
```bash
# Interactive mode
metis chat

# Single query
metis chat "What is machine learning?"

# With session context
metis chat --session project_review "Analyze my Python project"
```

**Options:**
- `--session, -s TEXT` - Session ID for maintaining context across conversations

**Examples:**
```bash
# Start interactive session
metis chat

# One-off query
metis chat "Explain quantum computing in simple terms"

# Continue previous conversation
metis chat --session work_session "What did we discuss about APIs?"
```

### 2. Code Command

Comprehensive development assistant with natural language processing.

**Basic Usage:**
```bash
# Natural language requests
metis code "analyze this Python project structure"
metis code "create a REST API with authentication"
metis code "fix syntax errors in main.py"
metis code "generate unit tests for the User class"
```

**Structured Subcommands:**

#### Create
```bash
# Create files and components
metis code create component UserCard
metis code create api AuthAPI
metis code create test calculator.py
metis code c component LoginForm  # 'c' is alias for 'create'
```

#### Edit
```bash
# Edit specific files
metis code edit main.py "add error handling"
metis code edit config.py "update database settings"
metis code e app.py "refactor user authentication"  # 'e' is alias
```

#### Fix
```bash
# Fix code issues
metis code fix --type syntax
metis code fix --type logic main.py
metis code f  # Interactive fix mode
```

#### Test
```bash
# Generate and run tests
metis code test generate calculator.py
metis code test run
metis code t unit  # Run unit tests only
```

#### Documentation
```bash
# Generate documentation
metis code docs generate
metis code docs api
metis code d readme  # Generate README
```

#### Status & Analysis
```bash
# Project status and analysis
metis code status
metis code diff main.py
metis code s  # Quick status check
```

#### Markdown Generation
```bash
# Professional document generation
metis code md prd "User Authentication System"
metis code md api "REST API Documentation"
metis code md readme
```

#### Git Integration
```bash
# Smart commit generation
metis code commit
metis code commit --message "Add user authentication"
```

**Global Options:**
- `--session, -s TEXT` - Session ID for context
- `--branch, -b TEXT` - Create named feature branch
- `--no-branch` - Skip automatic branch creation
- `--auto, -a` - Auto mode, skip prompts
- `--fast` - Fast mode for simple operations
- `--stream` - Streaming mode for complex operations
- `--yes, -y` - Skip confirmations
- `--review` - Force detailed review mode
- `--interface [simple|advanced|expert]` - Set interface complexity

**Examples:**
```bash
# Create a complete web application
metis code "create a Flask web app with user authentication and a dashboard"

# Analyze and improve existing code
metis code "review my Python project and suggest improvements"

# Generate comprehensive documentation
metis code docs generate --include-api --include-examples

# Quick bug fixes
metis code fix --auto --fast
```

### 3. Todo Command

Advanced task management system for complex workflows.

**Basic Usage:**
```bash
# Quick start with automatic task breakdown
metis todo start "Build a REST API with authentication"

# Create empty session
metis todo create "Web Development Project"

# Add individual tasks
metis todo add "Set up Flask application structure"
```

**Session Management:**
```bash
# List all sessions
metis todo sessions

# Load specific session
metis todo load project_001

# Show current session status
metis todo status
```

**Task Management:**
```bash
# List all tasks in current session
metis todo list

# Mark task as completed
metis todo complete 1

# Update task status
metis todo update 2 in_progress

# Get next suggested task
metis todo next
```

**Advanced Features:**
```bash
# Automatic task breakdown from natural language
metis todo breakdown "Create a user management system with CRUD operations"

# Progress tracking and analytics
metis todo progress

# Show detailed help
metis todo help
```

**Examples:**
```bash
# Start new project workflow
metis todo start "Build an e-commerce website with Python and React"

# Continue existing work
metis todo load ecommerce_project
metis todo next

# Track progress
metis todo progress
metis todo list --status pending
```

### 4. Agents Command

Multi-agent system management for complex orchestration.

**System Management:**
```bash
# Initialize multi-agent system
metis agents init

# Show system status
metis agents system

# List all active agents
metis agents list
```

**Agent Management:**
```bash
# Create specialized agent
metis agents create --type researcher --name "DataResearcher"

# Get agent status
metis agents status agent_001

# Stop specific agent
metis agents stop agent_001
```

**Knowledge Sharing:**
```bash
# Share knowledge between agents
metis agents share --from agent_001 --to agent_002 --topic "project_context"

# List shared knowledge
metis agents knowledge

# Cleanup system data
metis agents cleanup
```

**Examples:**
```bash
# Set up multi-agent development team
metis agents init
metis agents create --type coder --name "BackendDev"
metis agents create --type tester --name "QAEngineer"
metis agents create --type reviewer --name "CodeReviewer"

# Coordinate agent collaboration
metis agents share --from BackendDev --to QAEngineer --topic "api_endpoints"
```

### 5. Config Command

Configuration and customization management.

**Basic Configuration:**
```bash
# Show current configuration
metis config show

# Set configuration values
metis config set llm_provider groq
metis config set llm_model llama-3.1-8b-instant

# Reset to defaults
metis config reset
```

**LLM Configuration:**
```bash
# List available models for current provider
metis config list-models

# Configure HuggingFace local models
metis config hf-device auto
metis config hf-quantization 8bit
metis config hf-max-length 2048

# Configure Ollama
metis config ollama-url http://localhost:11434
```

**Agent Identity:**
```bash
# Show agent identity
metis config identity

# Set custom agent name
metis config set-name "DevAssistant"

# Set agent personality
metis config set-personality "You are a senior software architect"

# Regenerate identity
metis config regenerate-identity
```

**System Messages:**
```bash
# Set system message
metis config system-message base
metis config system-message custom "You are an expert Python developer"
```

**Knowledge Base:**
```bash
# Knowledge base configuration
metis config knowledge init
metis config knowledge status
```

**Examples:**
```bash
# Configure for Python development
metis config set-name "PythonExpert"
metis config set-personality "You are a senior Python developer with expertise in web frameworks"
metis config set llm_provider openai
metis config set llm_model gpt-4o-mini

# Configure for local development
metis config set llm_provider ollama
metis config ollama-url http://localhost:11434
metis config hf-device cuda
```

### 6. Auth Command

API key and authentication management with secure encryption.

**API Key Management:**
```bash
# Set API keys
metis auth set groq YOUR_GROQ_API_KEY
metis auth set openai YOUR_OPENAI_API_KEY
metis auth set anthropic YOUR_ANTHROPIC_API_KEY

# List configured keys
metis auth list

# Remove API key
metis auth remove openai
```

**Testing Connectivity:**
```bash
# Test specific provider
metis auth test groq
metis auth test openai

# Test all configured providers
metis auth test
```

**Examples:**
```bash
# Initial setup
metis auth set groq gsk_your_groq_key_here
metis auth test groq

# Multiple providers
metis auth set openai sk-your_openai_key
metis auth set anthropic sk-ant-your_anthropic_key
metis auth list

# Troubleshooting
metis auth test openai
```

## Advanced Usage Patterns

### 1. Chaining Commands

```bash
# Development workflow
metis code create api UserAPI && \
metis code test generate user_api.py && \
metis code commit

# Project setup
metis todo start "Build web application" && \
metis agents init && \
metis code status
```

### 2. Session Management

```bash
# Start focused development session
metis chat --session feature_auth "Starting work on authentication feature"
metis code --session feature_auth "analyze current auth system"
metis todo --session feature_auth create "Authentication improvements"
```

### 3. Configuration Profiles

```bash
# Development profile
metis config set llm_provider groq
metis config set-name "DevBot"
metis config set-personality "Senior full-stack developer"

# Research profile  
metis config set llm_provider openai
metis config set-name "Researcher"
metis config set-personality "Academic researcher with deep technical knowledge"
```

### 4. Automation Scripts

Create shell scripts for common workflows:

```bash
#!/bin/bash
# development_workflow.sh

echo "Starting development workflow..."
metis config set llm_provider groq
metis todo start "$1"
metis code status
metis agents init
echo "Development environment ready!"
```

## Interactive Mode Features

### Chat Mode Interactive Commands
```bash
metis chat
> /help          # Show help
> /config        # Show configuration
> /memory        # Show memory status
> /tools         # List available tools
> /session new   # Start new session
> /quit          # Exit
```

### Code Mode Interactive Commands
```bash
metis code
> /create component UserCard
> /edit main.py
> /test run
> /docs generate
> /status
> /help
> /quit
```

## Environment Variables

Set these environment variables as alternatives to CLI configuration:

```bash
# LLM Provider API Keys
export GROQ_API_KEY="your_groq_key"
export OPENAI_API_KEY="your_openai_key"
export ANTHROPIC_API_KEY="your_anthropic_key"

# Optional Service APIs
export GOOGLE_API_KEY="your_google_key"
export E2B_API_KEY="your_e2b_key"
export FIRECRAWL_API_KEY="your_firecrawl_key"

# Configuration Override
export METIS_LLM_PROVIDER="groq"
export METIS_LLM_MODEL="llama-3.1-8b-instant"
```

## Configuration Files

Configuration is stored in:
- **Linux/Mac:** `~/.metis_agent/config.json`
- **Windows:** `%USERPROFILE%\.metis_agent\config.json`

Sample configuration:
```json
{
    "llm_provider": "groq",
    "llm_model": "llama-3.1-8b-instant",
    "memory_enabled": true,
    "titans_memory": true,
    "agent_name": "MetisAssistant",
    "max_context_length": 4000,
    "session_timeout": 3600
}
```

## Troubleshooting

### Common Issues

**Command not found:**
```bash
# Verify installation
pip install metis-agent
which metis  # Linux/Mac
where metis  # Windows
```

**API Key errors:**
```bash
# Check API keys
metis auth list
metis auth test groq

# Reset if needed
metis auth remove groq
metis auth set groq YOUR_NEW_KEY
```

**Configuration issues:**
```bash
# Check current config
metis config show

# Reset to defaults
metis config reset

# Verify agent identity
metis config identity
```

**Import or dependency errors:**
```bash
# Update to latest version
pip install --upgrade metis-agent

# Install with all dependencies
pip install metis-agent[dev,security,local-models]
```

### Getting Help

- **Command-specific help:** Add `--help` to any command
- **Interactive help:** Use `/help` in interactive modes
- **Verbose output:** Add `-v` or `--verbose` flags where available
- **Documentation:** Check examples in the `examples/` directory

## Performance Tips

1. **Use Groq for speed:** Fastest inference for most tasks
2. **Session management:** Use sessions for related tasks to maintain context
3. **Local models:** Use Ollama for privacy and offline work
4. **Batch operations:** Combine related tasks in single commands
5. **Auto mode:** Use `--auto` and `--fast` flags for simple operations

## Security Features

- **Encrypted storage:** API keys stored with AES-256-GCM encryption
- **Input validation:** All inputs validated against injection attacks
- **Secure execution:** Command execution with comprehensive sanitization
- **Path protection:** Advanced directory traversal prevention
- **Audit logging:** Security events logged for enterprise compliance

---

**For more examples and advanced usage, see the `examples/` directory in the repository.**