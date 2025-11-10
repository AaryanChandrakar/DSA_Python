#Two Sum Problem

# Normal Solution:
def two_sum(nums,target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
            
nums = [5,9,1,2,4,15,6,3]
target = 13
print("The index of those elements (normal): ",two_sum(nums,target))
# Time Complexity:  O(n^2)
# Space Complexity: O(1)
print("-------------------------------------------")


# Optimal Solution:
def two_sum_opt(nums,target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement],i]
        seen[nums[i]] = i
nums2 = [2,7,11,15]
target2 = 9
print("The index of those elements (optimal): ",two_sum_opt(nums2,target2))
# Time Complexity:  O(n)
# Space Complexity: O(n)
# With optimal solution, we can do in constant space, we always need extra space, 
# In case to achive contant space, we have to compromise with time complexity (will be increased)