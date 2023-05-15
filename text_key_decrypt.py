import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# Load environment variables from the .env file
load_dotenv("config.env")

# Load the key
with open('key.key', 'rb') as key_file:
    key = key_file.read()

# Load the encrypted string from the environment variable
encrypted_string = os.environ.get('ENCRYPTED_STRING')

# Decrypt the string
cipher_suite = Fernet(key)
decrypted_string = cipher_suite.decrypt(
    encrypted_string.encode('utf-8')).decode('utf-8')

print("Decrypted string:", decrypted_string)
