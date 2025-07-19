"""
Custom Tool Template

This template provides a starting point for creating custom tools for the Metis Agent framework.
"""
import os
import requests
from typing import Dict, Any, Optional, List
from metis_agent import SingleAgent, BaseTool, register_tool

class CustomAPITool(BaseTool):
    """Template for a custom tool that interacts with an external API."""
    
    name = "custom_api_tool"
    description = "A custom tool that interacts with an external API"
    
    def __init__(self, api_key=None, api_url=None):
        """Initialize the custom API tool."""
        self.api_key = api_key or os.environ.get("CUSTOM_API_KEY")
        self.api_url = api_url or "https://api.example.com"
        
    def can_handle(self, task):
        """Determine if this tool can handle the task."""
        # Define keywords that indicate this tool should be used
        keywords = [
            "custom api", "external api", "api request", 
            "fetch data", "get information", "api call"
        ]
        return any(keyword in task.lower() for keyword in keywords)
        
    def execute(self, task):
        """Execute the task using the external API."""
        # Extract parameters from the task
        params = self._extract_parameters(task)
        
        # Make the API request
        try:
            response = self._make_api_request(params)
            return self._format_response(response)
        except Exception as e:
            return f"Error executing API request: {str(e)}"
    
    def _extract_parameters(self, task):
        """Extract parameters from the task description."""
        # This is a simplified implementation
        # In a real tool, you would use more sophisticated parsing
        params = {}
        
        # Example: Extract a query parameter
        if "query:" in task.lower():
            query_part = task.lower().split("query:")[1].strip()
            query = query_part.split()[0]
            params["query"] = query
            
        # Example: Extract a limit parameter
        if "limit:" in task.lower():
            limit_part = task.lower().split("limit:")[1].strip()
            try:
                limit = int(limit_part.split()[0])
                params["limit"] = limit
            except ValueError:
                pass
                
        return params
    
    def _make_api_request(self, params):
        """Make a request to the external API."""
        # In a real implementation, you would make an actual API request
        # This is a mock implementation for demonstration purposes
        
        if not self.api_key:
            return {"error": "API key not provided"}
            
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # Mock API response
        mock_response = {
            "status": "success",
            "data": {
                "items": [
                    {"id": 1, "name": "Item 1", "description": "Description of Item 1"},
                    {"id": 2, "name": "Item 2", "description": "Description of Item 2"},
                    {"id": 3, "name": "Item 3", "description": "Description of Item 3"}
                ],
                "total": 3,
                "query": params.get("query", ""),
                "limit": params.get("limit", 10)
            }
        }
        
        # Uncomment to make a real API request
        # response = requests.get(f"{self.api_url}/endpoint", headers=headers, params=params)
        # return response.json()
        
        return mock_response
    
    def _format_response(self, response):
        """Format the API response for the user."""
        if "error" in response:
            return f"Error: {response['error']}"
            
        if response["status"] != "success":
            return f"API request failed with status: {response['status']}"
            
        data = response["data"]
        items = data["items"]
        
        result = "# API Response\n\n"
        result += f"Query: {data.get('query', 'None')}\n"
        result += f"Total items: {data['total']}\n\n"
        
        result += "## Items\n\n"
        for item in items:
            result += f"### {item['name']}\n"
            result += f"ID: {item['id']}\n"
            result += f"Description: {item['description']}\n\n"
            
        return result


class CustomDataProcessingTool(BaseTool):
    """Template for a custom tool that processes data."""
    
    name = "custom_data_processing_tool"
    description = "A custom tool that processes data"
    
    def can_handle(self, task):
        """Determine if this tool can handle the task."""
        # Define keywords that indicate this tool should be used
        keywords = [
            "process data", "analyze data", "data processing",
            "data analysis", "transform data", "data transformation"
        ]
        return any(keyword in task.lower() for keyword in keywords)
        
    def execute(self, task):
        """Execute the data processing task."""
        # Extract data from the task
        data = self._extract_data(task)
        
        # Process the data
        try:
            processed_data = self._process_data(data)
            return self._format_results(processed_data)
        except Exception as e:
            return f"Error processing data: {str(e)}"
    
    def _extract_data(self, task):
        """Extract data from the task description."""
        # This is a simplified implementation
        # In a real tool, you would use more sophisticated parsing
        
        # Example: Extract data between triple backticks
        import re
        data_match = re.search(r'```(.*?)```', task, re.DOTALL)
        
        if data_match:
            data_str = data_match.group(1).strip()
            try:
                # Try to parse as JSON
                import json
                return json.loads(data_str)
            except json.JSONDecodeError:
                # If not JSON, return as string
                return data_str
                
        # If no data found, return empty dict
        return {}
    
    def _process_data(self, data):
        """Process the data."""
        # This is a simplified implementation
        # In a real tool, you would implement your data processing logic
        
        # Example: If data is a dict, add a "processed" flag
        if isinstance(data, dict):
            processed_data = data.copy()
            processed_data["processed"] = True
            return processed_data
            
        # Example: If data is a string, count words and characters
        if isinstance(data, str):
            words = data.split()
            return {
                "original_text": data,
                "word_count": len(words),
                "character_count": len(data),
                "processed": True
            }
            
        # Default: Return data unchanged
        return data
    
    def _format_results(self, processed_data):
        """Format the processing results for the user."""
        if isinstance(processed_data, dict):
            result = "# Data Processing Results\n\n"
            
            for key, value in processed_data.items():
                result += f"**{key}**: {value}\n"
                
            return result
            
        return f"Processed data: {processed_data}"


def create_custom_agent(api_key=None, use_titans_memory=True):
    """Create an agent with custom tools."""
    # Register the custom tools
    register_tool("custom_api_tool", CustomAPITool)
    register_tool("custom_data_processing_tool", CustomDataProcessingTool)
    
    # Create the agent
    agent = SingleAgent(
        use_titans_memory=use_titans_memory,
        llm_provider="openai",
        llm_model="gpt-4o"
    )
    
    # Set API keys if provided
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    
    return agent


def main():
    """Run a demonstration of the custom tools."""
    # Get API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    
    # Create an agent with custom tools
    agent = create_custom_agent(api_key=api_key)
    
    # Define a session ID
    session_id = "custom_tool_session"
    
    # Test the custom API tool
    api_query = "Make a custom API request with query: products and limit: 5"
    print(f"Custom API Tool Query: {api_query}")
    
    api_response = agent.process_query(
        api_query,
        session_id=session_id,
        tool_name="custom_api_tool"
    )
    print(f"API Response:\n{api_response}")
    
    # Test the custom data processing tool
    data_query = "Process the following data:\n```\n{\"name\": \"Example\", \"values\": [1, 2, 3, 4, 5]}\n```"
    print(f"\nCustom Data Processing Tool Query: {data_query}")
    
    data_response = agent.process_query(
        data_query,
        session_id=session_id,
        tool_name="custom_data_processing_tool"
    )
    print(f"Data Processing Response:\n{data_response}")

if __name__ == "__main__":
    main()