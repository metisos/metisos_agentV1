#!/usr/bin/env python3
"""
Clean Metis Agent Web App Template

This template demonstrates how to create a web-based chat interface using Flask
with the Metis Agent framework. This is a clean, public-ready template that users
can customize for their own agents.

Usage:
    1. Set your API keys in .env.local file
    2. Customize the agent personality below
    3. Run: python clean_web_app_template.py
    4. Visit: http://localhost:5000

Features:
    - Custom agent personality
    - Session-based memory
    - Tool integration
    - Clean, customizable interface
"""

from flask import Flask, render_template, render_template_string, request, jsonify, session
from flask_cors import CORS
from metis_agent import SingleAgent
import os
import uuid
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env.local'))
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Explicitly set Google API environment variables for tools
google_api_key = os.getenv('GOOGLE_API_KEY')
if google_api_key:
    os.environ['GOOGLE_API_KEY'] = google_api_key
    os.environ['GOOGLE_SEARCH_ENGINE_ID'] = os.getenv('GOOGLE_SEARCH_ENGINE_ID', '53433d9e4d284403e')
    os.environ['GOOGLE_CSE_ID'] = os.getenv('GOOGLE_SEARCH_ENGINE_ID', '53433d9e4d284403e')
    print(f"Google API setup: Key loaded, Engine ID: {os.environ['GOOGLE_SEARCH_ENGINE_ID']}")

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

# Global agent instance
agent = None

def check_api_keys():
    """Check if required API keys are available."""
    llm_keys = ['OPENAI_API_KEY', 'GROQ_API_KEY', 'ANTHROPIC_API_KEY']
    available_llms = []
    
    for key in llm_keys:
        value = os.getenv(key)
        if value and len(value) > 10:  # Basic validation
            available_llms.append(key.replace('_API_KEY', ''))
    
    if not available_llms:
        print("WARNING: No LLM API keys found!")
        print("   Please set at least one of: OPENAI_API_KEY, GROQ_API_KEY, ANTHROPIC_API_KEY")
        print("   Add them to your .env.local file")
        return False
    
    print(f"Available LLM providers: {', '.join(available_llms)}")
    
    # Check optional tool API keys
    tool_keys = {
        'GOOGLE_API_KEY': 'Google Search',
        'FIRECRAWL_API_KEY': 'Web Scraping',
    }
    
    for key, tool_name in tool_keys.items():
        value = os.getenv(key)
        if value and len(value) > 10:
            print(f"{tool_name} API key found")
        else:
            print(f"{tool_name} API key not found (optional)")
    
    return True

