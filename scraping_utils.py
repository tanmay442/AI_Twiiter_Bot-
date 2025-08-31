import requests
from bs4 import BeautifulSoup
import time
import re

def scrape_url_for_text_content(url, delay=1):
    print(f"Starting scrape for: {url}")#just to get beautifull logs in termial
    time.sleep(delay) # Polite delay
    try:
        print("Sending HTTP request...")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print("HTTP request successful. Parsing HTML...")#just to get beautifull logs in termial
        soup = BeautifulSoup(response.text, 'html.parser')
        main_content_tags = ['article', 'main']
        text_content = ""
        for tag_name in main_content_tags:
            content_tag = soup.find(tag_name)
            if content_tag:
                print(f"Found main content in <{tag_name}> tag.")#just to get beautifull logs in termial
                text_content = content_tag.get_text(separator=' ', strip=True)
                break
        else:
            print("Main content tags not found. Falling back to <body> tag.")
            body_tag = soup.find('body')
            if body_tag:
                for unwanted_tag in body_tag(['script', 'style', 'nav', 'footer', 'header']):
                    unwanted_tag.decompose()
                text_content = body_tag.get_text(separator=' ', strip=True)
        text_content = re.sub(r'\s+', ' ', text_content).strip()
        if not text_content:
            print(f"Warning: No significant text content extracted from {url}")
        print("Scraping complete.")#just to get beautifull logs in termial
        return text_content
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error for {url}: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error for {url}: {err}")
    except Exception as e:
        print(f"Parsing/General Error for {url}: {e}")
    return None

