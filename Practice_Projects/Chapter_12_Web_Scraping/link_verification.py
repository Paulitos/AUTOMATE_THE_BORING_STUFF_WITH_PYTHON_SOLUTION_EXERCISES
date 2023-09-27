# Link Verification Page 299 Chapter 12
import requests
from bs4 import BeautifulSoup

def check_links(url, startswith_pattern):
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        all_links = soup.find_all('a', href=True)

        for link in all_links:
            href_url = link['href']
            if href_url.startswith(startswith_pattern):
                try:
                    res = requests.get(href_url)
                    if res.status_code == 404:
                        print('Status Code 404:', href_url)
                except requests.exceptions.RequestException:
                    continue

        print('All links checked!')
    except requests.exceptions.RequestException as e:
        print('Error:', e)

# Example usage:
website_url = 'https://example.com'
prefix_to_check = 'http'  # Modify this to match the desired prefix
check_links(website_url, prefix_to_check)
