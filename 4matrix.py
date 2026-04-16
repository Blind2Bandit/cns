import numpy as np

# A non-singular matrix (determinant is not 0)
matrix = [[1, 2], [3, 4]]

# Calculate the standard inverse
print(np.linalg.inv(matrix))