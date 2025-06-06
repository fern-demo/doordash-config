#!/usr/bin/env python3
"""
Scrape DoorDash Marketplace Docs Using Sitemap

- Parses https://developer.doordash.com/en-US/sitemap.xml
- Extracts all URLs under /en-US/docs/marketplace/
- Downloads each page, extracts main content, converts to Markdown
- Saves each page as a Markdown file in a directory structure mirroring the URL path

Requirements:
    pip install requests beautifulsoup4 markdownify

Usage:
    python scrape_doordash_docs.py
"""
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import os

SITEMAP_URL = "https://developer.doordash.com/en-US/sitemap.xml"
OUTPUT_DIR = "doordash_marketplace_docs"
USER_AGENT = "Mozilla/5.0 (compatible; DoorDashDocScraper/1.0)"

def get_marketplace_urls():
    resp = requests.get(SITEMAP_URL)
    soup = BeautifulSoup(resp.content, "xml")
    urls = [loc.text for loc in soup.find_all("loc")]
    # Only keep marketplace docs
    return [url for url in urls if "/en-US/docs/marketplace/" in url]

def save_markdown(url):
    resp = requests.get(url, headers={"User-Agent": USER_AGENT})
    soup = BeautifulSoup(resp.text, "html.parser")
    main = soup.find('main', class_='theme-doc-markdown') or soup.find('main')
    if not main:
        print(f"[WARN] Could not find main content for {url}")
        return
    md_content = md(str(main), heading_style="ATX")
    # Build output path
    path = url.split("/en-US/docs/marketplace/")[-1].strip("/")
    if not path or path.endswith("/"):
        path += "index"
    out_path = os.path.join(OUTPUT_DIR, path + ".md")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"[SAVED] {out_path}")

if __name__ == "__main__":
    urls = get_marketplace_urls()
    print(f"Found {len(urls)} marketplace doc URLs.")
    for url in urls:
        save_markdown(url)
    print("Done!") 