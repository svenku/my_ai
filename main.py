import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    try:    
        args = sys.argv
        prompt = args[1]

        messages = [
            genai.types.Content(role="user", 
                                parts=[genai.types.Part(text=prompt)]),
        ]   
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages)

        if len(args) == 3 and args[2] == "--verbose":
            print(f'User prompt: {prompt}')
            print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
            print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
        print(response.text)
    except IndexError:
        print("Usage: python main.py <prompt>")
        sys.exit(1)

    

if __name__ == "__main__":
    main() 