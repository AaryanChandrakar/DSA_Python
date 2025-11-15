# Rearrange Array Elements by Sign in alternate manner and need to maintain the order

# nums = [5,10,-3,-1,-10,6]
#result= [5,-3,10,-1,6,-10]

nums = [5,10,-3,-1,-10,6]

# Bruteforce 
def fun(nums):
    pos = [num for num in nums if num>=0]
    neg = [num for num in nums if num<0]

    for i in range(len(pos)):
        nums[2*i] = pos[i]
        nums[2*i+1] = neg[i]
    return nums
print("Original Array:   ",nums)
print("Rearranged Array: ",fun(nums))
# Time Complexity:  O(n/2 + n/2 + n/2) = O(n + n/2) ~= O(n)
# Space Complexity: O(n/2 + n/2) ~= O(n)
print("------------------------------------")

# Optimal Solution
def fun_opt(nums):
    n = len(nums)
    result = [0]*n
    pos_index = 0
    neg_index = 1
    for i in range(0,n):
        if nums[i]>=0:
            result[pos_index]=nums[i]
            pos_index+=2
        else:
            result[neg_index]=nums[i]
            neg_index+=2
    return result
nums2 = [5,10,-3,-1,-10,6]
print("Original Array:   ",nums2)
print("Rearranged Array: ",fun_opt(nums2))
# Time Complexity:  O(n)
# Space Complexity: O(n)
