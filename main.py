import tweepy
import os
from pprint import pprint
from dotenv import load_dotenv
import advertools as adv
import pandas as pd
from scraping_utils import scrape_url_for_text_content
from openai import OpenAI



print("Loading environment variables...")
load_dotenv()

def create_client():
    print("Creating Twitter client...")
    client = tweepy.Client(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
    )
    print("Twitter client created.")
    return client


def create_tweet(client, text):
    print("Creating tweet...")
    response = client.create_tweet(text=text)
    print("Tweet created.")
    return response



sitemap_url = 'https://philosophyspread.vercel.app/sitemap.xml'

def fetch_URL(sitemap_url):
    print(f"Fetching sitemap from: {sitemap_url}")
    try:
        sitemap_df = adv.sitemap_to_df(sitemap_url)
        print(f"Sitemap data loaded into a DataFrame with {len(sitemap_df)} entries.")
        def filetering_urls(sitemap_df):
            global filtered_df
            filtered_df = sitemap_df[sitemap_df['loc'].str.contains('/blog/')]
            print(f"Filtered {len(filtered_df)} blog URLs.")
            return filtered_df
        filetering_urls(sitemap_df)
    except Exception as e:
        print(f"An error occurred: {e}")
    return filtered_df


blog_urls_df = fetch_URL(sitemap_url)


def get_latest_blog_url(blog_urls_df):
    print("Getting latest blog URL...")
    try:
        last_url = blog_urls_df.iloc[-1]['loc']
        print(f"Latest blog URL found: {last_url}")
        return last_url
    except Exception as e:
        print(f"An error occurred while fetching the latest blog URL: {e}")
        return None

latest_blog_url = get_latest_blog_url(blog_urls_df)
print("Scraping latest blog for text content...")
text_content = scrape_url_for_text_content(latest_blog_url)
print("Writing scraped content to latest_blog.txt...")
with open('latest_blog.txt', 'w', encoding='utf-8') as file:
    file.write(text_content)
print("Done.")





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


##MOre to do left ot do but will do later cause  i aam a big eater gonna eat some food