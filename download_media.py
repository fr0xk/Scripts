import requests

import os

import mimetypes

from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup

from tqdm import tqdm

import threading

def is_valid(url):

    """

    Check if a url is valid

    """

    parsed = urlparse(url)

    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(url):

    """

    Returns all image URLs on a single `url`

    """

    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    urls = []

    for img in soup.find_all("img"):

        img_url = img.attrs.get("src")

        if not img_url:

            continue

        # make the URL absolute by joining domain with the URL that is just extracted

        img_url = urljoin(url, img_url)

        try:

            pos = img_url.index("?")

            img_url = img_url[:pos]

        except ValueError:

            pass

        # finally, if the url is valid

        if is_valid(img_url):

            urls.append(img_url)

    return urls

def get_all_documents(url):

    """

    Returns all embedded document URLs on a single `url`

    """

    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    urls = []

    for doc in soup.find_all("embed"):

        doc_url = doc.attrs.get("src")

        if not doc_url:

            continue

        # make the URL absolute by joining domain with the URL that is just extracted

        doc_url = urljoin(url, doc_url)

        # finally, if the url is valid

        if is_valid(doc_url):

            urls.append(doc_url)

    return urls

def get_all_videos(url):

    """

    Returns all video URLs on a single `url`

    """

    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    urls = []

    for video in soup.find_all("video"):

        video_url = video.attrs.get("src")

        if not video_url:

            continue

        # make the URL absolute by joining domain with the URL that is just extracted

        video_url = urljoin(url, video_url)

        # finally, if the url is valid

        if is_valid(video_url):

            urls.append(video_url)

    return urls

def download(url, folder):

    """

    Downloads a single `url` to a specified `folder`

    """

    try:

        response = requests.get(url, stream=True)

        # get the file name from the URL

        file_name = os.path.join(folder, os.path.basename(urlparse(url).path))

        # get the content type of the response

        content_type = response.headers.get("Content-Type")

        # if the content type is unknown, use the file extension to guess the file type

        if not content_type:

            content_type = mimetypes.guess_type(file_name)[0]

        # if the content type is still unknown, default to binary/octet-stream

        if not content_type:

            content_type = "binary/octet-stream"

        # get the file extension from the content type

        extension = mimetypes.guess_extension(content_type.split(";")[0]) or os.path.splitext(file_name)[1]

        # set the file name to include the extension

        file_name += extension

        # get the content length of the response

        content_length = int(response.headers.get("Content-Length", 0))

        # ask user permission for large files based on file types

