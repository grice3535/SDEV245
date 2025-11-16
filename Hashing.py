'''
Program Name: Secure Hashing
Author: Gillian Rice
Date: November 16, 2025
Description:
    This program takes a string and outputs its SHA hash.
'''

import hashlib

string = "Hello"

def sha(message, bits=256):
    """
    Takes a string and SHA type returns its SHA hash.
    """
    # Ensures bits is an integer
    bits = int(bits)

    # Encode string so readable by machine
    encoded_string = message.encode("utf-8")

    # Generate hash
    hashed_string = getattr(hashlib, f"sha{bits}")

    # Create a hash object
    hasher = hashed_string()

    # Update has with the string you want to hash
    hasher.update(encoded_string)

    # Convert output to hexadecimal
    print(hasher.hexdigest())

sha("hello", "256")