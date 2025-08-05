def encrypt_message(message, key):
    result = []
    for i, char in enumerate(message):
        shift = ord(key[i % len(key)]) % 5 + 1
        xor_char = (ord(char) + shift) ^ ord(key[i % len(key)])
        result.append(xor_char)
    return bytes(result)  # Return as bytes for safe output

def decrypt_message(encrypted_bytes, key):
    result = []
    for i, byte in enumerate(encrypted_bytes):
        xor_val = byte ^ ord(key[i % len(key)])
        shift = ord(key[i % len(key)]) % 5 + 1
        original_char = chr(xor_val - shift)
        result.append(original_char)
    return ''.join(result)

# ===============================
# DEMONSTRATION
# ===============================
original_message = "The highest bidding price is 406714 NZ$"
secret_key = "Key42"

encrypted_message = encrypt_message(original_message, secret_key)
decrypted_message = decrypt_message(encrypted_message, secret_key)

# Output to console
print("Original message:", original_message)
print("Encrypted message (hex):", encrypted_message.hex())
print("Decrypted message:", decrypted_message)
