def caesar(t,k):
    return "".join(chr((ord(c)-65+k)%26+65) for c in t)

e = caesar("HELLO",3)
d = caesar(e,-3)
print(e,d)

