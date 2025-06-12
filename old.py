import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client  = genai.Client(api_key=api_key)

messages = [
        types.Content(role="user",parts=[types.Part(text=sys.argv[1])])
        ]

verbose = "--verbose" in sys.argv
args = [arg for arg in sys.argv[1:] if not  arg.startswith("--")]

if not args:
    print("AI Assistant")
    print("Make sure to ask a question")
    exit(1)

user_prompt = " ".join(args)

if verbose:
    print(f"User prompt: {user_prompt}\n")

#I might want to move the message down to here later
response = client.models.generate_content(model="gemini-2.0-flash-001",contents=messages)

if verbose:
    print(f"Prompt tokes: {response.usage_metadata.prompt_token_count}")
    print(f"{response.usage_metadata.candidates_token_count}")
print("Response:")
print(response.text)
