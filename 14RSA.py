# Setup: Primes (p, q), Public Exponent (e), and Message (m)
p, q, e, m = 61, 53, 17, 65 

# 1. Key Generation
n, phi = p * q, (p - 1) * (q - 1)
d = pow(e, -1, phi) # The magic step: finds private key instantly

# 2. Encryption & Decryption
cipher = pow(m, e, n)
plain = pow(cipher, d, n)

print(f"Public Key: ({e}, {n}) | Private Key: ({d}, {n})")
print(f"Original: {m} -> Encrypted: {cipher} -> Decrypted: {plain}")