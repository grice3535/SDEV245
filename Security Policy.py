'''
Program Name: Security Policy
Author: Gillian Rice
Date: December 1, 2025
Description:
    This project analyzes vulnerable Python code samples and applies minimal-change fixes 
    to address several OWASP Top 10 security risks. Each example includes an explanation 
    of the vulnerability, a corrected secure version of the code, and references to 
    relevant OWASP categories.
'''

# 1.

"""
1. ShA-1 is a weak hashing algorithm
2. No salt is used
3. SHA-1 is cryptography broken

If an attacker gets the stored_hash values, they can run offline brute-force attacks
 without rate limits use rainbow tables since there is no saalt, and immediatly identify 
 users with the same password.
"""

from argon2 import PasswordHasher

_ph = PasswordHasher()

def hash_password(password: str) -> str:
    return _ph.hash(password)

def verify_password(password: str, stored_hash: str) -> bool:
    try:
        return _ph.verify(stored_hash, password)
    except Exception:
        return False
    
'''
Argon2 automatically generates a cryptography secure random salt.

Work factor increases attack cost because Argon2 uses configured parameters.
Which are time_cost, memory_cost, and parallelism. Making brute-force attacks slow and expensive.

OWASP Top 10: A02 - Crptographic Failures
OWASP Password Storage Cheat Sheet
'''

# 2.
'''
This line is unsafe:
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
'''

import sqlite3
from getpass import getpass

def login():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()

    username = input("Username: ")
    password = getpass("Password: ")

    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cur.execute(query, (username, password))

    row = cur.fetchone()

    if row:
        print("Login successful!")
    else:
        print("Invalid username or password.")

    conn.close()

if __name__ == "__main__":
    login()

'''
OWASP Top 10: A03 - Injection

This is dangerous since attackers can retrieve all users, modify or delete tables, 
bypass authentication, and install backdoors or escalate privleges.
'''

# 3.

'''
Hardcoding API keys is a security issue by numerous means. For exapmle, the keys can end up 
in Git history, developer laptops, logs, and CI/CD artifacts. Anybody who has access, could 
preform frudulanlent charges, refund abuse, API takeover, or data extraction.

If the key is leaked, attackers can charge credit cards fraudulently, steal customer data,
max out quatas, leading to operational or financial damage, or sell the leaked API keys 
on breach forums.
'''

import os
import requests

API_KEY = os.getenv("PAYMENT_API_KEY")
BASE_URL = "https://api.payment-provider.example/v1"

def charge_customer(customer_id, amount_cents):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"customer": customer_id, "amount": amount_cents}
    response = requests.post(f"{BASE_URL}/charge", headers=headers, json=data)
    print("Status:", response.status_code)
    print("Response:", response.text)

'''
OWASP Top 10: A05 - Security Misconfiguration

Embedding secrets in code is a misconfiguration of how sensitice settings should be managed, and 
it significatly increases the risk of data breaches or unaothrixed access to external services.
'''