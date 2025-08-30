import tweepy
import os
from pprint import pprint
from dotenv import load_dotenv
import advertools as adv
import pandas as pd
from scraping_utils import scrape_url_for_text_content


load_dotenv()

def create_client():
    client = tweepy.Client(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
    )
    return client


def create_tweet(client, text):
    response = client.create_tweet(text=text)
    return response



sitemap_url = 'https://philosophyspread.vercel.app/sitemap.xml'

def fetch_URL(sitemap_url):
    try:
        sitemap_df = adv.sitemap_to_df(sitemap_url)

        #print(f"Sitemap data loaded into a DataFrame with {len(sitemap_df)} entries.")'''use thisto check the number of url loaded '''
        #print(sitemap_df[['loc', 'lastmod']]) #for testing purposes

        def filetering_urls(sitemap_df):
            global filtered_df #bruh dont forgot to make it global or govind sir ki aatma satayegi
            filtered_df = sitemap_df[sitemap_df['loc'].str.contains('/blog/')]
            return filtered_df
        
        filetering_urls(sitemap_df)

    except Exception as e:
        print(f"An error occurred: {e}")

    return filtered_df


blog_urls_df = fetch_URL(sitemap_url)


def get_latest_blog_url(blog_urls_df): #getting the last url bro why did i choose dataframe over list idk ,pagal to hun thoda sa
    try:
        last_url = blog_urls_df.iloc[-1]['loc']
        return last_url
        
    except Exception as e:
        print(f"An error occurred while fetching the latest blog URL: {e}")
        return None

latest_blog_url = get_latest_blog_url(blog_urls_df)
print(f"Latest blog URL: {latest_blog_url}")

text_content = scrape_url_for_text_content(latest_blog_url)
with open('latest_blog.txt', 'w', encoding='utf-8') as file:
    file.write(text_content)