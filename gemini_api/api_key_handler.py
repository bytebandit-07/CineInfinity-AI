from cryptography.fernet import Fernet

def load_api_key():
    with open("fernet.key", "rb") as key_file:
        fernet_key = key_file.read()
    fernet = Fernet(fernet_key)

    with open("encrypted_api_key.txt", "rb") as enc_file:
        encrypted_key = enc_file.read()
    return fernet.decrypt(encrypted_key).decode()
