def aff_e(t,a,b):
    return "".join(chr((a*(ord(c)-65)+b)%26+65) for c in t)

def aff_d(t,a,b):
    ai = pow(a,-1,26)
    return "".join(chr((ai*(ord(c)-65-b))%26+65) for c in t)

# Example
e = aff_e("HELLO",5,8)
d = aff_d(e,5,8)
print(e,d)