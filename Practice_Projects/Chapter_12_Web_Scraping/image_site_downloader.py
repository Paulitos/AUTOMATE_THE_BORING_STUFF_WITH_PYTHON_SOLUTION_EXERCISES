# Image Site Downloader Page 298 Chapter 12
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Function to download an image from a URL
def download_image(url, folder_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Get the file name from the URL
            parsed_url = urlparse(url)
            file_name = os.path.basename(parsed_url.path)

            # Combine the folder path and file name
            file_path = os.path.join(folder_path, file_name)

            # Save the image to the specified folder
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {file_path}")
    except Exception as e:
        print(f"Error downloading image from {url}: {str(e)}")

# Function to download images from a search URL
def download_images_from_search(search_url, folder_path):
    try:
        response = requests.get(search_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all image elements on the page
            img_tags = soup.find_all('img')

            for img_tag in img_tags:
                img_url = img_tag.get('src')
                if img_url:
                    # Handle relative URLs
                    img_url = urljoin(search_url, img_url)
                    download_image(img_url, folder_path)
        else:
            print(f"Failed to fetch {search_url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error processing {search_url}: {str(e)}")

# Main function
if __name__ == "__main__":
    # Provide the search URL and folder path
    search_url = "https://www.flickr.com/search/?text=spectrobes%20nintendo%20ds%20"  # Replace with your search URL
    folder_path = r"C:\Users\pablo\Documents\Github_repo_AUTOMATING_THE_BORING_STUFF_WITH_PYTHON\Practice_Projects\Chapter_12_Web_Scraping\image_site_downloader_folder" # Replace with your desired folder path

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Download images from the search URL
    download_images_from_search(search_url, folder_path)

