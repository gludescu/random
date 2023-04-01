"""
This script demonstrates how to encrypt a string using the Fernet symmetric encryption scheme from the cryptography library and save the encrypted string to a .env file. It assumes you have a key.key file with the encryption key.

To use this script:

1. Create a key.key file in the same directory as the script, containing the Fernet encryption key.
2. Replace text_to_encrypt with the string you want to encrypt.
3. Install the required package, if not already installed: cryptography.
4. Run the script to encrypt the string and save it in a config.env file.

Here's a commented breakdown of the code:

1. Import the Fernet class from the cryptography.fernet module for encrypting the string using the Fernet symmetric encryption scheme.
2. Read the encryption key from the key.key file and store it in the key variable.
3. Create a Fernet object using the encryption key, stored in the cipher_suite variable.
4. Encode the plaintext string (replace "text_to_encrypt" with the actual text) as UTF-8 bytes and store it in the plaintext variable.
5. Encrypt the plaintext bytes using the Fernet object's encrypt method, and store the encrypted bytes in the ciphertext variable.
6. Save the encrypted string to a config.env file:
   Open (or create) the config.env file in write mode.
   Write the encrypted string to the file by first decoding the encrypted bytes back into a string using the 'utf-8' encoding.
   Close the file to ensure the changes are saved.

To summarize, this script loads an encryption key from a file, encrypts a given string using the Fernet symmetric encryption scheme, and saves the encrypted string to a config.env file.
"""


from cryptography.fernet import Fernet

# Load the key
with open('key.key', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)
plaintext = "text_to_encrypt".encode('utf-8')
ciphertext = cipher_suite.encrypt(plaintext)

# Save the encrypted string to a config file
with open('config.env', 'w') as config_file:
    config_file.write(ciphertext.decode('utf-8'))
