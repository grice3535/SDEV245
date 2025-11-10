

alphabets = 'abcdefghijklmnopqrstuvwxyz'
shift = 4

# Create the shifted alphabet
rearranged = alphabets[shift:] + alphabets[:shift]

def encrypt(message):
    result = ""
    for char in message.lower():
        if char in alphabets:
            index = alphabets.index(char)
            result += rearranged[index]
        else:
            result += char
    return result

def decrypt(message):
    result = ""
    for char in message.lower():
        if char in rearranged:
            index = rearranged.index(char)
            result += alphabets[index]
        else:
            result += char
    return result
    
# Examples
text = "hello world"
encrypted = encrypt(text)
decrypted = decrypt(encrypted)

print("Original: ", text)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)