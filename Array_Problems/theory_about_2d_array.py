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

# 2D Matrix
# What is 2D matrix / 2D list ?
"""
nums = [[5,20,3],[7,-10,9],[1,-52,6]]
#index     0         1          2
length of array 'nums' is: 3

    col 0   1    2
row   --------------
0     | 5 | 20 | 3 |
      --------------
1     | 7 |-10 | 9 |
      --------------
2     | 1 |-52 | 6 |

Here, we can see the 3*3 matrix.

If I need to make a variable that represants no. of rows in 2D matrix then we can do:
      no_of_rows = len(nums)

If I need to make a variable that represants no. of cols in 2D matric then we can do,
     np_of_cols = len(nums[0])


"""