def create_custom_agent():
    """
    Create a custom Metis Agent with your own personality and configuration.
    
    This is where you customize your agent:
    - Modify the system message to define personality
    - Enable/disable features
    - Configure memory settings
    """
    
    # Ensure all environment variables are properly set
    api_keys = {
        'GOOGLE_API_KEY': os.getenv('GOOGLE_API_KEY'),
        'FIRECRAWL_API_KEY': os.getenv('FIRECRAWL_API_KEY'),
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'GROQ_API_KEY': os.getenv('GROQ_API_KEY'),
        'GOOGLE_SEARCH_ENGINE_ID': os.getenv('GOOGLE_SEARCH_ENGINE_ID', '53433d9e4d284403e')
    }
    
    for key, value in api_keys.items():
        if value:
            os.environ[key] = value
            if key == 'GOOGLE_SEARCH_ENGINE_ID':
                os.environ['GOOGLE_CSE_ID'] = value  # Alternative name
    
    print(f"Environment setup complete. Google API available: {bool(os.getenv('GOOGLE_API_KEY'))}")
    
    # Step 1: Create agent directly (AgentConfig not available in current version)
    # The SingleAgent will use default configuration with memory enabled
    
    # Step 3: Define your agent's personality and capabilities
    # Customize this system message to create your unique agent!
    custom_personality = """You are a helpful and intelligent AI assistant created with the Metis Agent framework.

## Your Personality
- Be friendly, professional, and engaging
- Provide clear, accurate, and helpful responses
- Show enthusiasm for helping users solve problems
- Be concise but thorough when needed

## Your Capabilities
You have access to various tools and can:
- Search the web for current information
- Perform calculations and data analysis
- Generate and analyze code
- Create content and documents
- Work with files and data
- Conduct research and analysis

## Your Approach
- Always aim to be helpful and accurate
- If you're not sure about something, say so
- Offer to use tools when they would be beneficial
- Explain your reasoning when helpful
- Ask clarifying questions if needed

Remember: You're powered by the Metis Agent framework, which gives you intelligent tool selection and adaptive memory capabilities."""

    # Step 2: Create the agent with default configuration
    agent = SingleAgent()
    
    # Step 5: Configure GoogleSearchTool with parameter injection
    google_api_key = os.getenv('GOOGLE_API_KEY')
    google_engine_id = os.getenv('GOOGLE_SEARCH_ENGINE_ID', '53433d9e4d284403e')
    
    if google_api_key and 'GoogleSearchTool' in agent.tools:
        google_tool = agent.tools['GoogleSearchTool']
        
        # Store original execute method
        original_execute = google_tool.execute
        
        # Create wrapper function that always passes required parameters
        def execute_with_params(query, **kwargs):
            # Always inject the required parameters
            kwargs['google_api_key'] = google_api_key
            kwargs['cx'] = google_engine_id
            print(f"GoogleSearch executing: {query[:50]}... with engine ID: {google_engine_id}")
            return original_execute(query, **kwargs)
        
        # Replace the execute method with our wrapper
        google_tool.execute = execute_with_params
        print(f"GoogleSearchTool configured with API key and engine ID: {google_engine_id}")
    
    # Step 6: Set the custom personality
    agent.set_system_message(custom_personality)
    
    return agent

def initialize_agent():
    """Initialize the Metis Agent."""
    global agent
    
    print("Initializing Metis Agent...")
    
    # Check API keys
    if not check_api_keys():
        print("\nCannot start without LLM API keys. Please check your .env.local file.")
        return False
    
    # Create custom agent
    agent = create_custom_agent()
    
    # Get agent info
    identity = agent.get_agent_identity()
    agent_name = identity.get('agent_name', 'Custom Agent')
    agent_id = identity.get('agent_id', 'unknown')
    
    print(f"Agent initialized: {agent_name} ({agent_id})")
    print(f"Memory enabled: True")
    print(f"Tools available: {len(agent.tools)} tools discovered")
    
    return True

