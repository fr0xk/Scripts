# Import libraries
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Define a function to get the article links from the website
def get_article_links(url):
  # Get the HTML content of the website
  response = requests.get(url)
  html = response.text

  # Parse the HTML using BeautifulSoup
  soup = BeautifulSoup(html, "html.parser")

  # Find all the <a> tags with class "article-link"
  links = soup.find_all("a", class_="article-link")

  # Extract the href attribute from each link and prepend the base url
  base_url = "https://stansberryresearch.com"
  article_links = [base_url + link["href"] for link in links]

  # Return the list of article links
  return article_links

# Define a function to get the article title and content from a link
def get_article_content(link):
  # Get the HTML content of the link
  response = requests.get(link)
  html = response.text

  # Parse the HTML using BeautifulSoup
  soup = BeautifulSoup(html, "html.parser")

  # Find the <h1> tag with class "article-title" and get its text
  title = soup.find("h1", class_="article-title").text

  # Find the <div> tag with class "article-content" and get its text
  content = soup.find("div", class_="article-content").text

  # Return the title and content as a tuple
  return (title, content)

# Define a function to summarize an article using HuggingFace pipeline
def summarize_article(article):
  # Initialize the summarization pipeline
  summarizer = pipeline("summarization")

  # Summarize the article and get the first result
  summary = summarizer(article)[0]

  # Return the summary text
  return summary["summary_text"]

# Define a function to index and summarize the latest articles from the website
def index_and_summarize_articles(url):
  # Get the article links from the website
  article_links = get_article_links(url)

  # Create an empty dictionary to store the articles and summaries
  articles_and_summaries = {}

  # Loop through each link
  for link in article_links:
    # Get the article title and content from the link
    title, content = get_article_content(link)

    # Summarize the article content
    summary = summarize_article(content)

    # Store the title, link and summary in the dictionary with title as key
    articles_and_summaries[title] = (link, summary)

  # Return the dictionary of articles and summaries
  return articles_and_summaries

# Define a function to display a menu of articles and summaries for user selection
def display_menu(articles_and_summaries):
  # Print a welcome message
  print("Welcome to the article summarizer!")

  # Print a list of article titles with numbers
  print("Here are the latest articles from https://stansberryresearch.com/articles/:")
  
  titles = list(articles_and_summaries.keys())
  
  for i, title in enumerate(titles):
    print(f"{i+1}. {title}")

  # Ask the user to enter a number to select an article or enter q to quit
  while True:
    choice = input("Enter a number to select an article or enter q to quit: ")

    # If the user enters q, break the loop and exit the program
    if choice.lower() == "q":
      print("Thank you for using the article summarizer!")
      break

    # If the user enters a valid number, show the link and summary of the selected article
    elif choice.isdigit() and int(choice) in range(1, len(titles) + 1):
      index = int(choice) - 1
      
      link, summary = articles_and_summaries[titles[index]]

      print(f"You selected: {titles[index]}")
      print(f"Link: {link}")
      print(f"Summary: {summary}")

    # If the user enters anything else, show an error message and ask again
    else:
      print("Invalid input. Please try again.")

# Main program

# Define the url of the website to scrape articles from
url = "https://stansberryresearch.com/articles/"

# Index and summarize the latest articles from the website
articles_and_summaries = index_and_summarize_articles(url)

# Display a menu of articles and summaries for user selection
display_menu(articles_and_summaries)
