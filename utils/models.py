"""
Model Initialization File

Configures the LLM model used throughout the project.
Provider: Google Gemini (needs GOOGLE_API_KEY in .env).
"""

from dotenv import load_dotenv
load_dotenv(override=True)

from langchain.chat_models import init_chat_model

# Only ONE `model =` line should exist in this file.
# If you hit 429 rate limits, try "google_genai:gemini-2.5-flash-lite".
model = init_chat_model("google_genai:gemini-3.8-flash")