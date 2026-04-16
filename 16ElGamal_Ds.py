import math

p = int(input("Enter prime p: "))
g = int(input("Enter generator g: "))
x = int(input("Enter private key x: "))
m = int(input("Enter message (integer): "))

# 1. Generate Public Key
y = pow(g, x, p)

# 2. Choose random k coprime to p-1
k = int(input("Enter random k: "))
while math.gcd(k, p - 1) != 1:
    k += 1

# 3. Generate Signature (r, s)
r = pow(g, k, p)
s = (pow(k, -1, p - 1) * (m - x * r)) % (p - 1)

# 4. Verification
left = pow(g, m, p)
right = (pow(y, r, p) * pow(r, s, p)) % p

print(f"\n=== ElGamal Signature ===")
print(f"Public Key: ({p}, {g}, {y}) | Private Key: {x}")
print(f"Signature: ({r}, {s})")
print(f"Verification: {left == right}")