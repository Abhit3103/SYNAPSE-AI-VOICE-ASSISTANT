from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

class AIEngine:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY not found")

        self.client = genai.Client(api_key=api_key)

    def ask(self, command):
        try:
            response = self.client.models.generate_content(
                model="models/gemini-1.5-flash-latest",
                contents=command
            )
            return response.text
        except Exception as e:
            print("GEMINI ERROR:", e)
            return "Sorry, Gemini AI is not available right now."
