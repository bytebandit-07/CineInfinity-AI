# File: gemini_api/extract_movie_description.py

from google import genai
from gemini_api.api_key_handler import load_api_key

# --- Initialization ---
try:
    api_key = load_api_key()
    # Use the genai.Client() method which is compatible with your library version
    client = genai.Client(api_key=api_key)
    print("✅ Gemini client initialized successfully.")
except Exception as e:
    client = None
    print(f"❌ CRITICAL ERROR: Failed to initialize Gemini client. Check API key. Error: {e}")


def get_movie_description(movie_title: str) -> str:
    """
    Generates a one-line description for a given movie title using the Gemini API.
    """
    if not client:
        return "Error: Gemini client is not available."

    prompt = f"Give a one-line description for the movie titled '{movie_title}'. Be concise and engaging."

    try:
        # Use the client.models.generate_content_stream method and the correct model name
        full_response = ""
        for chunk in client.models.generate_content_stream(
                # Use the correct model name we found with your list_models.py script
                model="models/gemini-1.5-flash-latest",
                contents=prompt
        ):
            if chunk.text:
                full_response += chunk.text

        return full_response.strip().replace('*', '')

    except Exception as e:
        print(f"❌ An error occurred while generating content for '{movie_title}': {e}")
        return "Description not available at this time."