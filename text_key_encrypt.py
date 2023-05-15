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
