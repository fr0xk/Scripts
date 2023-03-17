import os, requests, mimetypes, uuid, re

from bs4 import BeautifulSoup

def download_media(url):

    try:

        response = requests.get(url)

        response.raise_for_status()

    except requests.exceptions.RequestException as e:

        print(f"Error: {e}")

        return

    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    media_tags = soup.find_all(lambda tag: tag.name in ['img', 'video', 'source', 'a'])

    frame_tags = soup.find_all(lambda tag: tag.name in ['frame', 'iframe'])

    for frame_tag in frame_tags:

        try:

            response = requests.get(frame_tag['src'])

            response.raise_for_status()

        except requests.exceptions.RequestException as e:

            print(f"Error: {e}")

            continue

        frame_html_content = response.content

        frame_soup = BeautifulSoup(frame_html_content, 'html.parser')

        media_tags += frame_soup.find_all(lambda tag: tag.name in ['img', 'video', 'source', 'a'])

    directory = "downloaded_media"

    os.makedirs(directory, exist_ok=True)

    media_files = [(media_tag.get('src') or media_tag.get('href'), media_tag.get('alt', 'media')) for media_tag in media_tags if media_tag.get('src') or media_tag.get('href')]

    for media_url, media_alt in media_files:

        if media_url.startswith('http'):

            file_name = re.sub(r'[^a-zA-Z0-9\.\-_]', '_', media_alt) or re.sub(r'[^a-zA-Z0-9\.\-_]', '_', os.path.basename(media_url))

            try:

                response = requests.head(media_url)

                response.raise_for_status()

            except requests.exceptions.RequestException as e:

                print(f"Error: {e}")

                continue

            content_type = response.headers.get('Content-Type')

            extension = mimetypes.guess_extension(content_type.split(';')[0]) if content_type else os.path.splitext(media_url)[1]

            file_name = os.path.join(directory, file_name + extension)

            file_size = int(response.headers.get('Content-Length', 0))

            if file_size > 52428800:

                answer = input(f"The file '{file_name}' is large ({file_size//1048576} MB). Do you want to download it? (y/n) ")

                if answer.lower() != 'y':

                    continue

            try:

                response = requests.get(media_url)

                response.raise_for_status()

            except requests.exceptions.RequestException as e:

                print(f"Error: {e}")

                continue

            with open(file_name, 'wb') as f:

                f.write(response.content)

    print("All media downloaded successfully!")

def main():

    url = input("Enter the URL of the web page to download media from: ")

    download_media(url)

if __name__ == '__main__':

    main()

