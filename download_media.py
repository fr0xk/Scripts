import os

import re

import requests

import urllib.parse

from bs4 import BeautifulSoup as BS

from typing import List, Tuple, Dict

def generate_file_name(url: str, tag: str, alt: str) -> str:

    return os.path.join("downloaded_media",

                        re.sub(r'[^a-zA-Z0-9\.\-_]', '_', alt or os.path.basename(urllib.parse.urlsplit(url).path))

                        + os.path.splitext(url if tag != 'audio' else requests.head(url).headers.get('Content-Type'))

                        .pop(0))

def download_file(url: str, file_name: str, max_size: int) -> None:

    print(f'Downloading {file_name}')

    try:

        response = requests.get(url, stream=True)

        if max_size and int(response.headers.get('Content-Length', 0)) > max_size and \

                input(f"Do you want to download this file ({url})? [y/N] ").lower() != 'y':

            return

        with open(file_name, 'wb') as file:

            for chunk in response.iter_content(1024):

                file.write(chunk)

    except requests.exceptions.RequestException as e:

        print(f'Error downloading {url}: {e}')

url = input("Enter the URL of the web page: ")

try:

    response = requests.get(url)

    response.raise_for_status()

    soup = BS(response.content, 'html.parser')

    tags: List[Tuple[str, str]] = [('img', 'src'), ('video', 'src'), ('audio', 'src'), ('source', 'src')]

    max_sizes: Dict[str, int] = {'img': 10000000, 'video': 100000000, 'audio': 10000000, 'source': 10000000}

    media_tags: List[Tuple[str, str]] = [(tag.name, tag.get(attribute)) for tag in soup.find_all(tags)]

    document_links: List[str] = [link.get('href') for link in soup.find_all('a', {'href': re.compile(

        r'\.(pdf|docx?|xlsx?|pptx?|txt)$', re.IGNORECASE)}) if link.get('href').startswith('http')]

    download_media = lambda url, tag: download_file(url, generate_file_name(url, tag, BS(str(tag), 'html.parser')

                                                                    .get('alt')), max_sizes.get(tag.name))

    download_document = lambda url: download_file(url, generate_file_name(url, '', ''), 0)

    for tag, url in media_tags:

        if url and url.startswith('http') and not BS(str(tag), 'html.parser').has_attr('data-no-download'):

            download_media(url, tag)

    for url in document_links:

        if url and url.startswith('http'):

            download_document(url)

except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:

    print(f'Error: {e}')

except Exception as e:

    print(f'Unexpected Error: {e}')

