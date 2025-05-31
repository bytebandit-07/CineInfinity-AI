from google import genai
from google.genai import types
from api_key_handler import load_api_key

# Initialize Gemini client
api_key = load_api_key()
client = genai.Client(api_key=api_key)

def get_movie_description(movie_title: str) -> str:
    prompt = f"Give a one-line summary of the movie titled '{movie_title}'."

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        ),
    ]

    config = types.GenerateContentConfig(response_mime_type="text/plain")

    try:
        full_response = ""
        for chunk in client.models.generate_content_stream(
            model="gemini-2.0-flash",
            contents=contents,
            config=config,
        ):
            if chunk.text:
                full_response += chunk.text
        return full_response.strip()
    except Exception as e:
        return f"❌ Error: {e}"

