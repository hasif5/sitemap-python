# create_sitemap.py
import os
import xml.etree.ElementTree as ET
from crawl import crawl
from urllib.parse import urlparse

def calculate_priority(depth):
    if depth == 0:
        return 1.0
    elif depth == 1:
        return 0.8
    elif depth == 2:
        return 0.6
    elif depth == 3:
        return 0.4
    else:
        return 0.2

def create_sitemap(urls):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url, depth in urls.items():
        url_element = ET.Element("url")
        loc_element = ET.Element("loc")
        loc_element.text = url
        priority_element = ET.Element("priority")
        priority_element.text = str(calculate_priority(depth))
        url_element.append(loc_element)
        url_element.append(priority_element)
        urlset.append(url_element)
    return urlset

def save_sitemap(sitemap, directory, filename="sitemap.xml"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    tree = ET.ElementTree(sitemap)
    tree.write(filepath, encoding="utf-8", xml_declaration=True)
    return filepath

if __name__ == "__main__":
    start_url = input("Enter the full URL of the website to crawl: ")
    parsed_url = urlparse(start_url)
    directory = parsed_url.netloc

    crawled_urls = crawl(start_url, max_urls=100)
    sitemap = create_sitemap(crawled_urls)
    sitemap_path = save_sitemap(sitemap, directory)
    print(f"Sitemap saved as {sitemap_path}")
