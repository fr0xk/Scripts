import requests

from bs4 import BeautifulSoup

import os

def download_images(url):

    # Create 'images' directory if it does not exist

    if not os.path.exists('downloaded_images'):

        os.makedirs('downloaded_images')

    # Send request and get HTML content

    response = requests.get(url)

    html = response.content

    # Parse HTML content with BeautifulSoup

    soup = BeautifulSoup(html, 'html.parser')

    # Extract image URLs and filter advertising content

    img_urls = [img['src'] for img in soup.find_all('img') if 'ad' not in img['src'] and 'banner' not in img['src']]

    # Download images and show progress

    print(f"Downloading {len(img_urls)} images...")

    for i, url in enumerate(img_urls):

        try:

            response = requests.get(url)

            if response.status_code == 200:

                file_name = f"images/{i}.jpg"

                with open(file_name, 'wb') as f:

                    f.write(response.content)

                print(f"Downloaded {file_name}")

            else:

                print(f"Error downloading {url}: {response.status_code}")

        except Exception as e:

            print(f"Error downloading {url}: {e}")

    print(f"Download complete. {len(img_urls)} images downloaded to the 'images' directory.")

if __name__ == '__main__':

    url = input("Enter website URL: ")

    download_images(url)

