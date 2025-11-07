# Right Rotate an Array by 1 Place 

# 1. Using Slicing [ : ]
#index  0   1  2  3  4  5   6  7
nums = [5, -2, 3, 9, 0, 6, 10, 7]
#index -8  -7 -6 -5 -4 -3  -2 -1
n = len(nums)
print("Before Rotation: ",nums)
nums[:] = [nums[-1]] + nums[0:n-1]
# Or      [nums[n-1]] + nums[0:n-1]
print("After Rotation:  ",nums)

#  Time Complexity: 0(n)
# Space Complexity: 0(n)



# 2. Using Loop:
def fun (nums):
    n = len(nums)
    temp = nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1] = nums[i]
    nums[0] = temp
    return nums

print("Before Rotation: ",nums)
print("After Rotation:  ",fun(nums))
#  Time Complexity: O(n-1) =~ 0(n)
# Space Complexity: 0(1)

