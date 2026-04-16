text = "HELLO"
key = "KEY"

enc = ""
dec = ""

# Encryption
for i in range(len(text)):
    enc += chr((ord(text[i]) - 65 + ord(key[i % len(key)]) - 65) % 26 + 65)

# Decryption
for i in range(len(enc)):
    dec += chr((ord(enc[i]) - 65 - (ord(key[i % len(key)]) - 65)) % 26 + 65)

print("Encrypted:", enc)
print("Decrypted:", dec)