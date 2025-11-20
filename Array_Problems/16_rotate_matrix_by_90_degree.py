# Rotate a Matric by 90 Degree (In Place)
# (rotate in right direction by 90 degree, and do not return anything i.e in-place)

nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# Bruteforce Approch using extra space and returning resultant matrix
def fun(nums):
    n = len(nums)
    result = [[0 for i in range(n)] for i in range(n)]
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            result[j][(n-1)-i] = nums[i][j]
    return result

print("Original Matrix: ")
for row in nums:
    print(*row)
print("90 degree rotated matrix: ")
for row in fun(nums):
    print(*row)
# Time Complexity:  O(n^2)
# Space Complexity: O(n^2)
print("-------------------------------------------")

# Optimal Approach
# (do transpose of matrix then -> reverse each row of matrix)

def fun_opt(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums[0])):
            nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
    for i in range(len(nums)):
        nums[i].reverse()
print("Original Array: ")
for row in nums:
    print(*row)
fun_opt(nums)   # function calling
print("Rotated Array: ")
for row in nums:
    print(*row)

# Time Complexity:  O(n*m) + O(n*n)
# Space Complexity: O(1)         