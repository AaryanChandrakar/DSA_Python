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
     no_of_cols = len(nums[0])  # Bcos elements in any row is equal to no of columns

"""

# Iterating each elements of an array:
nums = [[5,20,3],[7,-10,9],[1,-52,6]]
print("Printing 2D Array: ",nums)
print("Iterating 2D Array: ")
for i in range(len(nums)):
    for j in range(len(nums[0])):
        print(nums[i][j], end=", ")
print(" ")
# Find total of all elements in 2D matrix
total = 0
for i in range(len(nums)):
    for j in range(len(nums[0])):
        total += nums[i][j]
print("Total Sum of all the elements: ",total)

# print firsts row 
print("Elements in first row: ")
for i in range(1):
    for j in range(len(nums[0])):
        print(nums[i][j], end=", ")
print(" ")

#print second row:
print("Elements in second row: ")
for i in range(1,2):
    for j in range(len(nums[0])):
        print(nums[i][j], end=", ")
print(" ")

#print elements in third row:
print("Elements in third row: ")
for i in range(2,3):
    for j in range(len(nums[0])):
        print(nums[i][j], end=", ")
print(" ")
        
        
