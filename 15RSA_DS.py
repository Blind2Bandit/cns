p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
m = int(input("Enter message (integer): "))
e = int(input("Enter public exponent e: "))

# 1. Key Generation
n, phi = p * q, (p - 1) * (q - 1)
d = pow(e, -1, phi)  # Instantly calculates modular inverse

# 2. Signature & Verification
signature = pow(m, d, n)
verify = pow(signature, e, n)

# 3. Output
print(f"\n=== RSA Signature ===")
print(f"Public Key: ({e}, {n}) | Private Key: ({d}, {n})")
print(f"Signature: {signature}")
print(f"Verification: {verify == m}")