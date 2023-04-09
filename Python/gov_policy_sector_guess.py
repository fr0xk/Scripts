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
    impacted_sectors = set()
    for sector, subsectors in SECTORS_DICT.items():
        if any(keyword in sector.lower() or keyword in subsector.lower() for keyword in keywords for subsector in subsectors):
            impacted_sectors.add(sector)
    return impacted_sectors

def guess_sector(statement):
    sentiment_scores = SentimentIntensityAnalyzer().polarity_scores(statement)
    if sentiment_scores['compound'] <= -0.05:
        return "Infrastructure"
    elif sentiment_scores['compound'] > 0.05:
        return "Technology"
    else:
        return "Energy"

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
        for sector in impacted_sectors:
            print(f"- {sector}")

if __name__ == "__main__":
    main()

