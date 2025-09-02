import tweepy
import os
import sys
from pprint import pprint
from dotenv import load_dotenv
from scraping_utils import scrape_url_for_text_content
from sitemap_utils import fetch_blog_urls_from_sitemap
from Content_gen_utils import generate_tweet


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



# Prompt user for configuration choice
print("Do you want to use the preconfigured blog settings or enter a custom blog URL?")
print("1. Preconfigured (latest blog from sitemap)")
print("2. Custom blog URL")
choice = input("Enter 1 or 2: ").strip()

if choice == "2":
    selected_blog_url = input("Enter the custom blog URL: ").strip()
    print(f"Using custom blog URL: {selected_blog_url}")
else:
    sitemap_url = 'https://philosophyspread.vercel.app/sitemap.xml'
    filter_string = '/blog/'  # to segregate url basically 
    # Fetching the Sitemap and filtered URLs
    blog_urls_df = fetch_blog_urls_from_sitemap(sitemap_url, filter_string)

    # Getting the latest blog URL
    def get_latest_blog_url(blog_urls_df):
        print("Getting latest blog URL...")
        try:
            last_url = blog_urls_df.iloc[-1]['loc']
            print(f"Latest blog URL found: {last_url}")
            return last_url
        except Exception as e:
            print(f"An error occurred while fetching the latest blog URL: {e}")
            return None

    selected_blog_url = get_latest_blog_url(blog_urls_df)

print("Scraping blog for text content...")
text_content = scrape_url_for_text_content(selected_blog_url)
print("Text content scraped.")

##print(type(text_content)) #just confirming hte type is str

try:
    tweat_content = generate_tweet(text_content, selected_blog_url)
    print("Tweet content generated:")
    ##pprint(tweat_content)   ##testing purpose
except Exception as e:
    print(f"An error occurred while generating tweet content: {e}")
    sys.exit(0)

   

def clean_model_output(raw_text: str) -> str:
    """Removes leading model control tags like '<|start|>...<|message|>' from text."""

    marker = "<|message|>" # This is the final tag before the actual content begins.
    marker_pos = raw_text.find(marker) # Find the position of where this final tag ends.

    # If the marker tag is found in the string...
    if marker_pos != -1:
        # ...slice the string to get only the text that comes *after* the marker.
        clean_text = raw_text[marker_pos + len(marker):]
    else:
        # ...otherwise, assume the text is already clean and use it as is.
        clean_text = raw_text
        
    # Finally, strip any leftover wrapper characters (like ' or () ) and whitespace from the ends.
    return clean_text.strip(" '\"()")

print("Cleaning model output...")
cleaned_tweet = clean_model_output(tweat_content)
print("Cleaned tweet content:")
##pprint(cleaned_tweet)    ##for testing purpose

create_tweet(create_client(), cleaned_tweet)
