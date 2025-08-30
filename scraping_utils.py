import requests
from bs4 import BeautifulSoup
import time
import re

def scrape_url_for_text_content(url, delay=1):
    """
    Adding AI Generated Comments to the Code to make it more understandable
    Fetches URL's HTML, extracts main text content.

    Args:
        url (str): URL to scrape.
        delay (int): Seconds to wait before request (polite scraping).

    Returns:
        str: Extracted text, or None on error.
    """
    # print(f"Attempting to scrape: {url}") # Uncomment for verbose output
    time.sleep(delay) # Polite delay

    try:
        # Mimic browser, set timeout
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Raise for 4xx/5xx errors

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract main content from common HTML tags
        main_content_tags = ['article', 'main']
        text_content = ""

        for tag_name in main_content_tags:
            content_tag = soup.find(tag_name)
            if content_tag:
                text_content = content_tag.get_text(separator=' ', strip=True)
                break
        else:
            # Fallback to body text, removing scripts/styles/nav/footer/header
            body_tag = soup.find('body')
            if body_tag:
                for unwanted_tag in body_tag(['script', 'style', 'nav', 'footer', 'header']):
                    unwanted_tag.decompose()
                text_content = body_tag.get_text(separator=' ', strip=True)

        # Clean whitespace
        text_content = re.sub(r'\s+', ' ', text_content).strip()

        if not text_content:
            print(f"Warning: No significant text content extracted from {url}")

        return text_content[12:-18]

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error for {url}: {errh}")
    except requests.exceptions.RequestException as err: # Catch all other requests errors
        print(f"Request Error for {url}: {err}")
    except Exception as e: # Catch other parsing or general errors
        print(f"Parsing/General Error for {url}: {e}")
    return None

# The example usage is removed here.
# To use this function:
# 1. Save it as a Python file (e.g., 'my_scraper_functions.py')
# 2. In your main code, import it: 'from my_scraper_functions import scrape_url_for_text_content'
# 3. Call it with your URL: 'text = scrape_url_for_text_content("https://your-url.com")'