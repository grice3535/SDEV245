'''
Program Name: RSA
Author: Gillian Rice
Date: November 9, 2025
Description:
    This program runs a short word, encrypting it and decryting it using asymmetric methods.
'''

import math

# pick 2 prime numbers
p = 3
q = 7
message = 10
n = p * q

totient = (p-1)*(q-1)

for i in range(2, totient):
    if math.gcd(i, totient)==1:
        e = i
        break

# encrypting the message before displaying the public keys

c = m**e % n

print(f"public keys: ({e}, {n})")
print(f"cipher text: ({c})")

# finding d which is any number that when you multiply e, mod phi of n, will give you 1

for j in range(1,100):
    if (j * e) % totient == 1:
        d = j
        break

print (f"d is: {d}")

plaintext = c ** d % n

print(f"Plaintext: {plaintext}")

