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
