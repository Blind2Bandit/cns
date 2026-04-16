import hashlib

text = input("Enter text: ")

# SHA-1
sha1_hash = hashlib.sha1(text.encode()).hexdigest()

# SHA-512
sha512_hash = hashlib.sha512(text.encode()).hexdigest()

# MD 5
mac = hashlib.md5(text.encode()).hexdigest()