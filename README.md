# Twitter Blog Auto-Tweeter

## Project Overview
This project was born from the idea of sharing the latest blog posts from my website on Twitter. What started as a simple plan to post updates manually quickly evolved into a fully automated solution, combining web scraping, AI-powered content generation, and seamless Twitter integration.

**Developer:** Tanmay Goel  
**Contact:** goeltanmay442@outlook.com

---

## How It Works
1. **Sitemap Scraping:**
   - The bot fetches your website's sitemap using the `advertools` library.
   - It filters URLs based on a configurable string (e.g., `/blog/`) to find the latest blog post.
   - This logic is modularized in `sitemap_utils.py` for easy reuse and customization.
2. **Content Extraction:**
   - The latest blog URL is parsed using `scraping_utils.py`, which uses `requests` and `BeautifulSoup` to extract only the main readable text (ignoring navigation, scripts, etc.).
3. **AI Tweet Generation:**
   - The extracted blog content is sent to OpenRouter's API using the `openai` Python client.
   - The model used for tweet generation is `openai/gpt-oss-120b:free`, but you can easily swap in other models supported by OpenRouter.
4. **Twitter Posting:**
   - The generated tweet is posted to Twitter using the `tweepy` library.
   - All credentials are securely loaded from a `.env` file.
5. **Live Logging:**
   - Throughout the process, beautiful and informative logs are printed to the terminal, showing each step in real time (e.g., loading environment, scraping, parsing, AI generation, posting).

---

## Directory Structure
```
Twitter-Bot-TRY/
├── main.py                # Main orchestration script
├── sitemap_utils.py       # Sitemap fetching & filtering
├── scraping_utils.py      # Blog content extraction
├── Content_gen_utils.py   # (Optional) Additional content generation utilities
├── Requirements.txt       # All required Python packages
├── .env                   # Your API keys and secrets
└── README.md              # This documentation
```

---

## Technologies Used
- Python 3.8+
- Tweepy (Twitter API)
- python-dotenv
- advertools
- pandas
- requests
- beautifulsoup4
- openai (for OpenRouter API)

---

## Quick Start
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/tanmay442/Twitter-Bot-TRY.git
   cd Twitter-Bot-TRY
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r Requirements.txt
   ```
3. **Set Up Environment Variables:**
   - Create a `.env` file in the project root:
     ```env
     CONSUMER_KEY=your_twitter_consumer_key
     CONSUMER_SECRET=your_twitter_consumer_secret
     ACCESS_TOKEN=your_twitter_access_token
     ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
     OPENROUTER_API_KEY=your_openrouter_api_key
     ```
4. **Run the Bot:**
   ```bash
   python main.py
   ```
   - Watch the live logs in your terminal as each step is performed!

---

## Customization & Extensibility
- **Change the URL Filter:**
  - In `main.py`, set `filter_string` to match your blog URLs (e.g., `/blog/`, `/news/`, etc.).
- **Switch AI Models:**
  - Update the model name in the OpenRouter API call to use different AI models.
- **Add More Features:**
  - Extend `Content_gen_utils.py` for advanced content manipulation or multi-platform posting.

---

## Replication & Contribution
- Fork or clone the repo and follow the setup steps above.
- All modules are designed for easy extension and integration.
- Feel free to reach out for questions or collaboration!

---

## Final Notes
- All credentials are kept secure in `.env`.
- The bot generates beautiful, step-by-step logs so you always know what it's doing.
- Modular design makes it easy to adapt for other websites or social platforms.

---

**Made with ❤️ by Tanmay Goel**
