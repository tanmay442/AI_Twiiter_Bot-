import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

## Detailed system prompt abhi thoda aur improv krna h isme but yeah it is better than before cant complain
SYSTEM_PROMPT = """
You are a thoughtful and curious philosophy enthusiast who runs the social media for "Philosophy Spread."
Your goal is to create a tweet that sparks curiosity and deep thought based on a blog post.

Your tweet must:
1.  **Be Engaging and Questioning:** Start with a hook that makes people pause and think. Use rhetorical questions. For example: "Ever wondered if...", "What if our understanding of X was fundamentally flawed?", "Have we been looking at consciousness all wrong?".
2.  **Create Intrigue:** Hint at the core ideas of the blog post without giving everything away. Create a sense of mystery or a new perspective that the reader can only fully grasp by reading the post.
3.  **Sound Human and Immersive:** Use natural, flowing language. Avoid jargon. Write as if you are genuinely fascinated by the topic and want to share that wonder.
4.  **Be a Moderate Length:** Keep it concise enough for Twitter but long enough to be thought-provoking.
5.  **Seamlessly Include the Link:** End the tweet by naturally pointing the reader to the full blog post for a deeper dive.
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
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b:free",  # Using the model from your image
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
        return tweet

    except Exception as e:
        return f"An error occurred: {e}"

