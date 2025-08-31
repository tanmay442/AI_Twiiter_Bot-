import tweepy
import os
from pprint import pprint
from dotenv import load_dotenv
from scraping_utils import scrape_url_for_text_content
from sitemap_utils import fetch_blog_urls_from_sitemap
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

filter_string = '/blog/'  # to segregate url basically 

##Fetching the Sitemap and filtered URLs
blog_urls_df = fetch_blog_urls_from_sitemap(sitemap_url, filter_string)

##getting the latest blog URL
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
print("Text content scraped.")




