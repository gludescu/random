from cryptography.fernet import Fernet

key = Fernet.generate_key()

# Save the key to a file
with open('key.key', 'wb') as key_file:
    key_file.write(key)
