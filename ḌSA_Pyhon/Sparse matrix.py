import numpy as np
from scipy.sparse import coo_matrix

# Creating a sparse matrix
data = np.array([3, 1, 4, 1])  # Values of non-zero elements
row = np.array([0, 1, 2, 2])  # Row indices of non-zero elements
col = np.array([0, 2, 1, 3])  # Column indices of non-zero elements

# Creating a COO matrix
sparse_matrix = coo_matrix((data, row, col), shape=(3, 4))

# Print the sparse matrix
print("Sparse Matrix in COO format:")
print(sparse_matrix)
