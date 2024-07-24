# sitemap-python
Crawl websites to generate Google/Seo friendly sitemap


# Sitemap Crawler and Generator

This project provides a Python-based sitemap crawler and generator. It crawls a given website, collects URLs, and generates a sitemap XML file following Google's guidelines. The sitemap file is saved in a subdirectory named after the website's domain.

## Features

- Crawls a website and collects URLs
- Generates a sitemap XML file
- Sets priority based on page depth
- Saves the sitemap in a subdirectory named after the website's domain

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hasif5/sitemap-python.git
cd sitemap-python
```

2. Install the required Python packages:

```bash
pip install requests beautifulsoup4 lxml
```

## Usage
Run the create_sitemap.py script:

```bash
python create_sitemap.py
```
- Enter the full URL of the website when prompted. 

Enter optional path to be ignored in the crawl in second prompt. Example:
```bash
/admin/,/rss/,/feed/
```

The script will crawl the website, generate a sitemap, and save it in a subdirectory named after the website's domain.

### File Structure

```text
|- crawl.py: 
            Contains the crawling logic to collect URLs from a website.
|- create_sitemap.py: 
            Contains the logic to generate and save the sitemap XML file. It also prompts the user for the website URL and handles directory creation.
```

### Example
```bash
$ python create_sitemap.py
```
- Enter the full URL of the website to crawl: https://example.com
```text
Crawling: https://example.com
Crawling: https://example.com/page1
Crawling: https://example.com/page2
```

- Sitemap saved as example.com/sitemap.xml
 

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Acknowledgements

This project uses the following Python packages:

- **requests**
- **beautifulsoup4**
- **lxml**

### Contact
For any questions or suggestions, please open an issue in this repository.
