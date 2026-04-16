def xor(t,k):
    return "".join(chr(ord(t[i]) ^ ord(k[i%len(k)])) for i in range(len(t)))

e = xor("HELLO","KEY")
d = xor(e,"KEY")
print(e,d)