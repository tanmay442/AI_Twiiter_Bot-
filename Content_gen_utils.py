from openai import OpenAI   
import os
from dotenv import load_dotenv

load_dotenv()

#Inintialising the open ai Clienr 

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= "<OPENROUTER_API_KEY>",
)


completion = client.chat.completions.create(
    model="openai/gpt-oss-120b:free",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the meaning of life?"}
    ]
)
print(completion.choices[0].message.content)