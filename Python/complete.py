import openai
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate text using OpenAI GPT-3')
parser.add_argument('--model', help='The name of the GPT-3 model to use', default='text-davinci-002')
parser.add_argument('--max-tokens', help='The maximum number of tokens to generate', type=int, default=1024)
args = parser.parse_args()

# Prompt the user for the text to generate
prompt = input('Enter the text to generate: ')

# Set up the OpenAI API client
openai.api_key = "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"
model_engine = args.model

# Generate the completion
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=args.max_tokens
)

# Print the generated text
message = completions.choices[0].text
print(message)

