from cryptography.fernet import Fernet

# Generate a Fernet key (run this only once and reuse it later)
fernet_key = Fernet.generate_key()
with open("fernet.key", "wb") as key_file:
    key_file.write(fernet_key)

# Your Gemini API key here (REPLACE THIS WITH YOUR ACTUAL API KEY)
api_key = "your api key"

# Encrypt the API key
fernet = Fernet(fernet_key)
encrypted_key = fernet.encrypt(api_key.encode())

# Save encrypted key to file
with open("encrypted_api_key.txt", "wb") as enc_file:
    enc_file.write(encrypted_key)

print("✅ API key encrypted and saved.")
