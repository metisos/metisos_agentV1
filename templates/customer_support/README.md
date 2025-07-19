# Customer Support Template

This template provides a specialized agent for handling customer inquiries. It includes custom tools for FAQ handling and ticket creation.

## Features

- FAQ handling with knowledge base
- Support ticket creation
- Inquiry categorization and prioritization
- Structured responses

## Usage

```python
from customer_support import CustomerSupportAgent

# Create the customer support agent
agent = CustomerSupportAgent(api_key="your_api_key")

# Define a session ID
session_id = "support_session"

# Handle an FAQ question
faq_question = "What are your business hours?"
faq_response = agent.answer_faq(faq_question, session_id=session_id)

# Create a support ticket
issue = "I'm having trouble logging into my account. It says my password is incorrect, but I'm sure it's right."
ticket_response = agent.create_ticket(issue, session_id=session_id)

# Handle a general inquiry
inquiry = "Can you tell me more about your premium subscription features?"
inquiry_response = agent.handle_inquiry(inquiry, session_id=session_id)
```

## Customization

You can customize the customer support agent by:

1. Modifying the `FAQTool` class to change how FAQ questions are handled
2. Adjusting the `TicketCreationTool` class to change how tickets are created
3. Adding a custom FAQ database by providing a JSON file
4. Adding additional tools for specific customer support tasks

## Example

See the `customer_support.py` file for a complete example of how to use this template.