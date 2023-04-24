from transformers import pipeline, PipelineException
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# download nltk resources
nltk.download('popular', quiet=True)

# load NLP pipeline
try:
    nlp = pipeline("zero-shot-classification")
except PipelineException:
    print('Unable to load NLP pipeline.')
    exit()

# define sectors and keywords
sectors = ['Automobile', 'Banking', 'Cement', 'Consumer Durables', 'Energy', 'FMCG', 'Healthcare', 'IT', 'Media & Entertainment', 'Metal', 'Oil & Gas', 'Pharmaceuticals', 'Realty', 'Services', 'Telecom', 'Textiles']

keywords = {
    'Automobile': 'car, vehicle, auto, tyre, motor',
    'Banking': 'bank, loan, interest rate, credit, debit',
    'Cement': 'cement, concrete, construction, infrastructure, building',
    'Consumer Durables': 'electronics, home appliance, furniture, household goods, kitchenware',
    'Energy': 'oil, gas, renewable, electricity, power',
    'FMCG': 'food, beverage, personal care, home care, cleaning',
    'Healthcare': 'pharmaceutical, medical device, hospital, clinic, wellness',
    'IT': 'software, hardware, computer, internet, technology',
    'Media & Entertainment': 'movies, music, TV, radio, gaming',
    'Metal': 'steel, aluminium, copper, iron, metal fabrication',
    'Oil & Gas': 'oil, gas, refinery, exploration, production',
    'Pharmaceuticals': 'drug, medicine, vaccine, research, development',
    'Realty': 'real estate, property, construction, housing, apartment',
    'Services': 'transportation, logistics, hospitality, consulting, education',
    'Telecom': 'telecommunication, mobile, broadband, satellite, network',
    'Textiles': 'clothing, fabrics, apparel, fashion, yarn'
}

# preprocess text
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())
    filtered_words = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_words)

# predict sector based on text input
def predict_sector(text):
    try:
        text = preprocess(text)
        scores = nlp(text, sectors, multi_label=True)
        max_score = 0
        predicted_sector = None
        for i in range(len(sectors)):
            score = scores['scores'][i]
            if score > max_score:
                max_score = score
                predicted_sector = sectors[i]
        return predicted_sector
    except (PipelineException, ValueError):
        print('Unable to predict sector.')
        exit()

# check for potential SQL injection attack
def check_sql_injection(text):
    sql_injection_regex = re.compile(r'\'\s*or\s*\'|\"\s*or\s*\"|\s*;|\s*--')
    if sql_injection_regex.search(text):
        print('Potential SQL injection attack detected.')
        exit()

# check for potential XSS attack
def check_xss(text):
    xss_regex = re.compile(r'<script|<img|<a\s+href')
    if xss_regex.search(text):
        print('Potential XSS attack detected.')
        exit()

# get user input and predict sector
text = input('Enter text: ')
check_sql_injection(text)
check_xss(text)
predicted_sector = predict

# Print predicted sector
if predicted_sector: 
    print('Predicted sector: ', predicted_sector)
else: 
    print('Unable to predict sector.')
