import google.generativeai as genai
from api_key_handler import load_api_key

print("Attempting to load API key and list available models...")

try:
    # Load your API key securely
    api_key = load_api_key()
    genai.configure(api_key=api_key) # Use the configure method for initialization

    print("\n--- Available Models ---")
    # Iterate through the models and print their names
    for m in genai.list_models():
        # We only care about models that support the 'generateContent' method
        if 'generateContent' in m.supported_generation_methods:
            print(f"Model Name: {m.name}")
    print("------------------------")
    print("\nPlease use one of the model names listed above in your 'extract_movie_description.py' file.")

except Exception as e:
    print(f"\n❌ An error occurred. This could be due to an incorrect API key or other issue.")
    print(f"Error details: {e}")