from cryptography.fernet import Fernet, InvalidToken
import os
import time

# Generates a key for encryption
def generate_key():
    return(Fernet.generate_key().decode('utf-8'))

# Encrypts a given file with the user's given key
def encrypt_file(input_file, key):
    fernet = Fernet(key)

    with open(input_file, 'rb') as file:
        plain_text = file.read()

    with open(input_file, 'wb') as file:
        cipher_text = fernet.encrypt(plain_text)
        file.write(cipher_text)

# Decrypts a given file with the user's given key
def decrypt_file(input_file, key):
    fernet = Fernet(key)

    with open(input_file, 'rb') as file:
        cipher_text = file.read()
    try:
        with open(input_file, 'wb') as file:
            plain_text = fernet.decrypt(cipher_text)
            file.write(plain_text)
    except:
        with open(input_file, 'wb') as file:
            file.write(cipher_text)
        raise InvalidToken("Invalid decryption key or file already decrypted.")