@app.route('/')
def index():
    """
    Main chat interface page.
    """
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Handle chat messages from the web interface.
    """
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        # Get or create session ID
        if 'session_id' not in session:
            session['session_id'] = str(uuid.uuid4())
        
        session_id = session['session_id']
        
        # Process the query with the agent
        agent_response = agent.process_query(user_message, session_id=session_id)
        
        # Extract the response text from the agent's response dictionary
        if isinstance(agent_response, dict) and 'response' in agent_response:
            response_text = agent_response['response']
        else:
            response_text = str(agent_response)
        
        return jsonify({
            'response': response_text,
            'session_id': session_id,
            'agent_name': agent.get_agent_identity().get('agent_name', 'Assistant')
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/agent-info')
def agent_info():
    """
    Get agent identity information.
    """
    try:
        identity = agent.get_agent_identity()
        return jsonify({
            'name': identity.get('agent_name', 'Assistant'),
            'id': identity.get('agent_id', 'unknown'),
            'creation_date': identity.get('creation_timestamp', 'unknown')
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear-session', methods=['POST'])
def clear_session():
    """
    Clear the current chat session.
    """
    try:
        session.pop('session_id', None)
        return jsonify({'message': 'Session cleared'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def create_chat_template():
    """
    Create the HTML template for the chat interface.
    """
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    os.makedirs(template_dir, exist_ok=True)
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metis Agent Chat</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .chat-container {
            width: 90%;
            max-width: 800px;
            height: 80vh;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        
        .chat-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            text-align: center;
        }
        
        .chat-header h1 {
            margin: 0;
            font-size: 24px;
        }
        
        .agent-info {
            font-size: 14px;
            opacity: 0.9;
            margin-top: 5px;
        }
        
        .chat-messages {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            background: #f8f9fa;
        }
        
        .message {
            margin-bottom: 15px;
            display: flex;
            align-items: flex-start;
        }
        
        .message.user {
            justify-content: flex-end;
        }
        
        .message-content {
            max-width: 70%;
            padding: 12px 16px;
            border-radius: 18px;
            word-wrap: break-word;
        }
        
        .message.user .message-content {
            background: #007bff;
            color: white;
        }
        
        .message.agent .message-content {
            background: white;
            border: 1px solid #e0e0e0;
            color: #333;
        }
        
        .chat-input {
            padding: 20px;
            background: white;
            border-top: 1px solid #e0e0e0;
        }
        
        .input-group {
            display: flex;
            gap: 10px;
        }
        
        .message-input {
            flex: 1;
            padding: 12px 16px;
            border: 1px solid #ddd;
            border-radius: 25px;
            outline: none;
            font-size: 16px;
        }
        
        .send-button {
            padding: 12px 24px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            transition: background 0.3s;
        }
        
        .send-button:hover {
            background: #0056b3;
        }
        
        .send-button:disabled {
            background: #ccc;
            cursor: not-allowed;
        }
        
        .clear-button {
            padding: 8px 16px;
            background: #6c757d;
            color: white;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            margin-left: 10px;
        }
        
        .clear-button:hover {
            background: #545b62;
        }
        
        /* Message content formatting */
        .message-content ol {
            margin: 10px 0;
            padding-left: 20px;
        }
        
        .message-content li {
            margin: 5px 0;
            line-height: 1.4;
        }
        
        .message-content strong {
            font-weight: 600;
            color: #2c3e50;
        }
        
        .message-content br {
            line-height: 1.6;
        }
        
        .loading {
            display: none;
            color: #666;
            font-style: italic;
            padding: 10px;
        }
        
        .error {
            color: #dc3545;
            background: #f8d7da;
            padding: 10px;
            border-radius: 10px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h1>Metis Agent Chat</h1>
            <div class="agent-info" id="agent-info">Loading agent info...</div>
        </div>
        
        <div class="chat-messages" id="chat-messages">
            <div class="message agent">
                <div class="message-content">
                    Hello! I'm your Metis AI assistant. How can I help you today?
                </div>
            </div>
        </div>
        
        <div class="chat-input">
            <div class="input-group">
                <input type="text" id="message-input" class="message-input" 
                       placeholder="Type your message here..." maxlength="1000">
                <button id="send-button" class="send-button">Send</button>
                <button id="clear-button" class="clear-button">Clear</button>
            </div>
            <div id="loading" class="loading">Agent is thinking...</div>
        </div>
    </div>

    <script>
        const chatMessages = document.getElementById('chat-messages');
        const messageInput = document.getElementById('message-input');
        const sendButton = document.getElementById('send-button');
        const clearButton = document.getElementById('clear-button');
        const loading = document.getElementById('loading');
        const agentInfo = document.getElementById('agent-info');

        // Load agent info
        fetch('/api/agent-info')
            .then(response => response.json())
            .then(data => {
                agentInfo.textContent = `${data.name} (${data.id})`;
            })
            .catch(error => {
                agentInfo.textContent = 'Agent info unavailable';
            });

        function addMessage(content, isUser = false) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user' : 'agent'}`;
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            
            // Format content for better readability
            const formattedContent = formatMessageContent(content);
            contentDiv.innerHTML = formattedContent;
            
            messageDiv.appendChild(contentDiv);
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        function formatMessageContent(content) {
            // Simple and safe formatting - escape HTML and add formatting
            const div = document.createElement('div');
            div.textContent = content;
            let formatted = div.innerHTML;
            
            // Convert **bold** text using simple string operations
            while (formatted.indexOf('**') !== -1) {
                const firstPos = formatted.indexOf('**');
                const secondPos = formatted.indexOf('**', firstPos + 2);
                if (secondPos !== -1) {
                    const beforeText = formatted.substring(0, firstPos);
                    const boldText = formatted.substring(firstPos + 2, secondPos);
                    const afterText = formatted.substring(secondPos + 2);
                    formatted = beforeText + '<strong>' + boldText + '</strong>' + afterText;
                } else {
                    break;
                }
            }
            
            // Replace line breaks with <br> tags using character codes
            const cr = String.fromCharCode(13);
            const lf = String.fromCharCode(10);
            formatted = formatted.split(cr + lf).join('<br>');
            formatted = formatted.split(lf).join('<br>');
            formatted = formatted.split(cr).join('<br>');
            
            // Convert numbered lists using safe string operations
            const lines = formatted.split('<br>');
            let result = [];
            let inList = false;
            
            for (let i = 0; i < lines.length; i++) {
                const line = lines[i].trim();
                let isListItem = false;
                
                // Check if line starts with number, period, space (like "1. ")
                if (line.length > 2) {
                    const char1 = line.charAt(0);
                    const char2 = line.charAt(1);
                    const char3 = line.charAt(2);
                    if (char1 >= '0' && char1 <= '9' && char2 === '.' && char3 === ' ') {
                        isListItem = true;
                    }
                }
                
                // Start list if needed
                if (isListItem && !inList) {
                    result.push('<ol>');
                    inList = true;
                }
                
                // End list if needed
                if (!isListItem && inList) {
                    result.push('</ol>');
                    inList = false;
                }
                
                // Add list item or regular line
                if (isListItem) {
                    const dotPos = line.indexOf('. ');
                    const listContent = line.substring(dotPos + 2);
                    result.push('<li>' + listContent + '</li>');
                } else {
                    result.push(line);
                }
            }
            
            // Close list if still open
            if (inList) {
                result.push('</ol>');
            }
            
            return result.join('<br>');
        }

        function showError(message) {
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error';
            errorDiv.textContent = `Error: ${message}`;
            chatMessages.appendChild(errorDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        function sendMessage() {
            const message = messageInput.value.trim();
            if (!message) return;

            // Add user message to chat
            addMessage(message, true);
            messageInput.value = '';
            
            // Show loading
            loading.style.display = 'block';
            sendButton.disabled = true;

            // Send to agent
            fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    showError(data.error);
                } else {
                    addMessage(data.response);
                }
            })
            .catch(error => {
                showError('Failed to communicate with agent');
            })
            .finally(() => {
                loading.style.display = 'none';
                sendButton.disabled = false;
                messageInput.focus();
            });
        }

        function clearSession() {
            fetch('/api/clear-session', { method: 'POST' })
                .then(() => {
                    chatMessages.innerHTML = `
                        <div class="message agent">
                            <div class="message-content">
                                Session cleared! How can I help you?
                            </div>
                        </div>
                    `;
                })
                .catch(error => {
                    showError('Failed to clear session');
                });
        }

        // Event listeners
        sendButton.addEventListener('click', sendMessage);
        clearButton.addEventListener('click', clearSession);
        
        messageInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });

        // Focus input on load
        messageInput.focus();
    </script>
</body>
</html>'''
    
    with open(os.path.join(template_dir, 'chat.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    """
    Main function to run the web application.
    """
    print("=== Metis Agent Web App Template ===")
    print()
    
    # Check for API keys
    if not any(os.getenv(key) for key in ['GROQ_API_KEY', 'OPENAI_API_KEY', 'ANTHROPIC_API_KEY']):
        print("WARNING: No API keys found in environment variables.")
        print("Please set at least one of: GROQ_API_KEY, OPENAI_API_KEY, ANTHROPIC_API_KEY")
        print()
    
    # Create HTML template
    print("Creating chat interface template...")
    create_chat_template()
    
    # Initialize agent
    print("Initializing Metis Agent...")
    initialize_agent()
    
    identity = agent.get_agent_identity()
    print(f"Agent initialized: {identity.get('agent_name')} ({identity.get('agent_id')})")
    print()
    
    # Start web server
    print("Starting web server...")
    print("Visit: http://localhost:5000")
    print("Press Ctrl+C to stop")
    print()
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\nShutting down web server...")

if __name__ == "__main__":
    main()
