"""
Custom Tool Example

This example demonstrates how to create and use custom tools with Metis Agent.
"""
import os
import json
import requests
from metis_agent import SingleAgent, BaseTool, register_tool

class WeatherTool(BaseTool):
    """Custom tool for getting weather information."""
    
    name = "weather_tool"
    description = "Gets weather information for a location"
    
    def __init__(self, api_key=None):
        """Initialize the weather tool."""
        self.api_key = api_key or os.environ.get("WEATHER_API_KEY", "demo_key")
        
    def can_handle(self, task):
        """Determine if this tool can handle the task."""
        keywords = ["weather", "temperature", "forecast", "rain", "sunny", "climate"]
        return any(keyword in task.lower() for keyword in keywords)
        
    def execute(self, task):
        """Execute the weather task."""
        # Extract location from task
        # This is a simplified example - in a real tool, you'd use NLP or the LLM to extract entities
        location = self._extract_location(task)
        
        if not location:
            return "I couldn't determine the location. Please specify a city or location."
        
        # In a real implementation, you would call a weather API
        # For this example, we'll return mock data
        weather_data = self._get_mock_weather(location)
        
        return f"Weather for {location}:\n" + \
               f"Temperature: {weather_data['temperature']}°C\n" + \
               f"Condition: {weather_data['condition']}\n" + \
               f"Humidity: {weather_data['humidity']}%\n" + \
               f"Wind: {weather_data['wind']} km/h"
    
    def _extract_location(self, task):
        """Extract location from task description."""
        # This is a simplified implementation
        # In a real tool, you would use NLP or the LLM to extract entities
        task_lower = task.lower()
        
        # Look for common patterns
        if "in " in task_lower:
            parts = task_lower.split("in ")
            if len(parts) > 1:
                location_part = parts[1].strip()
                return location_part.split()[0].capitalize()
        
        if "for " in task_lower:
            parts = task_lower.split("for ")
            if len(parts) > 1:
                location_part = parts[1].strip()
                return location_part.split()[0].capitalize()
        
        # Default location if we can't extract one
        return "New York"
    
    def _get_mock_weather(self, location):
        """Get mock weather data for demonstration purposes."""
        # In a real implementation, you would call a weather API
        mock_data = {
            "New York": {"temperature": 22, "condition": "Partly Cloudy", "humidity": 65, "wind": 12},
            "London": {"temperature": 18, "condition": "Rainy", "humidity": 80, "wind": 15},
            "Tokyo": {"temperature": 26, "condition": "Sunny", "humidity": 70, "wind": 8},
            "Paris": {"temperature": 24, "condition": "Clear", "humidity": 60, "wind": 10},
            "Sydney": {"temperature": 28, "condition": "Sunny", "humidity": 55, "wind": 14}
        }
        
        return mock_data.get(location, {"temperature": 20, "condition": "Unknown", "humidity": 60, "wind": 10})


class StockPriceTool(BaseTool):
    """Custom tool for getting stock price information."""
    
    name = "stock_price_tool"
    description = "Gets current stock price information"
    
    def can_handle(self, task):
        """Determine if this tool can handle the task."""
        keywords = ["stock", "price", "market", "shares", "ticker", "stock price"]
        return any(keyword in task.lower() for keyword in keywords)
        
    def execute(self, task):
        """Execute the stock price task."""
        # Extract ticker symbol from task
        ticker = self._extract_ticker(task)
        
        if not ticker:
            return "I couldn't determine the stock ticker. Please specify a company or ticker symbol."
        
        # In a real implementation, you would call a stock API
        # For this example, we'll return mock data
        stock_data = self._get_mock_stock_data(ticker)
        
        return f"Stock information for {ticker} ({stock_data['name']}):\n" + \
               f"Current Price: ${stock_data['price']}\n" + \
               f"Change: {stock_data['change']}%\n" + \
               f"Volume: {stock_data['volume']}"
    
    def _extract_ticker(self, task):
        """Extract ticker symbol from task description."""
        # This is a simplified implementation
        task_lower = task.lower()
        
        common_tickers = {
            "apple": "AAPL",
            "microsoft": "MSFT",
            "google": "GOOGL",
            "amazon": "AMZN",
            "tesla": "TSLA",
            "facebook": "META",
            "netflix": "NFLX"
        }
        
        for company, ticker in common_tickers.items():
            if company in task_lower:
                return ticker
                
        # Look for ticker patterns (all caps 1-5 letters)
        words = task_lower.split()
        for word in words:
            word = word.strip(",.?!:;()")
            if word.isupper() and 1 <= len(word) <= 5:
                return word
        
        # Default ticker if we can't extract one
        return "AAPL"
    
    def _get_mock_stock_data(self, ticker):
        """Get mock stock data for demonstration purposes."""
        # In a real implementation, you would call a stock API
        mock_data = {
            "AAPL": {"name": "Apple Inc.", "price": 182.63, "change": 0.85, "volume": "32.5M"},
            "MSFT": {"name": "Microsoft Corporation", "price": 415.28, "change": 1.2, "volume": "22.1M"},
            "GOOGL": {"name": "Alphabet Inc.", "price": 142.89, "change": -0.3, "volume": "18.7M"},
            "AMZN": {"name": "Amazon.com Inc.", "price": 178.12, "change": 0.5, "volume": "25.3M"},
            "TSLA": {"name": "Tesla, Inc.", "price": 215.76, "change": -1.8, "volume": "40.2M"}
        }
        
        return mock_data.get(ticker, {"name": "Unknown Company", "price": 100.00, "change": 0.0, "volume": "0"})


def main():
    """Run the custom tool example."""
    # Register our custom tools
    register_tool("weather_tool", WeatherTool)
    register_tool("stock_price_tool", StockPriceTool)
    
    # Create an agent
    agent = SingleAgent()
    
    # Process weather queries
    print("\n=== Weather Tool Example ===")
    weather_query = "What's the weather like in Tokyo today?"
    print(f"Query: {weather_query}")
    
    response = agent.process_query(weather_query)
    print(f"Response:\n{response}")
    
    # Process stock queries
    print("\n=== Stock Price Tool Example ===")
    stock_query = "What's the current stock price of AAPL?"
    print(f"Query: {stock_query}")
    
    response = agent.process_query(stock_query)
    print(f"Response:\n{response}")
    
    # Process a query that doesn't match any custom tool
    print("\n=== Default Behavior Example ===")
    general_query = "What is the capital of France?"
    print(f"Query: {general_query}")
    
    response = agent.process_query(general_query)
    print(f"Response:\n{response}")
    
    print("\nCustom tool example completed!")

if __name__ == "__main__":
    main()