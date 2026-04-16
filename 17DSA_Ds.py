p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
g = int(input("Enter generator g: "))
x = int(input("Enter private key x: "))
m = int(input("Enter message (integer): "))

# 1. Generate Public Key
y = pow(g, x, p)

# 2. Choose random k and generate signature (r, s)
k = int(input("Enter random k: "))
r = pow(g, k, p) % q
s = (pow(k, -1, q) * (m + x * r)) % q

# 3. Verification
w = pow(s, -1, q)
u1, u2 = (m * w) % q, (r * w) % q
v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

# 4. Output
print(f"\n=== DSA Signature ===")
print(f"Public Key: (p={p}, q={q}, g={g}, y={y}) | Private Key: {x}")
print(f"Signature: ({r}, {s})")
print(f"Verification: {v == r}")