# Knowledge Base System - User Guide

The Metis Agent includes a powerful Knowledge Base system that allows you to store, organize, and retrieve information efficiently. The agent prioritizes knowledge base responses over tool execution, providing faster and more accurate answers for topics you've stored.

## Table of Contents

- [Quick Start](#quick-start)
- [Initialization](#initialization)
- [Managing Knowledge Entries](#managing-knowledge-entries)
- [Searching and Browsing](#searching-and-browsing)
- [Import and Export](#import-and-export)
- [Configuration](#configuration)
- [Categories and Tags](#categories-and-tags)
- [Best Practices](#best-practices)
- [Command Reference](#command-reference)

## Quick Start

### 1. Initialize the Knowledge Base

Choose a preset configuration that matches your use case:

```bash
# For software development
metis config knowledge init --preset coding

# For business use
metis config knowledge init --preset business

# For academic research
metis config knowledge init --preset academic

# For personal use
metis config knowledge init --preset personal
```

### 2. Add Your First Knowledge Entry

```bash
metis config knowledge add "Python Best Practices" \
  "Always use virtual environments when working with Python projects to avoid dependency conflicts." \
  --category programming --tags python,best-practices
```

### 3. Test the Knowledge Base

```bash
metis chat "What are Python best practices?"
```

The agent will now use your knowledge base to provide instant, accurate responses.

## Initialization

### Available Presets

**Coding Preset**
- Categories: programming, web-development, database, devops, testing
- Optimized for software development workflows
- Includes templates for code snippets and technical documentation

**Business Preset**
- Categories: company, projects, meetings, contacts, processes
- Designed for business knowledge management
- Templates for meeting notes and project documentation

**Academic Preset**
- Categories: research, papers, courses, references, notes
- Structured for academic and research work
- Templates for citations and research findings

**Personal Preset**
- Categories: journal, goals, learning, ideas, recipes
- For personal knowledge and life management
- Templates for personal notes and goal tracking

### Custom Initialization

```bash
# Initialize with default settings
metis config knowledge init

# Initialize with custom directory
metis config knowledge init --directory my_knowledge
```

## Managing Knowledge Entries

### Adding Entries

**Basic Entry**
```bash
metis config knowledge add "Title" "Content goes here"
```

**Entry with Category and Tags**
```bash
metis config knowledge add "FastAPI Framework" \
  "FastAPI is a modern, fast web framework for building APIs with Python 3.7+" \
  --category web-development \
  --tags python,fastapi,api,web
```

**Multi-line Content**
```bash
metis config knowledge add "Database Indexing" \
  "Database indexes improve query performance but can slow down write operations. 
  Use them strategically on frequently queried columns.
  Consider composite indexes for multi-column queries." \
  --category database \
  --tags performance,sql,optimization
```

### Updating Entries

**Update Content**
```bash
metis config knowledge update kb_abc123 \
  --content "Updated content with new information"
```

**Update Title and Tags**
```bash
metis config knowledge update kb_abc123 \
  --title "New Title" \
  --tags updated,tags,list
```

### Deleting Entries

```bash
metis config knowledge delete kb_abc123
```

The system will ask for confirmation before deleting.

## Searching and Browsing

### Search Knowledge

**Basic Search**
```bash
metis config knowledge search "python web framework"
```

**Search with Filters**
```bash
# Search in specific category
metis config knowledge search "optimization" --category database

# Search with specific tags
metis config knowledge search "performance" --tags sql,optimization

# Search with custom threshold
metis config knowledge search "python" --threshold 0.3
```

### List Entries

**List All Entries**
```bash
metis config knowledge list
```

**List by Category**
```bash
metis config knowledge list --category programming
```

**List by Tags**
```bash
metis config knowledge list --tags python,web
```

## Import and Export

### Import from Files

**Import Single File**
```bash
metis config knowledge import-file README.md \
  --category documentation \
  --tags readme,docs
```

**Import Directory**
```bash
# Import all supported files from directory
metis config knowledge import-directory ./docs \
  --category documentation

# Recursive import with auto-categorization
metis config knowledge import-directory ./project-docs \
  --recursive
```

**Supported File Formats**
- Markdown (.md, .markdown)
- Text files (.txt)
- Files with frontmatter metadata

### Export Knowledge

**Export Single Entry**
```bash
metis config knowledge export kb_abc123 ./exported_entry.md
```

**Export All Entries**
```bash
metis config knowledge export --all ./knowledge_backup/
```

## Configuration

### View Current Status

```bash
metis config knowledge status
```

This shows:
- Knowledge base status (enabled/disabled)
- Storage provider and directory
- Total entries and recent activity
- Performance metrics
- Configuration settings

### Configure Settings

**Adjust Similarity Threshold**
```bash
# Lower threshold = more results, higher threshold = more precise results
metis config knowledge configure --threshold 0.5
```

**Set Maximum Context Entries**
```bash
metis config knowledge configure --max-context 10
```

**Enable/Disable Auto-learning**
```bash
metis config knowledge configure --auto-learning
metis config knowledge configure --no-auto-learning
```

## Categories and Tags

### View Available Categories

```bash
metis config knowledge categories
```

### View All Tags

```bash
metis config knowledge tags
```

### Category Guidelines

**Programming**
- Code snippets and examples
- Language-specific best practices
- Framework documentation
- Technical tutorials

**Web Development**
- Frontend frameworks and libraries
- Backend technologies
- API documentation
- Deployment guides

**Database**
- Query optimization techniques
- Schema design patterns
- Database-specific features
- Performance tuning

**DevOps**
- Deployment procedures
- Infrastructure as code
- Monitoring and logging
- CI/CD pipelines

### Tagging Best Practices

- Use lowercase tags
- Separate words with hyphens (e.g., "best-practices")
- Be specific but not overly granular
- Use consistent naming conventions
- Include technology names, concepts, and difficulty levels

## Best Practices

### Content Organization

**Use Descriptive Titles**
```bash
# Good
metis config knowledge add "React Hooks Best Practices" "..."

# Avoid
metis config knowledge add "React stuff" "..."
```

**Write Clear, Concise Content**
- Focus on key information
- Use bullet points for lists
- Include examples when helpful
- Keep entries focused on single topics

**Consistent Categorization**
- Use existing categories when possible
- Create new categories sparingly
- Follow naming conventions
- Group related concepts together

### Knowledge Base Maintenance

**Regular Reviews**
- Periodically review and update entries
- Remove outdated information
- Consolidate duplicate entries
- Improve unclear content

**Import Strategy**
- Import existing documentation systematically
- Use consistent categorization during imports
- Review auto-categorized entries
- Clean up imported content formatting

### Search Optimization

**Effective Search Terms**
- Use specific keywords
- Include technology names
- Try different phrasings
- Adjust threshold for better results

**Understanding Relevance Scores**
- Scores range from 0.0 to 1.0
- Higher scores indicate better matches
- Threshold of 0.3+ typically provides good results
- Lower thresholds return more results but may be less relevant

## Command Reference

### Core Commands

| Command | Description | Example |
|---------|-------------|---------|
| `init` | Initialize knowledge base | `metis config knowledge init --preset coding` |
| `status` | Show system status | `metis config knowledge status` |
| `add` | Add new entry | `metis config knowledge add "Title" "Content"` |
| `update` | Update existing entry | `metis config knowledge update kb_123 --title "New Title"` |
| `delete` | Delete entry | `metis config knowledge delete kb_123` |
| `search` | Search entries | `metis config knowledge search "python"` |
| `list` | List entries | `metis config knowledge list --category programming` |

### Import/Export Commands

| Command | Description | Example |
|---------|-------------|---------|
| `import-file` | Import single file | `metis config knowledge import-file doc.md --category docs` |
| `import-directory` | Import directory | `metis config knowledge import-directory ./docs --recursive` |
| `export` | Export entries | `metis config knowledge export kb_123 ./output.md` |

### Utility Commands

| Command | Description | Example |
|---------|-------------|---------|
| `categories` | List categories | `metis config knowledge categories` |
| `tags` | List all tags | `metis config knowledge tags` |
| `configure` | Update settings | `metis config knowledge configure --threshold 0.5` |

### Common Options

| Option | Description | Available Commands |
|--------|-------------|-------------------|
| `--category` | Specify category | `add`, `search`, `list`, `import-file`, `import-directory` |
| `--tags` | Specify tags | `add`, `update`, `search`, `list`, `import-file`, `import-directory` |
| `--threshold` | Set similarity threshold | `search`, `configure` |
| `--recursive` | Include subdirectories | `import-directory` |
| `--max-context` | Maximum context entries | `configure` |

## Integration with Chat

Once you have knowledge entries, the Metis Agent automatically uses them during conversations:

**Knowledge-First Processing**
1. Agent analyzes your question
2. Searches knowledge base for relevant entries
3. If high-relevance entries found (score >= 0.3), provides direct answer
4. If no relevant knowledge, falls back to tool execution

**Example Interaction**
```bash
$ metis chat "What are the main components of FastAPI?"

# Agent finds relevant knowledge entry and responds immediately:
# "FastAPI is a modern, fast web framework for building APIs with Python 3.7+..."
```

**Benefits**
- Instant responses for known topics
- Consistent, accurate information
- Reduced API costs
- Personalized knowledge base

## Troubleshooting

### Common Issues

**No Search Results**
- Try lowering the similarity threshold
- Use different search terms
- Check spelling and terminology
- Verify entries exist with `list` command

**Import Failures**
- Check file permissions
- Verify file formats are supported
- Ensure files contain readable text
- Check for encoding issues

**Performance Issues**
- Reduce similarity threshold for faster searches
- Limit max context entries
- Clean up duplicate or unused entries
- Monitor knowledge base size

### Getting Help

For additional help and support:
- Check the knowledge base status: `metis config knowledge status`
- Review recent entries: `metis config knowledge list`
- Search for existing solutions in your knowledge base
- Consult the main Metis Agent documentation

## Advanced Usage

### Batch Operations

**Bulk Import with Scripting**
```bash
#!/bin/bash
for file in ./docs/*.md; do
    metis config knowledge import-file "$file" --category documentation
done
```

**Export Backup**
```bash
# Create timestamped backup
backup_dir="knowledge_backup_$(date +%Y%m%d_%H%M%S)"
metis config knowledge export --all "./$backup_dir/"
```

### Integration Patterns

**Development Workflow**
1. Import project documentation during setup
2. Add code snippets and solutions as you work
3. Tag entries with project names and technologies
4. Export knowledge when switching projects

**Learning and Research**
1. Create entries for new concepts as you learn
2. Link related entries through consistent tagging
3. Regular review and consolidation sessions
4. Export summaries for sharing or backup

This knowledge base system transforms your Metis Agent into a personalized, intelligent assistant that grows smarter with every entry you add.
