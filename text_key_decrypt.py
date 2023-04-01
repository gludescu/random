"""
This script demonstrates how to load environment variables, read a key file, and decrypt a string using the Fernet symmetric encryption scheme from the cryptography library.
It assumes you have a .env file containing the encrypted string and a key.key file with the encryption key.

To use this script:

1. Create a config.env file in the same directory as the script, containing the environment variable ENCRYPTED_STRING with the encrypted string you want to decrypt.
2. Create a key.key file in the same directory, containing the Fernet encryption key used to encrypt the string.
3. Install the required packages, if not already installed: python-dotenv and cryptography.
4. Run the script to decrypt the string and display it in the console.

Here's a commented breakdown of the code:

1. Import necessary libraries:
   os for accessing environment variables.
   dotenv for loading environment variables from the .env file.
   Fernet for decrypting the string using the Fernet symmetric encryption scheme.
2. Load environment variables from the config.env file using the load_dotenv function.
3. Read the encryption key from the key.key file and store it in the key variable.
4. Retrieve the encrypted string from the environment variable ENCRYPTED_STRING and store it in the encrypted_string variable.
5. Create a Fernet object using the encryption key, stored in the cipher_suite variable.
6. Decrypt the encrypted string using the Fernet object's decrypt method, and then decode the decrypted bytes back into a string. Store the decrypted string in the decrypted_string variable.
7. Finally, print the decrypted string to the console with a descriptive message.

To summarize, this script loads an encrypted string and its encryption key from separate files, decrypts the string using the Fernet symmetric encryption scheme, and prints the decrypted string to the console.
"""


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
