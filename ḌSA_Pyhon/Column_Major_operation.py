import numpy as np

# Using np.asfortranarray() for column-major order:
col_major_array = np.asfortranarray([[1, 2, 3], [4, 5, 6]])

# Using np.array() with 'F' order flag:
col_major_array = np.array([[1, 2, 3], [4, 5, 6]], order='F')
# Directly access elements in column-major order:
element = col_major_array[1, 0]  # Accesses the second row, first column

# Iterate through columns:
for i in range(col_major_array.shape[1]):
    for j in range(col_major_array.shape[0]):
        print(col_major_array[j, i])
  class ColumnMajorMatrix:
    def __init__(self, rows, cols):
        self.data = [0] * (rows * cols)
        self.rows = rows
        self.cols = cols

    def __getitem__(self, index):
        row, col = index
        return self.data[col * self.rows + row]

    def __setitem__(self, index, value):
        row, col = index
        self.data[col * self.rows + row] = value

row_major_array = np.array([[1, 2, 3], [4, 5, 6]])
col_major_view = row_major_array.T  # Create a transposed view


