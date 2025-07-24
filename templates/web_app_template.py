#!/usr/bin/env python3
"""
Web App Metis Agent Template

This template shows how to create a web-based chat interface using Flask
with the Metis Agent backend. Perfect for creating web applications with
AI chat capabilities.

Usage:
    python web_app_template.py
    Then visit: http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
from metis_agent import SingleAgent
from metis_agent.core.agent_config import AgentConfig
import os
import uuid
import json

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management
CORS(app)

# Global agent instance
agent = None

def initialize_agent():
    """
    Initialize the Metis Agent with web-optimized configuration.
    """
    global agent
    
    config = AgentConfig()
    
    # Configure for web usage
    config.set_memory_enabled(True)  # Enable memory for conversation context
    config.set_titans_memory(True)   # Enhanced memory for better responses
    
    # Create agent
    agent = SingleAgent(config)
    
    # Set web-friendly personality
    web_personality = """You are a helpful AI assistant integrated into a web application. 
    You provide clear, concise responses and are designed to help users with various tasks. 
    You maintain conversation context and provide a friendly, professional experience."""
    
    agent.config.agent_identity.set_custom_system_message(web_personality)
    
    return agent

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
        response = agent.process_query(user_message, session_id=session_id)
        
        return jsonify({
            'response': response,
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
            contentDiv.textContent = content;
            
            messageDiv.appendChild(contentDiv);
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
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
