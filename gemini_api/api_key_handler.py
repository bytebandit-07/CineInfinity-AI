import os
from cryptography.fernet import Fernet


def load_api_key():
    """
    Securely loads and decrypts the API key.

    This function constructs absolute paths to the key files, making it
    robust to changes in the current working directory. It will raise
    a FileNotFoundError if the required key files are not found in the
    same directory as this script.
    """
    try:
        # Determine the directory where this script is located
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Build absolute paths to the necessary files
        key_path = os.path.join(base_dir, 'fernet.key')
        encrypted_path = os.path.join(base_dir, 'encrypted_api_key.txt')

        # Fail fast with a clear error message if either file is missing
        if not os.path.isfile(key_path):
            raise FileNotFoundError(f"Encryption key not found at the expected path: {key_path}")
        if not os.path.isfile(encrypted_path):
            raise FileNotFoundError(f"Encrypted API key file not found at the expected path: {encrypted_path}")

        # Load the fernet key used for encryption
        with open(key_path, 'rb') as kf:
            fernet_key = kf.read()

        f = Fernet(fernet_key)

        # Load the encrypted API key
        with open(encrypted_path, 'rb') as ef:
            encrypted_api_key = ef.read()

        # Decrypt the API key and return it as a string
        decrypted_key = f.decrypt(encrypted_api_key).decode('utf-8')
        return decrypted_key

    except FileNotFoundError as e:
        print(f"ERROR: A required file was not found. {e}")
        # Depending on your application's needs, you might want to exit or return None
        raise  # Re-raising the exception is often a good choice
    except Exception as e:
        print(f"An unexpected error occurred while loading the API key: {e}")
        raise