text = "HELLOWORLD"
key = [3, 1, 4, 2]   # column order

# Padding (if needed)
while len(text) % len(key) != 0:
    text += 'X'

# Create matrix row-wise
rows = len(text) // len(key)
mat = []
k = 0
for i in range(rows):
    row = []
    for j in range(len(key)):
        row.append(text[k])
        k += 1
    mat.append(row)

# Encryption (column order)
enc = ""
for num in range(1, len(key)+1):
    col = key.index(num)
    for i in range(rows):
        enc += mat[i][col]

print("Encrypted:", enc)


# Decryption
dec_mat = [[""]*len(key) for _ in range(rows)]
k = 0

for num in range(1, len(key)+1):
    col = key.index(num)
    for i in range(rows):
        dec_mat[i][col] = enc[k]
        k += 1

dec = ""
for i in range(rows):
    for j in range(len(key)):
        dec += dec_mat[i][j]

print("Decrypted:", dec)