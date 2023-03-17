import requests

import os

from tqdm import tqdm

# Define the file extensions for different media types

MEDIA_TYPES = {

    'audio': ['.mp3', '.wav', '.ogg', '.aac'],

    'image': ['.jpg', '.jpeg', '.png', '.gif'],

    'video': ['.mp4', '.avi', '.flv', '.wmv'],

    'document': ['.pdf', '.doc', '.docx', '.txt']

}

def download_media(url, media_type):

    # Get the response object from the URL

    response = requests.get(url, stream=True)

    # If the file size is larger than 50 MB, ask for user permission

    if int(response.headers.get('Content-Length', 0)) > 50 * 1024 * 1024:

        user_choice = input(f"The {media_type} file is larger than 50 MB. Do you want to download it? [Y/N]: ")

        if user_choice.lower() != 'y':

            return None

    # Create a folder for the downloaded files if it doesn't exist

    if not os.path.exists('downloaded_media'):

        os.makedirs('downloaded_media')

    # Get the file name from the URL

    file_name = url.split('/')[-1]

    # Create a progress bar using tqdm

    progress_bar = tqdm(unit="B", total=int(response.headers.get('Content-Length', 0)), unit_scale=True)

    # Download the file in chunks and update the progress bar

    with open(f"downloaded_media/{media_type}/{file_name}", 'wb') as file:

        for chunk in response.iter_content(chunk_size=1024):

            if chunk:

                file.write(chunk)

                progress_bar.update(len(chunk))

    return file_name

# Ask for user input

url = input("Enter the URL to download media from: ")

# Download all media files from the website

media_files = {media_type: [] for media_type in MEDIA_TYPES.keys()}

response = requests.get(url)

for line in response.iter_lines():

    line = line.decode('utf-8')

    if 'href=' in line:

        for media_type, extensions in MEDIA_TYPES.items():

            for extension in extensions:

                if extension in line:

                    media_url = line.split('href="')[-1].split('"')[0]

                    media_file = download_media(f"{url}/{media_url}", media_type)

                    if media_file:

                        media_files[media_type].append(media_file)

# Print the downloaded files

if any(media_files.values()):

    print("The following files have been downloaded:")

    for media_type, files in media_files.items():

        if files:

            print(f"{media_type} files:")

            for file in files:

                print(file)

else:

    print("No media files were found on the website.")

