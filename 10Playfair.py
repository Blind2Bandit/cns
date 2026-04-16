key = "MONARCHY"
text = "INSTRUMENTS"

# Generate key matrix
k = ""
for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J removed
    if c not in k:
        k += c

mat = [list(k[i:i+5]) for i in range(0,25,5)]

def find(c):
    if c == 'J': c = 'I'
    for i in range(5):
        for j in range(5):
            if mat[i][j] == c:
                return i,j

# Prepare text
pt = ""
i = 0
while i < len(text):
    a = text[i]
    b = text[i+1] if i+1 < len(text) else 'X'
    
    if a == b:
        pt += a + 'X'
        i += 1
    else:
        pt += a + b
        i += 2

if len(pt) % 2: pt += 'X'

# Encryption
enc = ""
for i in range(0,len(pt),2):
    r1,c1 = find(pt[i])
    r2,c2 = find(pt[i+1])
    
    if r1 == r2:
        enc += mat[r1][(c1+1)%5] + mat[r2][(c2+1)%5]
    elif c1 == c2:
        enc += mat[(r1+1)%5][c1] + mat[(r2+1)%5][c2]
    else:
        enc += mat[r1][c2] + mat[r2][c1]

print("Encrypted:", enc)


# Decryption
dec = ""
for i in range(0,len(enc),2):
    r1,c1 = find(enc[i])
    r2,c2 = find(enc[i+1])
    
    if r1 == r2:
        dec += mat[r1][(c1-1)%5] + mat[r2][(c2-1)%5]
    elif c1 == c2:
        dec += mat[(r1-1)%5][c1] + mat[(r2-1)%5][c2]
    else:
        dec += mat[r1][c2] + mat[r2][c1]

print("Decrypted:", dec)