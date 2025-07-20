# Metis Agent CLI Documentation

**Version**: 0.1.5  
**Description**: AI Agent Framework with Multi-Phase Development Support  

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Command Groups](#command-groups)
  - [Authentication](#authentication-auth)
  - [Code Intelligence](#code-intelligence-code)
  - [Dependency Management](#dependency-management-deps)
  - [File Operations](#file-operations-files)
  - [Project Generation](#project-generation-generate)
  - [Git Integration](#git-integration-git)
  - [Memory Management](#memory-management-memory)
  - [Project Management](#project-management-project)
  - [Task Management](#task-management-tasks)
  - [Tool Management](#tool-management-tools)
  - [LLM Configuration](#llm-configuration-configure-llm)
  - [Agent Execution](#agent-execution-run)
  - [Web Server](#web-server-serve)
- [Examples](#examples)
- [Best Practices](#best-practices)

## Installation

```bash
pip install metis-agent>=0.1.3
```

## Quick Start

```bash
# Configure your LLM provider
metis configure-llm

# Generate a new project
metis generate project "FastAPI backend with PostgreSQL" --name my-api

# Run an agent
metis run "analyze this codebase and suggest improvements"

# Start web interface
metis serve
```

## Command Groups

### Authentication (`auth`)

Manage API keys and authentication for LLM providers.

```bash
# Store API key for a provider
metis auth set-key openai YOUR_API_KEY

# List configured providers
metis auth list-keys

# Validate API key
metis auth validate openai

# Remove API key
metis auth remove-key openai
```

**Supported Providers:**
- `openai` - OpenAI GPT models
- `anthropic` - Claude models  
- `groq` - Groq LLaMA models
- `huggingface` - HuggingFace models

### Code Intelligence (`code`)

Code analysis, generation, and refactoring capabilities.

```bash
# Analyze code quality and structure
metis code analyze [PATH]

# Generate code from description
metis code generate "create a REST API endpoint for user management"

# Refactor code with suggestions
metis code refactor [FILE] --suggestions

# Review code and provide feedback
metis code review [PATH]

# Generate documentation
metis code document [PATH]
```

**Options:**
- `--language` - Specify programming language
- `--output` - Output file/directory
- `--format` - Output format (markdown, json, text)

### Dependency Management (`deps`)

Manage project dependencies and virtual environments.

```bash
# Install dependencies
metis deps install

# Add new dependency
metis deps add package-name[==version]

# Update dependencies
metis deps update [PACKAGE]

# Remove dependency
metis deps remove package-name

# List installed packages
metis deps list

# Check for security vulnerabilities
metis deps audit

# Create requirements file
metis deps freeze > requirements.txt
```

**Options:**
- `--dev` - Install development dependencies
- `--upgrade` - Upgrade to latest versions
- `--dry-run` - Show what would be installed

### File Operations (`files`)

File system operations and content management.

```bash
# List directory contents
metis files list [PATH] [--pattern PATTERN]

# Read file content
metis files read FILE

# Search for files
metis files find PATTERN [--path PATH]

# Search within file contents
metis files search QUERY [--path PATH]

# Copy files/directories
metis files copy SOURCE DEST

# Move files/directories
metis files move SOURCE DEST

# Delete files/directories
metis files delete PATH [--recursive]

# Create directory structure
metis files mkdir PATH [--parents]
```

**Options:**
- `--recursive` - Apply recursively
- `--pattern` - File pattern matching
- `--ignore` - Ignore patterns (.gitignore style)

### Project Generation (`generate`)

**Phase 4**: Advanced multi-file project scaffolding with AI-powered generation.

#### Project Generation
```bash
# Generate complete projects
metis generate project "DESCRIPTION" [OPTIONS]

# Examples
metis generate project "FastAPI backend with PostgreSQL database" --name my-api
metis generate project "React frontend with TypeScript" --name my-app --type react-app
metis generate project "Full-stack e-commerce platform" --name shop --type fullstack
```

**Options:**
- `--name NAME` - Project name (auto-generated if not provided)
- `--type TYPE` - Project type: `python-api`, `react-app`, `fullstack`
- `--features FEATURES` - Comma-separated features: `database`, `auth`, `testing`

#### Feature Generation
```bash
# Generate new features for existing projects
metis generate feature "user authentication system" --project PATH

# Generate API endpoints
metis generate api "product management endpoints" --project PATH

# Generate React components
metis generate component "product list component" --project PATH

# Generate CRUD operations
metis generate crud "User" --project PATH
```

**Generated Project Structure:**
```
project-name/
├── README.md              # Project overview and setup
├── tasks.md               # Development tasks and milestones  
├── requirements.md        # Detailed requirements specification
├── requirements.txt       # Python dependencies
├── main.py               # Application entry point
├── config.py             # Configuration settings
├── models/               # Data models
├── routes/               # API routes (FastAPI)
├── src/                  # Source code (React)
└── tests/                # Test files
```

### Git Integration (`git`)

**Phase 3**: Comprehensive git workflow management.

```bash
# Initialize repository
metis git init [PATH]

# Stage and commit changes
metis git commit "commit message" [--all]

# Create and manage branches
metis git branch create BRANCH_NAME
metis git branch switch BRANCH_NAME
metis git branch list

# Push/pull changes
metis git push [--set-upstream]
metis git pull [--rebase]

# Merge branches
metis git merge BRANCH_NAME [--no-ff]

# View history and status
metis git status
metis git log [--oneline] [--graph]

# Manage remotes
metis git remote add NAME URL
metis git remote list

# Advanced operations
metis git stash [--include-untracked]
metis git reset [--hard] [COMMIT]
metis git rebase BRANCH [--interactive]
```

### Memory Management (`memory`)

Manage agent memory and context persistence.

```bash
# Store information in memory
metis memory store "key information about the project"

# Retrieve memories
metis memory search "query"
metis memory get MEMORY_ID

# List all memories
metis memory list [--tag TAG]

# Clear memories
metis memory clear [--confirm]
metis memory delete MEMORY_ID

# Export/import memory
metis memory export memories.json
metis memory import memories.json
```

### Project Management (`project`)

**Phase 1-2**: Project scaffolding and structure management.

```bash
# Create new project structure
metis project create PROJECT_NAME [--template TEMPLATE]

# Initialize existing directory as project
metis project init [PATH]

# Validate project structure
metis project validate

# List project templates
metis project templates

# Update project structure
metis project update [--force]

# Project information
metis project info
```

**Available Templates:**
- `python-basic` - Basic Python project
- `python-api` - FastAPI project template
- `react-app` - React application template
- `data-science` - Jupyter/Data Science template

### Task Management (`tasks`)

Manage development tasks and workflows.

```bash
# List tasks
metis tasks list [--status STATUS]

# Create new task
metis tasks create "task description" [--priority PRIORITY]

# Update task status
metis tasks update TASK_ID --status STATUS

# Complete task
metis tasks complete TASK_ID

# Delete task
metis tasks delete TASK_ID

# Show task details
metis tasks show TASK_ID

# Task statistics
metis tasks stats
```

**Task Statuses:** `todo`, `in-progress`, `review`, `done`  
**Priorities:** `low`, `medium`, `high`, `urgent`

### Tool Management (`tools`)

Manage agent tools and capabilities.

```bash
# List available tools
metis tools list [--category CATEGORY]

# Get tool information
metis tools info TOOL_NAME

# Test tool functionality
metis tools test TOOL_NAME

# Enable/disable tools
metis tools enable TOOL_NAME
metis tools disable TOOL_NAME

# Tool statistics and usage
metis tools stats
```

**Available Tool Categories:**
- `code` - Code generation and analysis
- `content` - Content generation
- `search` - Web search and data retrieval
- `files` - File system operations
- `git` - Version control
- `project` - Project management

### LLM Configuration (`configure-llm`)

Configure Large Language Model providers and settings.

```bash
# Interactive LLM configuration
metis configure-llm

# Set specific provider
metis configure-llm --provider openai

# Configure model parameters
metis configure-llm --model gpt-4 --temperature 0.7 --max-tokens 2048

# Test LLM connection
metis configure-llm --test

# Show current configuration
metis configure-llm --show
```

**Supported Providers:**
- **Groq** (Recommended) - Fast inference with LLaMA models
- **Anthropic** - Claude models (claude-3-sonnet, claude-3-haiku)
- **OpenAI** - GPT models (gpt-4, gpt-3.5-turbo)  
- **HuggingFace** - Open source models

### Agent Execution (`run`)

Execute AI agents with specific prompts and tasks.

```bash
# Run agent with prompt
metis run "analyze this codebase and suggest improvements"

# Run with specific tools
metis run "create a React component" --tools code,files

# Run with context
metis run "refactor this function" --context ./src/utils.py

# Interactive mode
metis run --interactive

# Save results
metis run "generate documentation" --output docs/

# Run with memory
metis run "continue previous task" --use-memory
```

**Options:**
- `--tools TOOLS` - Specify tools to use
- `--context PATH` - Provide context files/directories
- `--output PATH` - Save results to file/directory
- `--interactive` - Interactive conversation mode
- `--use-memory` - Use persistent memory
- `--verbose` - Show detailed execution logs

### Web Server (`serve`)

Start the Metis web interface for GUI interaction.

```bash
# Start web server
metis serve [--host HOST] [--port PORT]

# Start with specific configuration
metis serve --host 0.0.0.0 --port 8080

# Start in development mode
metis serve --dev --reload

# Start with authentication
metis serve --auth --secret-key SECRET
```

**Default**: `http://localhost:8000`

**Web Interface Features:**
- Interactive chat with agents
- Project management dashboard  
- File browser and editor
- Task tracking and workflows
- Memory visualization
- Tool management interface

## Examples

### Quick Project Setup
```bash
# 1. Configure LLM (first time only)
metis configure-llm

# 2. Generate a new FastAPI project
metis generate project "FastAPI backend with authentication and database" --name my-api

# 3. Navigate to project
cd my-api

# 4. Install dependencies
metis deps install

# 5. Initialize git repository
metis git init
metis git commit "Initial project structure" --all

# 6. Start development
python main.py
```

### AI-Powered Development Workflow
```bash
# Analyze existing codebase
metis code analyze ./src

# Generate new feature
metis generate feature "user profile management" --project .

# Review and refactor code  
metis code review ./src --suggestions

# Commit changes
metis git commit "Add user profile management feature" --all

# Generate documentation
metis code document ./src --output docs/
```

### Multi-Agent Collaboration
```bash
# Start web interface for team collaboration
metis serve --host 0.0.0.0 --port 8080

# Use memory for context persistence
metis memory store "Project requirements: e-commerce platform with React frontend and FastAPI backend"

# Generate frontend
metis generate project "React e-commerce frontend" --name ecommerce-frontend --type react-app

# Generate backend  
metis generate project "FastAPI e-commerce backend" --name ecommerce-backend --type python-api

# Run analysis across both projects
metis run "analyze integration points between frontend and backend" --context ./ecommerce-frontend ./ecommerce-backend
```

## Best Practices

### 1. **Environment Setup**
- Always configure your LLM provider first: `metis configure-llm`
- Use environment variables for API keys: `.env` files
- Keep API keys secure and never commit them to version control

### 2. **Project Generation**
- Use descriptive project descriptions for better AI understanding
- Specify project names explicitly: `--name my-project`
- Review generated `tasks.md` and `requirements.md` files
- Customize generated code before starting development

### 3. **Git Workflow Integration**
- Initialize git immediately after project generation
- Use meaningful commit messages with `metis git commit`
- Create feature branches: `metis git branch create feature/new-feature`
- Leverage git integration for team collaboration

### 4. **Memory Management**
- Store important project context: `metis memory store`
- Use descriptive tags for better memory organization
- Regular memory cleanup to avoid context pollution
- Export memories before major project changes

### 5. **Tool Usage**
- Start with `metis tools list` to see available capabilities
- Use specific tools for focused tasks: `--tools code,files`
- Test tools individually before complex workflows
- Monitor tool performance with `metis tools stats`

### 6. **Development Workflow**
```bash
# Recommended daily workflow
metis memory search "yesterday's progress"    # Resume context
metis tasks list --status in-progress        # Check active tasks  
metis run "continue development"              # Interactive development
metis git commit "Daily progress" --all      # Save progress
metis memory store "Today's achievements"    # Store context
```

---

**Need Help?** 
- Run any command with `--help` for detailed usage
- Use `metis run --interactive` for guided assistance
- Check `metis tools list` for available capabilities
- Visit the web interface: `metis serve` → `http://localhost:8000`

**Version**: 0.1.3 | **License**: Apache 2.0 | **Support**: Multi-terminal parallel development workflows
