def transpose(matrix):
    if not matrix or not matrix[0]:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    # Create a new matrix with cols rows and rows columns
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result

# Sample function call:
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = transpose(matrix)
print(transposed)  # Output: [[1, 4], [2, 5], [3, 6]]
