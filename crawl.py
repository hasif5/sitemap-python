# crawl.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    urls = set()
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        if href in urls:
            continue
        if domain_name not in href:
            continue
        urls.add(href)
    return urls

def crawl(url, max_urls=50):
    visited_urls = {}
    urls_to_crawl = deque([(url, 0)])
    while urls_to_crawl and len(visited_urls) < max_urls:
        current_url, depth = urls_to_crawl.popleft()
        print(f"Crawling: {current_url}")
        visited_urls[current_url] = depth
        new_urls = get_all_website_links(current_url)
        for new_url in new_urls:
            if new_url not in visited_urls:
                urls_to_crawl.append((new_url, depth + 1))
    return visited_urls

if __name__ == "__main__":
    start_url = input("Enter the full URL of the website to crawl: ")
    crawled_urls = crawl(start_url, max_urls=100)
    for url, depth in crawled_urls.items():
        print(f"URL: {url}, Depth: {depth}")
