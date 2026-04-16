p = int(input("Enter prime p: "))
g = int(input("Enter primitive root g: "))
a = int(input("Enter private key of A: "))
b = int(input("Enter private key of B: "))

# Using Python's built-in pow() for modular exponentiation
A = pow(g, a, p)
B = pow(g, b, p)

keyA = pow(B, a, p)
keyB = pow(A, b, p)

print("Public key of A:", A)
print("Public key of B:", B)
print("Shared key (computed by A):", keyA)
print("Shared key (computed by B):", keyB)


p, g = 997, 2  # Public Prime and Base
a, b, c = 12, 15, 19  # Private keys: Alice, Bob, Carol

# Round 1: Generate & broadcast public keys
A, B, C = pow(g, a, p), pow(g, b, p), pow(g, c, p)

# Round 2: Pass keys in a circle (A->B, B->C, C->A) and exponentiate
# Bob computes A^b, Carol computes B^c, Alice computes C^a
AB, BC, CA = pow(A, b, p), pow(B, c, p), pow(C, a, p)

# Round 3: Pass intermediate keys in a circle again and compute final key
# Carol computes (A^b)^c, Alice computes (B^c)^a, Bob computes (C^a)^b
key_C, key_A, key_B = pow(AB, c, p), pow(BC, a, p), pow(CA, b, p)

print(f"Shared Keys: Alice={key_A}, Bob={key_B}, Carol={key_C}")


p, g = 997, 2
a, b, eve = 12, 15, 99 # Private keys: Alice, Bob, Eve

# 1. Alice and Bob generate public keys to send to each other
A, B = pow(g, a, p), pow(g, b, p)

# 2. Eve intercepts A and B, and sends her OWN public key (E) to both
E = pow(g, eve, p)

# 3. Alice and Bob compute shared keys (tricked into using Eve's public key)
key_A = pow(E, a, p) # Alice thinks this key is for Bob
key_B = pow(E, b, p) # Bob thinks this key is for Alice

# 4. Eve computes both shared keys (using the intercepted A and B)
eve_key_A = pow(A, eve, p) # Eve's link to Alice
eve_key_B = pow(B, eve, p) # Eve's link to Bob

# Proof that Eve has successfully hijacked both sides of the connection:
print(f"Alice's Key: {key_A} == Eve's Key for Alice: {eve_key_A}")
print(f"Bob's Key:   {key_B} == Eve's Key for Bob:   {eve_key_B}")