# Set Matrix Zeros
# (If we find 0 as element in matrix, then we need to make all the elements '0' in respective row and column)

nums = [[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]

#Bruteforce Approach
def mark_infinity(nums,row,col):
    for i in range(len(nums)):
        if nums[i][col]!=0:
            nums[i][col]=float("inf")
    for i in range(len(nums[0])):
        if nums[row][i]!=0:
            nums[row][i]=float("inf")

def set_zeros(nums):
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j]==0:
                mark_infinity(nums,i,j)

    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j]==float("inf"):
                nums[i][j]=0
    print("Array After Operation: ")
    for row in nums:
        print(*row)

print("Original Array: ")
for i in nums:
    print(*i)
set_zeros(nums)