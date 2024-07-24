import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def exclude_resources(url):
    excluded_extensions = ['.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.ico', '.woff', '.woff2', '.ttf', '.eot']
    for ext in excluded_extensions:
        if url.endswith(ext):
            return True
    return False

def should_exclude_path(url, exclude_paths):
    for path in exclude_paths:
        if path in url:
            return True
    return False

def get_all_website_links(url, exclude_paths):
    urls = set()
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    # Find all relevant tags that might contain links
    for tag in soup.find_all(['a', 'link', 'area']):
        href = tag.attrs.get("href")
        if not href or href.startswith('#') or href.startswith('mailto:'):
            continue

        href = urljoin(url, href)
        parsed_href = urlparse(href)

        # Normalize the URL
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href) or exclude_resources(href) or should_exclude_path(href, exclude_paths):
            continue
        if href in urls:
            continue
        if domain_name not in href:
            continue
        urls.add(href)

    return urls

def crawl(url, max_urls=50, exclude_paths=[]):
    visited_urls = {}
    urls_to_crawl = deque([(url, 0)])
    while urls_to_crawl and len(visited_urls) < max_urls:
        current_url, depth = urls_to_crawl.popleft()
        print(f"Crawling: {current_url}")
        visited_urls[current_url] = depth
        new_urls = get_all_website_links(current_url, exclude_paths)
        for new_url in new_urls:
            if new_url not in visited_urls:
                urls_to_crawl.append((new_url, depth + 1))
    return visited_urls

if __name__ == "__main__":
    start_url = input("Enter the full URL of the website to crawl: ")
    exclude_paths_input = input("Enter paths to exclude from the crawl, separated by commas (e.g., /feed/, /admin/): ")
    exclude_paths = [path.strip() for path in exclude_paths_input.split(',')] if exclude_paths_input else []
    
    crawled_urls = crawl(start_url, max_urls=100, exclude_paths=exclude_paths)
    for url, depth in crawled_urls.items():
        print(f"URL: {url}, Depth: {depth}")
