# Content Creator Template

This template provides a specialized agent for creating various types of content. It includes custom tools for blog posts and social media content.

## Features

- Blog post generation with customizable tone and length
- Social media content for various platforms
- Content series creation across multiple platforms
- Structured output with formatting

## Usage

```python
from content_creator import ContentCreator

# Create the content creator
creator = ContentCreator(api_key="your_api_key")

# Define a session ID
session_id = "content_session"

# Create a blog post
topic = "Artificial Intelligence in Healthcare"
blog_post = creator.create_blog_post(
    topic, 
    tone="professional", 
    length="medium", 
    session_id=session_id
)

# Create social media posts
platforms = ["twitter", "linkedin"]
for platform in platforms:
    social_post = creator.create_social_media_post(platform, topic, session_id=session_id)

# Create a content series
results = creator.create_content_series(
    topic="Sustainable Living Tips",
    platforms=["twitter", "facebook", "instagram"],
    session_id=session_id
)
```

## Customization

You can customize the content creator by:

1. Modifying the `BlogPostTool` class to change how blog posts are generated
2. Adjusting the `SocialMediaTool` class to change how social media content is generated
3. Adding additional tools for other content types (e.g., email newsletters, video scripts)

## Example

See the `content_creator.py` file for a complete example of how to use this template.