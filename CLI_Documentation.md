# Metis Agent CLI Documentation

**Version:** v0.6.0  
**Command:** `metis`

The Metis Agent CLI provides a comprehensive command-line interface for AI-powered development, project management, and intelligent assistance. Built on natural language processing, it allows developers to interact with their projects using conversational commands.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Commands](#core-commands)
- [Natural Language Code Interface](#natural-language-code-interface)
- [Configuration Management](#configuration-management)
- [Authentication](#authentication)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)

## Installation

```bash
# Install Metis Agent
pip install metis-agent

# Verify installation
metis --help
```

## Quick Start

```bash
# Start interactive chat
metis chat

# Process a single query
metis chat "analyze this project structure"

# Natural language coding
metis code "create a FastAPI web server with authentication"

# Interactive coding session
metis code --interactive
```

## Core Commands

### Main CLI Structure

```bash
metis [COMMAND] [OPTIONS] [ARGUMENTS]
```

**Available Commands:**
- `chat` - Interactive conversation with the AI agent
- `code` - Natural language coding assistant
- `config` - Configuration management
- `auth` - API key and authentication management

## Natural Language Code Interface

The `metis code` command provides a revolutionary natural language interface for all coding tasks.

### Basic Usage

```bash
# Single request mode
metis code "analyze this project and tell me about its structure"
metis code "create a Python web app with FastAPI and authentication"
metis code "refactor the calculate method in calculator.py"
metis code "add error handling to all database operations"

# Interactive mode
metis code --interactive
metis code -i

# Auto mode (skip confirmations)
metis code --auto "create a new file utils.py with helper functions"
metis code -a "optimize the database queries in models.py"
```

### Advanced Features

```bash
# Session management
metis code --session my-feature "implement user authentication"
metis code -s backend-api "add API rate limiting"

# Branch management
metis code --branch feature-auth "implement OAuth2 authentication"
metis code --no-branch "quick bug fix in utils.py"

# Project creation
metis code "create a complete Django e-commerce application"
metis code "build a React dashboard with charts and analytics"
```

### Natural Language Examples

The code command understands natural language requests:

**Project Creation:**
```bash
metis code "create a FastAPI backend with PostgreSQL and JWT authentication"
metis code "build a React frontend with TypeScript and Material-UI"
metis code "make a Discord bot with slash commands and database integration"
```

**Code Analysis:**
```bash
metis code "analyze this codebase and identify potential security issues"
metis code "review the performance of database queries in this project"
metis code "find all TODO comments and create a task list"
```

**Code Generation:**
```bash
metis code "add comprehensive error handling to all API endpoints"
metis code "create unit tests for the user authentication module"
metis code "implement caching for frequently accessed data"
```

**Refactoring:**
```bash
metis code "refactor this class to follow SOLID principles"
metis code "optimize the database schema for better performance"
metis code "modernize this legacy code to use current best practices"
```

### Intelligent Features

- **Project Detection**: Automatically detects project type and context
- **Branch Creation**: Creates feature branches for significant changes
- **Code Extraction**: Saves generated code to appropriate files
- **Git Integration**: Auto-commits changes with descriptive messages
- **Multi-Phase Workflows**: Handles complex project development in phases

## Configuration Management

### Configuration Commands

```bash
# Show current configuration
metis config show

# Set configuration values
metis config set <key> <value>
metis config set llm_provider openai
metis config set memory_enabled true

# Agent identity management
metis config show-identity
metis config set-name "MyAgent"
metis config set-personality --interactive
metis config regenerate-identity

# Reset to defaults
metis config reset
```

### System Message Management

```bash
# Set system message from file
metis config set-system-message --file system_prompt.txt

# Interactive system message setup
metis config set-system-message --interactive

# Set agent personality
metis config set-personality --file personality.txt
metis config set-personality --interactive
```

## Authentication

### API Key Management

```bash
# Set API keys
metis auth set openai sk-your-key-here
metis auth set groq gsk-your-key-here
metis auth set anthropic your-key-here

# List configured keys
metis auth list

# Remove API key
metis auth remove openai

# Test API connectivity
metis auth test
metis auth test openai
```

### Supported Services

- **OpenAI**: `openai`
- **Groq**: `groq`
- **Anthropic**: `anthropic`
- **Google**: `google`
- **Hugging Face**: `huggingface`
- **E2B Code Sandbox**: `e2b`
- **Firecrawl**: `firecrawl`

## Examples

### Complete Workflow Examples

**1. Creating a New Web Application:**
```bash
# Generate project
metis code "create a FastAPI backend with user authentication and PostgreSQL"

# Add features
metis code "add API rate limiting and request validation"

# Test the application
metis code "create comprehensive tests for all endpoints"
```

**2. Working with Existing Project:**
```bash
# Analyze existing codebase
metis chat "analyze this project and suggest improvements"

# Make improvements
metis code "optimize database queries and add caching"

# Add documentation
metis code "create comprehensive API documentation"
```

**3. Interactive Development Session:**
```bash
# Start interactive session
metis code --interactive

# In the session:
# > "I want to add user authentication to this Flask app"
# > "also add password reset functionality"
# > "create comprehensive tests for the auth system"
# > "exit"
```

### Natural Language Examples

**Project Creation:**
```bash
metis code "create a complete e-commerce platform with React frontend and Node.js backend"
metis code "build a data analysis dashboard with Python, Pandas, and Plotly"
metis code "make a real-time chat application with WebSockets"
```

**Code Analysis and Improvement:**
```bash
metis code "analyze this codebase for security vulnerabilities"
metis code "refactor this monolith into microservices"
metis code "add comprehensive error handling and logging"
metis code "optimize performance and reduce memory usage"
```

**Specific Tasks:**
```bash
metis code "implement OAuth2 authentication with Google and GitHub"
metis code "add database migrations and seed data"
metis code "create API documentation with Swagger/OpenAPI"
metis code "set up CI/CD pipeline with GitHub Actions"
```

## Advanced Features

### Multi-Phase Development

For complex projects, Metis automatically breaks down work into phases:

1. **Planning Phase**: Analyzes requirements and creates development plan
2. **Implementation Phase**: Generates code and project structure
3. **Testing Phase**: Creates tests and validation
4. **Documentation Phase**: Generates documentation and README
5. **Deployment Phase**: Sets up deployment configuration

### Blueprint Workflows

Metis includes pre-built blueprints for common development patterns:

- **Code Generation**: Intelligent code creation and modification
- **API Development**: RESTful API with authentication
- **Frontend Applications**: Modern web applications
- **Data Analysis**: Analysis and visualization workflows

### Intelligent Context Awareness

- **Code Pattern Recognition**: Understands existing code patterns
- **Context Understanding**: Analyzes current working directory
- **Session Memory**: Maintains context across interactions
- **Natural Language Processing**: Interprets complex development requests

## Configuration

### Environment Variables

```bash
# API Keys (recommended to use .env.local file)
OPENAI_API_KEY=your-openai-key
GROQ_API_KEY=your-groq-key
ANTHROPIC_API_KEY=your-anthropic-key
E2B_API_KEY=your-e2b-key
FIRECRAWL_API_KEY=your-firecrawl-key
GOOGLE_API_KEY=your-google-key
```

### Configuration File

Metis stores configuration in `~/.metis/config.json`:

```json
{
  "llm_provider": "groq",
  "llm_model": "llama-3.1-8b-instant",
  "memory_enabled": true,
  "titans_memory": true,
  "enhanced_processing": true,
  "agent_identity": {
    "agent_id": "metis-abc123",
    "agent_name": "CustomAgent",
    "custom_system_message": "..."
  }
}
```

## Troubleshooting

### Common Issues

**1. Command Not Found:**
```bash
# Ensure Metis is installed
pip install metis-agent

# Check if it's in PATH
which metis  # Linux/Mac
where metis  # Windows
```

**2. API Key Issues:**
```bash
# Set API keys
metis auth set openai your-key-here

# Test connectivity
metis auth test

# Check configuration
metis config show
```

**3. Code Generation Issues:**
```bash
# Test with simple request
metis code "create a simple hello world script"

# Check if in correct directory
pwd
ls -la
```

### Debug Mode

```bash
# Enable verbose output
export METIS_DEBUG=1
metis code "your request"

# Check logs
metis config show
```

### Getting Help

```bash
# General help
metis --help

# Command-specific help
metis code --help
metis config --help
metis auth --help

# Interactive help
metis chat "how do I use the code command?"
```

## Best Practices

### 1. Code Organization

- Use descriptive file and variable names
- Organize code into logical modules
- Follow language-specific best practices
- Use environment variables for API keys

### 2. Natural Language Commands

- Be specific about requirements
- Mention technology preferences
- Include context about existing code
- Ask for explanations when needed

### 3. Session Management

- Use sessions for related work
- Name sessions descriptively
- Switch sessions for different features
- Clean up old sessions periodically

### 4. Security

- Never commit API keys to version control
- Use environment variables or .env.local files
- Review generated code before deployment
- Validate all user inputs in generated code

### 5. Development Workflow

- Start with clear requirements
- Use interactive mode for complex tasks
- Test generated code thoroughly
- Iterate and refine based on results

## Integration with IDEs

### VS Code Integration

Metis CLI works seamlessly with VS Code:

```bash
# Open project in VS Code after generation
metis code "create a React app" && code .

# Use integrated terminal
# Ctrl+` to open terminal, then use metis commands
```

### Terminal Integration

```bash
# Add to shell profile for aliases
alias mc="metis code"
alias mch="metis chat"
alias mconf="metis config"

# Use with other tools
metis code "analyze this code" && echo "Analysis complete"
metis chat "explain this error" && echo "Help provided"
```

## Updates and Maintenance

### Keeping Metis Updated

```bash
# Update to latest version
pip install --upgrade metis-agent

# Check version
metis --version

# Check for new features
metis chat "what's new in the latest version?"
```

### Configuration Backup

```bash
# Backup configuration
cp ~/.metis/config.json ~/.metis/config.backup.json

# Restore configuration
cp ~/.metis/config.backup.json ~/.metis/config.json
```

---

## Support and Community

- **Documentation**: [Official Docs](https://metis-agent.readthedocs.io)
- **GitHub**: [metis-agent/metis-agent](https://github.com/metis-agent/metis-agent)
- **Issues**: Report bugs and request features on GitHub
- **Discussions**: Community discussions and Q&A

---

**Version**: v0.6.0  
**Last Updated**: August 2025  
**License**: Apache License 2.0
