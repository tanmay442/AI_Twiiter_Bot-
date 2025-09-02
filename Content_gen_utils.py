import os
from openai import OpenAI
from dotenv import load_dotenv
import sys

load_dotenv()

## Detailed system prompt abhi thoda aur improv krna h isme but yeah it is better than before cant complain
SYSTEM_PROMPT = """
You are a thoughtful and curious philosophy enthusiast who runs the social media for "Philosophy Spread."
Your goal is to create a tweet that sparks curiosity and deep thought based on a blog post.

Your tweet must:
1.  **Be Engaging and Questioning:** Start with a hook that makes people pause and think.
2.  **Create Intrigue:** Hint at the core ideas of the blog post without giving everything away.
3.  **Sound Human and Immersive:** Use natural, flowing language. Avoid jargon.
4.  **Be a Moderate Length:** Keep it concise enough for Twitter but long enough to be thought-provoking.
5.  **Subtle Emoji Use:** Add one or two emojis if they genuinely enhance the thoughtful tone (e.g., 🤔, ✨).
6.  **Seamlessly Include the Link:** End the tweet by naturally pointing the reader to the full blog post.

**CRITICAL RULES FOR THE OUTPUT:**
- **START CLEAN:** Your response must begin DIRECTLY with the first word of the tweet. Do not include any prefixes, control tokens like '<|start|>', XML tags, or any other text that is not part of the tweet itself.
- **Plain Text Only:** Your output must be plain text only. Do not include any code, JSON, or technical formatting.
- **No Wrappers:** Do not wrap your final response in single or double quotes.
- **Clean and Readable:** Ensure the output is clean, human-readable text. Avoid any weird characters like '\\u202f'.
"""

def generate_tweet(blog_content: str, blog_url: str) -> str:
    """
    Generates an engaging tweet for a philosophy blog post.

    Args:
        blog_content: The text content of the blog post.
        blog_url: The URL to the full blog post.

    Returns:
        A string containing the generated tweet.
    """
    try:
        #intialisisnf the client
        print("Intialising open oruter client....")#just to get beautifull logs in termial
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )

        # The blog tesxt and url 
        user_content = f"""
        Here is the blog post content:
        ---
        {blog_content}
        ---
        And here is the link to the full article: {blog_url}
        """

        # calking the api
        print("Calling the OpenRouter API ...")#just to get beautifull logs in termial
        completion = client.chat.completions.create(
            model="microsoft/mai-ds-r1:free",  
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_content
                }
            ]
        )

        # ai response here 
        tweet = completion.choices[0].message.content
        print(tweet)  # For debugging purposes
        #print (type(tweet)) #just confirming hte type is str
        return tweet

    except Exception as e:
        print("API FAILED")
        print(f"An error occurred: {e}")
        sys.exit(0)
    
    
    

