import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def generate_text(contents=None, model= "gemini-2.0-flash-001"):
    """Generate text using the Gemini API."""
    response = client.models.generate_content(
        model=model,
        contents=contents
    )
    return response

def main():
    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    print("Generating text...")
    response = generate_text(prompt)
    print("Generated Text:")
    print(response.text)
    print("Response Usage Metadata:")
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

if __name__ == "__main__":
    main()