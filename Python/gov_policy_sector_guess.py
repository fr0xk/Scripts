import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

SECTORS_DICT = {
    "Infrastructure": ["Transportation", "Highways", "Ports", "Airports", "Water Supply"],
    "Energy": ["Renewable Energy", "Fossil Fuels", "Nuclear Energy"],
    "Technology": ["Artificial Intelligence", "Wireless Technology", "Software Development", "IT Services"],
    "Healthcare": ["Medical Infrastructure", "Research and Development", "Disease Prevention and Control"],
    "Education": ["Access to Education", "Scientific Research and Innovation"],
    "Agriculture": ["Sustainable Agriculture", "Rural Development"],
}

def download_nltk_libraries():
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('vader_lexicon')

def get_impacted_sectors(statement):
    keywords = [token.lower() for token in word_tokenize(statement) if token.isalpha() and token.lower() not in stopwords.words('english')]
    return set(sector for sector, subsectors in SECTORS_DICT.items() for keyword in keywords
               if keyword in sector.lower() or any(keyword in subsector.lower() for subsector in subsectors))

def guess_sector(statement):
    sentiment_scores = SentimentIntensityAnalyzer().polarity_scores(statement)
    return ["Technology", "Energy", "Infrastructure"][int(sentiment_scores['compound'] <= -0.05) + int(sentiment_scores['compound'] > 0.05)]

def main():
    try:
        stopwords.words('english')
    except LookupError:
        download_nltk_libraries()

    statement = input("Enter a statement related to government policies: ")
    impacted_sectors = get_impacted_sectors(statement)

    if not impacted_sectors:
        guessed_sector = guess_sector(statement)
        print(f"No potential sectors found based on the given statement. Guessing that the statement is related to the {guessed_sector} sector.")
    else:
        print("Potential sectors impacted by government policies for the given statement:")
        print(*("- " + sector for sector in impacted_sectors), sep="\n")

if __name__ == "__main__":
    main()

