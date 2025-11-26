'''
Program Name: Midterm
Author: Gillian Rice
Date: November 26, 2025
Description:
    My program keeps things confidential by using AES encryption, so only someone with
    the right password can actually read the message. To make sure the message is not
    changed, I hash it with SHA-256 before encrypting and then hash it again after 
    decrypting to check that both hashes match, and AES-GCM also warns if anything was
    tampered with. It’s also easy to run and doesn’t require anything complicated, so 
    it stays available for whoever needs to use it. The random salt and nonce give the
    program good entropy so the encryption isn’t predictable, and PBKDF2 turns the 
    password into a strong key, which makes the whole process more secure.
'''

import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

# SHA-256 Hashing

def sha(message, bits=256):
    bits = int(bits)
    encoded_string = message.encode("utf-8")
    hashed_string = getattr(hashlib, f"sha{bits}")
    hasher = hashed_string()
    hasher.update(encoded_string)
    return hasher.hexdigest()

# AES Encrypt + Decrypt

def aes_encrypt_decrypt(message, password):
    # Derive key using PBKDF2 (your parameters kept the same)
    salt = get_random_bytes(16)
    password_bytes = password.encode('utf-8')

    key = PBKDF2(password_bytes, salt, dkLen=32, count=100000, hmac_hash_module=SHA256)

    # Encrypt
    cipher = AES.new(key, AES.MODE_GCM)
    encrypted_message, tag = cipher.encrypt_and_digest(message.encode("utf-8"))
    nonce = cipher.nonce

    # Decrypt
    decrypt = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decrypted_message = decrypt.decrypt_and_verify(encrypted_message, tag)

    return encrypted_message, decrypted_message.decode("utf-8")

# Main Program

message = input("Enter a message: ")
password = input("Enter a password: ")

print("\n--- Hashing Message (SHA-256) ---")
original_hash = sha(message, 256)
print("Hash:", original_hash)

print("\n--- Encrypting Message (AES) ---")
ciphertext, decrypted_text = aes_encrypt_decrypt(message, password)
print("Ciphertext:", ciphertext)

print("\n--- Decrypted Message ---")
print("Decrypted:", decrypted_text)

print("\n--- Integrity Check ---")
new_hash = sha(decrypted_text, 256)

if original_hash == new_hash:
    print("Integrity Verified: HASHES MATCH")
else:
    print("Integrity FAILED: HASHES DO NOT MATCH")