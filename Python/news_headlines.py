import requests
from bs4 import BeautifulSoup
from typing import List, Set

# Define the URLs of the news sources you want to scrape headlines from
NEWS_SOURCES: List[str] = [
    'https://www.bbc.com/news',
    'https://www.reuters.com/',
    'https://edition.cnn.com/',
    'https://www.aljazeera.com/news/',
    'https://timesofindia.indiatimes.com/',
    'https://indianexpress.com/',
    'https://www.ndtv.com/'
]

# Define a function to fetch headlines from a news source URL
def fetch_headlines(source: str, headlines: Set[str]) -> Set[str]:
    try:
        # Send a request to the URL and get the HTML content
        response = requests.get(source)
        content = response.content

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')

        # Find all the headline elements on the page and extract their text
        headlines_on_page = list(map(lambda h: h.text.strip(), soup.find_all('h3')))

        # Add any new headlines to the headlines set and return it
        return headlines.union(set(headlines_on_page))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching headlines from {source}: {e}")
        return headlines

# Fetch headlines from each news source URL and combine them into a set
headlines: Set[str] = set()
for source in NEWS_SOURCES:
    headlines = fetch_headlines(source, headlines)

# Print the resulting set of headlines
for headline in headlines:
    print(headline)
