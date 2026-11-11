import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

env_path = Path(__file__).parent / ".env"
print("Script folder:", Path(__file__).parent)
print(".env exists:", env_path.exists())

load_dotenv(env_path, override=True)   

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=api_key)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)