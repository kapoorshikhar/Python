# Function to perform row-major operation on a matrix
def row_major_operation(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Perform row-major operation
    row_major_result = []
    for i in range(rows):
        for j in range(cols):
            row_major_result.append(matrix[i][j])

    return row_major_result

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Perform row-major operation on the matrix
result = row_major_operation(matrix)
print("Row-major operation result:", result)
# Function to perform row-major operation on a matrix
def row_major_operation(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Perform row-major operation
    row_major_result = []
    for i in range(rows):
        for j in range(cols):
            row_major_result.append(matrix[i][j])

    return row_major_result

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Perform row-major operation on the matrix
result = row_major_operation(matrix)
print("Row-major operation result:", result)
