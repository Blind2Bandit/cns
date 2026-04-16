

def ext_gcd(a, b):
    if b == 0: return a, 1, 0
    g, x, y = ext_gcd(b, a % b)
    return g, y, x - (a // b) * y

a = int(input())
b = int(input())
g, x, y = ext_gcd(a,b)
print(f"GCD: {g}, x: {x}, y: {y}") 