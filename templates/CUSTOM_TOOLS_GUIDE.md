# Custom Tools Development Guide - Metis Agent v0.6.0

## Overview

The Metis Agent Framework v0.6.0 allows users to create and register custom tools to extend agent capabilities for specific use cases. This guide demonstrates how to build, register, and integrate custom tools with your agents using the latest v0.6.0 architecture.

**New in v0.6.0:**
- Enhanced BaseTool with performance monitoring
- ComposableTool for tool chaining and pipelines
- Advanced capability metadata system
- Query analysis and compatibility scoring
- Resource monitoring and optimization

## Table of Contents

1. [Custom Tool Architecture](#custom-tool-architecture)
2. [v0.6.0 Enhanced Features](#v060-enhanced-features)
3. [Creating Custom Tools](#creating-custom-tools)
4. [Tool Registration](#tool-registration)
5. [Agent Integration](#agent-integration)
6. [Advanced Features](#advanced-features)
7. [Performance Monitoring](#performance-monitoring)
8. [Best Practices](#best-practices)
9. [Examples](#examples)

## Custom Tool Architecture

### Base Tool Structure

All custom tools must inherit from `BaseTool` and implement the required methods:

```python
from metis_agent.tools.base import BaseTool
from typing import Dict, Any

class MyCustomTool(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "MyCustomTool"
        self.description = "Description of what this tool does"
        self.version = "1.0.0"
    
    def can_handle(self, task: str) -> bool:
        """Check if this tool can handle the given task"""
        # Implementation here
        pass
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        """Execute the tool's functionality"""
        # Implementation here
        pass
    
    def get_capabilities(self) -> Dict[str, Any]:
        """Return tool capabilities metadata (v0.6.0 feature)"""
        return {
            "complexity_levels": ["simple", "moderate", "complex"],
            "input_types": ["text"],
            "output_types": ["structured_data"],
            "requires_internet": False,
            "requires_filesystem": False,
            "concurrent_safe": True,
            "resource_intensive": False,
            "supported_intents": [],
            "api_dependencies": []
        }
```

## v0.6.0 Enhanced Features

### Performance Monitoring

v0.6.0 introduces built-in performance monitoring for all tools:

```python
class MyTool(BaseTool):
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        # Use execute_with_monitoring for automatic performance tracking
        return self.execute_with_monitoring(task, **kwargs)
    
    def _actual_execute(self, task: str, **kwargs) -> Dict[str, Any]:
        # Your actual implementation here
        return {"success": True, "data": "result"}
```

### Capability Metadata System

Tools can now declare their capabilities for intelligent routing:

```python
def get_capabilities(self) -> Dict[str, Any]:
    return {
        "complexity_levels": ["simple", "moderate", "complex"],
        "input_types": ["text", "json", "file"],
        "output_types": ["structured_data", "file", "visualization"],
        "estimated_execution_time": "1-5s",
        "requires_internet": True,
        "requires_filesystem": False,
        "concurrent_safe": True,
        "resource_intensive": False,
        "supported_intents": ["data_analysis", "visualization"],
        "api_dependencies": ["openai", "groq"],
        "memory_usage": "medium"
    }
```

### ComposableTool for Advanced Workflows

Inherit from `ComposableTool` for tools that can be chained:

```python
from metis_agent.tools.base import ComposableTool

class ChainableTool(ComposableTool):
    def get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "data": {"type": "array"},
                "operation": {"type": "string"}
            },
            "required": ["data"]
        }
    
    def get_output_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "success": {"type": "boolean"},
                "processed_data": {"type": "array"},
                "metadata": {"type": "object"}
            },
            "required": ["success", "processed_data"]
        }
```

### Required Methods

1. **`can_handle(task: str) -> bool`**
   - Determines if the tool can handle a specific task
   - Should return `True` if the tool is suitable for the task
   - Use keyword matching, pattern recognition, or NLP

2. **`execute(task: str, **kwargs) -> Any`**
   - Executes the tool's main functionality
   - Can return any type, but Dict[str, Any] is recommended for consistency
   - Should include error handling and meaningful responses
   - In v0.6.0, consider using `execute_with_monitoring()` for performance tracking

### Response Format

Tools should return standardized responses:

```python
# Success response
{
    "success": True,
    "data": {...},  # Tool-specific data
    "tool_used": self.name,
    "metadata": {...}  # Optional metadata
}

# Error response
{
    "success": False,
    "error": "Error description",
    "tool_used": self.name,
    "suggestion": "How to fix the issue"  # Optional
}
```

## Creating Custom Tools

### Example 1: Simple Calculator Tool

```python
class CalculatorTool(BaseTool):
    def __init__(self):
        super().__init__()
        self.name = "CalculatorTool"
        self.description = "Perform mathematical calculations"
        self.version = "1.0.0"
    
    def can_handle(self, task: str) -> bool:
        math_keywords = ['calculate', 'compute', 'math', '+', '-', '*', '/', 'sum']
        return any(keyword in task.lower() for keyword in math_keywords)
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        try:
            # Extract mathematical expression
            expression = self._extract_expression(task)
            result = eval(expression)  # Note: Use safe evaluation in production
            
            return {
                "success": True,
                "data": {
                    "expression": expression,
                    "result": result
                },
                "tool_used": self.name
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Calculation failed: {str(e)}",
                "tool_used": self.name
            }
    
    def _extract_expression(self, task: str) -> str:
        # Implementation to extract math expression from natural language
        # This is simplified - use proper parsing in production
        import re
        pattern = r'[\d+\-*/().\s]+'
        matches = re.findall(pattern, task)
        return ''.join(matches).strip() if matches else task
```

### Example 2: API Integration Tool

```python
import requests

class APITool(BaseTool):
    def __init__(self, base_url: str, api_key: str = None):
        super().__init__()
        self.name = "APITool"
        self.description = "Integrate with external APIs"
        self.version = "1.0.0"
        self.base_url = base_url
        self.api_key = api_key
    
    def can_handle(self, task: str) -> bool:
        api_keywords = ['api', 'request', 'fetch', 'get data', 'endpoint']
        return any(keyword in task.lower() for keyword in api_keywords)
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        try:
            # Parse endpoint and method from task
            endpoint = kwargs.get('endpoint', '/api/data')
            method = kwargs.get('method', 'GET')
            
            # Make API request
            headers = {'Authorization': f'Bearer {self.api_key}'} if self.api_key else {}
            response = requests.request(
                method=method,
                url=f"{self.base_url}{endpoint}",
                headers=headers,
                timeout=30
            )
            
            return {
                "success": True,
                "data": {
                    "status_code": response.status_code,
                    "response": response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text,
                    "headers": dict(response.headers)
                },
                "tool_used": self.name
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"API request failed: {str(e)}",
                "tool_used": self.name
            }
```

### Example 3: Database Tool

```python
import sqlite3
from typing import List, Tuple

class DatabaseTool(BaseTool):
    def __init__(self, db_path: str):
        super().__init__()
        self.name = "DatabaseTool"
        self.description = "Execute database operations"
        self.version = "1.0.0"
        self.db_path = db_path
    
    def can_handle(self, task: str) -> bool:
        db_keywords = ['database', 'query', 'sql', 'select', 'insert', 'update', 'delete']
        return any(keyword in task.lower() for keyword in db_keywords)
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        try:
            query = kwargs.get('query') or self._parse_query(task)
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                
                if query.strip().upper().startswith('SELECT'):
                    results = cursor.fetchall()
                    columns = [description[0] for description in cursor.description]
                    data = [dict(zip(columns, row)) for row in results]
                else:
                    conn.commit()
                    data = {"rows_affected": cursor.rowcount}
                
                return {
                    "success": True,
                    "data": data,
                    "query": query,
                    "tool_used": self.name
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Database operation failed: {str(e)}",
                "tool_used": self.name
            }
    
    def _parse_query(self, task: str) -> str:
        # Simple query parsing - enhance with NLP in production
        if 'select' in task.lower():
            return "SELECT * FROM users LIMIT 10"  # Default query
        return task  # Return task as-is for now
```

## Tool Registration

### Custom Tool Registry

Create a registry to manage your custom tools:

```python
class CustomToolRegistry:
    def __init__(self):
        self.tools = {}
        self.tool_instances = {}
    
    def register_tool(self, tool_class, tool_config: Dict[str, Any] = None):
        """Register a custom tool"""
        tool_instance = tool_class(**(tool_config or {}))
        self.tools[tool_instance.name] = tool_class
        self.tool_instances[tool_instance.name] = tool_instance
        print(f"+ Registered custom tool: {tool_instance.name}")
    
    def get_tool(self, tool_name: str) -> Optional[BaseTool]:
        """Get a tool instance by name"""
        return self.tool_instances.get(tool_name)
    
    def list_tools(self) -> List[str]:
        """List all registered tools"""
        return list(self.tools.keys())
```

### Registration Example

```python
# Create registry
registry = CustomToolRegistry()

# Register tools with configurations
registry.register_tool(CalculatorTool)
registry.register_tool(APITool, {
    "base_url": "https://api.example.com",
    "api_key": "your-api-key"
})
registry.register_tool(DatabaseTool, {
    "db_path": "/path/to/database.db"
})
```

## Agent Integration

### Integrating Custom Tools with Agents

```python
def integrate_custom_tools(agent: SingleAgent, registry: CustomToolRegistry):
    """Integrate custom tools with an agent"""
    for tool_name, tool_instance in registry.tool_instances.items():
        # Add tool to agent's tool registry
        if hasattr(agent, 'tool_registry'):
            agent.tool_registry.tools[tool_name] = tool_instance
        print(f"+ Integrated {tool_name} with agent")

# Usage
agent = SingleAgent(config=config)
registry = CustomToolRegistry()
registry.register_tool(MyCustomTool)
integrate_custom_tools(agent, registry)
```

### Complete Integration Example

```python
def create_specialized_agent():
    """Create an agent with custom tools"""
    
    # 1. Create tool registry
    registry = CustomToolRegistry()
    
    # 2. Register custom tools
    registry.register_tool(CalculatorTool)
    registry.register_tool(APITool, {"base_url": "https://api.myservice.com"})
    registry.register_tool(DatabaseTool, {"db_path": "my_database.db"})
    
    # 3. Create agent
    config = AgentConfig()
    config.set_llm_provider('groq')
    agent = SingleAgent(config=config)
    
    # 4. Customize agent
    agent.config.update_name("SpecializedAgent")
    agent.config.update_custom_system_message(
        "You are a specialized agent with custom tools for calculations, API integration, and database operations."
    )
    
    # 5. Integrate tools
    integrate_custom_tools(agent, registry)
    
    return agent, registry
```

## Advanced Features

### Tool Chaining

Create tools that can use other tools:

```python
class WorkflowTool(BaseTool):
    def __init__(self, tool_registry):
        super().__init__()
        self.name = "WorkflowTool"
        self.description = "Execute multi-step workflows"
        self.registry = tool_registry
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        steps = []
        
        # Step 1: Use calculator
        calc_tool = self.registry.get_tool("CalculatorTool")
        if calc_tool:
            result1 = calc_tool.execute("calculate 10 + 5")
            steps.append(result1)
        
        # Step 2: Store in database
        db_tool = self.registry.get_tool("DatabaseTool")
        if db_tool:
            result2 = db_tool.execute("insert calculation result")
            steps.append(result2)
        
        return {
            "success": True,
            "workflow_steps": steps,
            "tool_used": self.name
        }
```

### Configurable Tools

Create tools with flexible configurations:

```python
class ConfigurableTool(BaseTool):
    def __init__(self, config: Dict[str, Any]):
        super().__init__()
        self.name = config.get('name', 'ConfigurableTool')
        self.description = config.get('description', 'A configurable tool')
        self.settings = config.get('settings', {})
        self.endpoints = config.get('endpoints', [])
    
    def can_handle(self, task: str) -> bool:
        keywords = self.settings.get('keywords', [])
        return any(keyword in task.lower() for keyword in keywords)
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        # Use self.settings and self.endpoints for execution
        pass
```

## Performance Monitoring

### v0.6.0 Built-in Monitoring

v0.6.0 provides automatic performance monitoring for all tools:

```python
class MonitoredTool(BaseTool):
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        # This automatically tracks execution time, memory usage, and API calls
        return self.execute_with_monitoring(task, **kwargs)
    
    def _actual_execute(self, task: str, **kwargs) -> Dict[str, Any]:
        # Your implementation here - monitoring is handled automatically
        return {
            "success": True,
            "data": "processed result",
            "tool_used": self.name
        }
```

### Custom Performance Metrics

Override monitoring methods for custom metrics:

```python
class CustomMetricsTool(BaseTool):
    def __init__(self):
        super().__init__()
        self.api_calls = 0
    
    def _get_api_call_count(self) -> int:
        """Override to track API calls"""
        return self.api_calls
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        self.api_calls += 1  # Track API usage
        return self.execute_with_monitoring(task, **kwargs)
```

### Resource Requirements

Declare resource requirements in capabilities:

```python
def get_capabilities(self) -> Dict[str, Any]:
    return {
        "memory_usage": "high",  # low, medium, high
        "resource_intensive": True,
        "estimated_execution_time": "10-30s",
        "concurrent_safe": False,  # Can't run multiple instances
        "requires_internet": True,
        "api_dependencies": ["openai", "anthropic"]
    }
```

## Best Practices

### 1. Error Handling

Always implement comprehensive error handling:

```python
def execute(self, task: str, **kwargs) -> Dict[str, Any]:
    try:
        # Tool logic here
        result = self._perform_operation(task)
        return {
            "success": True,
            "data": result,
            "tool_used": self.name
        }
    except ValueError as e:
        return {
            "success": False,
            "error": f"Invalid input: {str(e)}",
            "tool_used": self.name,
            "suggestion": "Please check your input format"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}",
            "tool_used": self.name
        }
```

### 2. Input Validation

Validate inputs before processing:

```python
def execute(self, task: str, **kwargs) -> Dict[str, Any]:
    # Validate required parameters
    if not task or not task.strip():
        return {
            "success": False,
            "error": "Task cannot be empty",
            "tool_used": self.name
        }
    
    # Validate specific requirements
    if len(task) > 1000:
        return {
            "success": False,
            "error": "Task description too long (max 1000 characters)",
            "tool_used": self.name
        }
    
    # Continue with execution
```

### 3. Logging and Monitoring

Add logging for debugging and monitoring:

```python
import logging

class MyTool(BaseTool):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        self.logger.info(f"Executing task: {task[:100]}...")
        
        try:
            result = self._perform_operation(task)
            self.logger.info("Task completed successfully")
            return {"success": True, "data": result, "tool_used": self.name}
        except Exception as e:
            self.logger.error(f"Task failed: {str(e)}")
            return {"success": False, "error": str(e), "tool_used": self.name}
```

### 4. Performance Optimization

Optimize for performance:

```python
class OptimizedTool(BaseTool):
    def __init__(self):
        super().__init__()
        self._cache = {}  # Simple caching
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        # Check cache first
        cache_key = hash(task)
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        # Perform operation
        result = self._perform_operation(task)
        
        # Cache result
        self._cache[cache_key] = result
        
        return result
```

## Testing Custom Tools

### Unit Testing

Create comprehensive tests for your tools:

```python
import unittest

class TestMyCustomTool(unittest.TestCase):
    def setUp(self):
        self.tool = MyCustomTool()
    
    def test_can_handle_valid_task(self):
        self.assertTrue(self.tool.can_handle("valid task description"))
    
    def test_can_handle_invalid_task(self):
        self.assertFalse(self.tool.can_handle("unrelated task"))
    
    def test_execute_success(self):
        result = self.tool.execute("valid task")
        self.assertTrue(result["success"])
        self.assertIn("data", result)
    
    def test_execute_error_handling(self):
        result = self.tool.execute("")  # Empty task
        self.assertFalse(result["success"])
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()
```

## Complete Example

See `custom_tools_template.py` for a complete working example that demonstrates:

- Multiple custom tool types (Weather, Database, API)
- Tool registration and integration with v0.6.0 features
- Agent configuration with enhanced memory and multi-provider LLM support
- Advanced workflow tools and tool chaining
- Performance monitoring and capability metadata
- Error handling and validation
- Environment loading and API key management
- Testing and usage examples

## Next Steps

1. **Identify Your Use Case**: Determine what specific functionality you need
2. **Design Your Tool**: Plan the interface and functionality
3. **Implement Following v0.6.0 Standards**: Use the BaseTool or ComposableTool interface
4. **Add Capability Metadata**: Define your tool's capabilities for intelligent routing
5. **Implement Performance Monitoring**: Use execute_with_monitoring for tracking
6. **Test Thoroughly**: Create comprehensive tests including performance tests
7. **Integrate with Agent**: Register and configure with your agent
8. **Monitor and Iterate**: Track usage, performance, and improve over time

## Support

For questions or issues with custom tool development:

1. Check the examples in `custom_tools_template.py`
2. Review the base tool implementation
3. Test with simple tools first before building complex ones
4. Follow the error handling and validation patterns shown

Custom tools are a powerful way to extend Metis Agent v0.6.0 capabilities for your specific needs!

**v0.6.0 brings enhanced capabilities:**
- Performance monitoring and optimization
- Advanced tool chaining and composition
- Intelligent routing based on capability metadata
- Resource management and monitoring
- Integration with 36+ built-in tools
