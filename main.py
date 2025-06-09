import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    try:    
        prompt = sys.argv[1]
        print("Generating text...")
        messages = [genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)]),]

        response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages)
        print(response.text)
        print("Response Usage Metadata:")
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    except IndexError:
        print("Usage: python main.py <prompt>")
        sys.exit(1)

    

if __name__ == "__main__":

    main() 