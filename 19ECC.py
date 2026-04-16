# 1. Setup Curve Parameters
p = int(input("Enter prime p: "))
a = int(input("Enter curve parameter a: "))
b = int(input("Enter curve parameter b: "))

# One-liner to find all points using list comprehension
# We use `None` to represent the point at infinity (O)
points = [(x, y) for x in range(p) for y in range(p) if (y*y) % p == (x**3 + a*x + b) % p] + [None]
print(f"\nAll points on curve:\n{points}")

# 2. Point Addition & Scalar Multiplication
def add(P, Q):
    if not P or not Q: return P or Q  # If either is infinity (None), return the other
    x1, y1 = P; x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0: return None # P + (-P) = Infinity
    
    try:
        # Calculate slope (m) instantly using pow(..., -1, p)
        m = ((3*x1**2 + a) * pow(2*y1, -1, p)) % p if P == Q else ((y2 - y1) * pow(x2 - x1, -1, p)) % p
        x3 = (m**2 - x1 - x2) % p
        return (x3, (m*(x1 - x3) - y1) % p)
    except ValueError: return None

def mult(k, P):
    R = None
    while k:
        if k & 1: R = add(R, P) # Bitwise check for odd numbers
        P = add(P, P)
        k >>= 1                 # Bitwise integer division by 2
    return R

# 3. Keys & Inputs
G = (int(input("\nEnter Base Gx: ")), int(input("Enter Base Gy: ")))
d = int(input("Enter private key d: "))
Q = mult(d, G)
print(f"Public Key: {Q}")

M = (int(input("\nEnter Message Mx: ")), int(input("Enter Message My: ")))
k = int(input("Enter random k: "))

# 4. Encryption
C1, C2 = mult(k, G), add(M, mult(k, Q))
print(f"\nCipher Text: C1={C1}, C2={C2}")

# 5. Decryption
S = mult(d, C1)
S_inv = None if not S else (S[0], -S[1] % p) # Inverse of point (x, y) is (x, -y mod p)
M_dec = add(C2, S_inv)

print(f"\nDecrypted Message: {M_dec}")