import argparse

import random

from typing import List, Dict

import openai

openai.api_key = "YOUR_API_KEY"

common_phrases = [

    "OMG, ", "Like, ", "Totally, ", "I can't even, ",

    "Literally, ", "So, like, ", "Oh my gosh, ", "As if, ",

    "No way, ", "For realsies, "

]

replace_words = {

    'awesome': ['amazeballs', 'lit', 'sick'],

    'cool': ['dope', 'chill', 'rad'],

    'great': ['amazing', 'awesome', 'fantabulous'],

    'good': ['legit', 'solid', 'bomb'],

    'bad': ['awful', 'terrible', 'lame'],

    'crazy': ['insane', 'bananas', 'nuts'],

    'funny': ['hilarious', 'LOL', 'ROFL'],

    'party': ['turn-up', 'shindig', 'banger']

}

def get_random_word(word_list: List[str]) -> str:

    return random.choice(word_list)

def rephrase_word(word: str) -> str:

    if not word.isalpha():

        return word

    if random.random() < 0.5:

        return word

    word = word.lower()

    if word in replace_words:

        return get_random_word(replace_words[word])

    else:

        return word + random.choice(common_phrases)

def rephrase_line(line: str) -> str:

    return ''.join(map(lambda word: rephrase_word(word), line.split()))

def rephrase_text(text: str) -> str:

    response = openai.Completion.create(

        engine="text-davinci-002",

        prompt=text,

        max_tokens=1024,

        n=1,

        stop=None,

        temperature=0.7,

    )

    return response.choices[0].text

def rephrase_file(input_file: str, output_file: str) -> None:

    with open(input_file) as f:

        with open(output_file, 'w') as out:

            for line in f.readlines():

                out.write(rephrase_line(line))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Rephrase input text files or text strings.')

    parser.add_argument('input', type=str, nargs='+', help='Input text files or text strings')

    parser.add_argument('-o', '--output', type=str, help='Output file name')

    args = parser.parse_args()

    for input_data in args.input:

        if input_data.endswith('.txt'):

            # Input is a file

            output_file = args.output or input_data.split('.')[0] + '_rephrased.txt'

            rephrase_file(input_data, output_file)

        else:

            # Input is a text string

            output_string = rephrase_text(input_data)

            print(output_string)

