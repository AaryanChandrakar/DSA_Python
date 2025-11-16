def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    row_zero = False
    col_zero = False

    # Check if first row has zero
    for j in range(cols):
        if matrix[0][j] == 0:
            row_zero = True

    # Check if first column has zero
    for i in range(rows):
        if matrix[i][0] == 0:
            col_zero = True

    # Use first row and column as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set zeroes for rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Set zeroes for first row
    if row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Set zeroes for first column
    if col_zero:
        for i in range(rows):
            matrix[i][0] = 0

# Sample function call and print
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

setZeroes(matrix)
print(matrix)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
