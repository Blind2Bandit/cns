# Setup (Prime p, Primitive Root g, Private Key x)
p, g, x = 107, 2, 45 
y = pow(g, x, p)  # Calculate Public Key

# Message (m) and random ephemeral key (k)
m, k = 66, 23 

# --- Encryption ---
# c1 = g^k mod p,  c2 = m * y^k mod p
c1, c2 = pow(g, k, p), (m * pow(y, k, p)) % p

# --- Decryption ---
# Multiply c2 by the modular inverse of (c1^x mod p)
plain = (c2 * pow(pow(c1, x, p), -1, p)) % p

print(f"Public Key: (p={p}, g={g}, y={y})")
print(f"Encrypted: ({c1}, {c2})")
print(f"Decrypted: {plain}")