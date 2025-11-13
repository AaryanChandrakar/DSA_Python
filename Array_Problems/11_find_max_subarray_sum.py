# Find max subarray sum

# What is sub-array;
"""
if array = [-2,1-3,4,-1,2,1,-5,4]
the sub-array's can be: [-2,1,-3], [4,-1], [-5], [1-5,4]
elements of sub-array must be continuos in the original array.
if we are preparing array by picking non-continuos elements, then it is called 'sub-sequence'.
"""

# nums = [-2,1,-3,4,-1,2,1,-5,4]

def fun(nums):
    n = len(nums)
    max_sum_arr = float("-inf")
    for i in range(0,n):
        total = 0
        for j in range(i,n):
            total = total + nums[j]
            max_sum_arr = max(max_sum_arr,total)
    return max_sum_arr
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Array: ",nums)
print("Max Sum Array: ",fun(nums))
# Time Complexity:  O(n^2)
# Space Complexity: O(1)

