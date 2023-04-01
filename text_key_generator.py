"""
This script demonstrates how to generate a Fernet symmetric encryption key using the cryptography library and save it to a file.

To use this script:

1. Install the required package, if not already installed: cryptography.
2. Run the script to generate a new Fernet key and save it in a key.key file.

Here's a commented breakdown of the code:

1. Import the Fernet class from the cryptography.fernet module for generating the Fernet symmetric encryption key.
2. Generate a new Fernet key using the generate_key() method and store it in the key variable.
3. Save the generated key to a file:
   Open (or create) the key.key file in write-binary mode, as the key is a bytes object.
   Write the key to the file.
   Close the file to ensure the key is saved.
   
To summarize, this script generates a new Fernet symmetric encryption key using the cryptography library and saves it to a key.key file.
"""


from cryptography.fernet import Fernet

key = Fernet.generate_key()

# Save the key to a file
with open('key.key', 'wb') as key_file:
    key_file.write(key)
