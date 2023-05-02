import argparse
import openai

def generate_completion(prompt, api_key, model):
    openai.api_key = api_key
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate text completion using OpenAI's GPT-2 model")
    parser.add_argument("prompt", type=str, help="Input prompt for GPT-2 model")
    parser.add_argument("--api-key", type=str, help="OpenAI API key")
    parser.add_argument("--model", type=str, default="text-davinci-002", help="GPT-2 model to use")
    args = parser.parse_args()

    api_key = args.api_key or openai.api_key
    if not api_key:
        print("Error: No OpenAI API key provided. Please provide an API key using the --api-key option or set it as the OPENAI_API_KEY environment variable.")
        exit(1)

    # Check for potential vulnerability in API key
    if "sk_" in api_key:
        print("Warning: Your OpenAI API key appears to be a secret key. Please use an API key with only permissions necessary for your use case.")
    
    try:
        message = generate_completion(args.prompt, api_key, args.model)
        print(message)
    except openai.Error as e:
        print(f"OpenAI API error: {e}")
        exit(1)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

