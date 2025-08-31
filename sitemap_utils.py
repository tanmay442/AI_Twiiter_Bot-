import advertools as adv
import pandas as pd

def fetch_blog_urls_from_sitemap(sitemap_url, filter_string):
    print(f"Fetching sitemap from: {sitemap_url}")
    try:
        sitemap_df = adv.sitemap_to_df(sitemap_url)
        print(f"Sitemap data loaded into a DataFrame with {len(sitemap_df)} entries.")#just to get beautifull logs in termial
        filtered_df = sitemap_df[sitemap_df['loc'].str.contains(filter_string)]
        print(f"Filtered {len(filtered_df)} URLs containing '{filter_string}'.")#just to get beautifull logs in termial
        return filtered_df
    except Exception as e:
        print(f"An error occurred while fetching sitemap: {e}")
        return pd.DataFrame([])
