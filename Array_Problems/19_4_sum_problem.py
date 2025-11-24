# 4 Sum problem in an Array
"""
# Very similar to 3 sum problem
* have to pick 4 element (non-repeating elements),
* and the sum of those 4 element must be equal to the given number
* nums = [1,0,-1,0,-2,2] , target = 0
* The best pick can be [-1, 0, 0, 1] , sum==0
*                     [-2, -1, 1, 2] , sum==0
*                     [-2, 0, 0, 2] , sum==0
* We need to return 2d list/array: [[-1,0,0,1],[-2,-1,1,2],[-2,0,0,2]]
* We do not need to return result in order
"""
nums = [1,0,-1,0,-2,2]
target = 0

# Bruteforce Approach
def fun_brute(nums, target):
    n = len(nums)
    my_set = set()
    if n<4:
        return []
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    sum = nums[i]+nums[j]+nums[k]+nums[l]
                    if sum == target:
                        my_set.add(tuple(sorted([nums[i],nums[j],nums[k],nums[l]])))
                        
    result = []
    for i in my_set:
        result.append(list(i))
    return result
print("Result: ",fun_brute(nums,target))
# Time Complexity:  O(n^4)
# Space Complexity: O(no. of quadruplet)
print("-------------------------------------------------------------")

# Better Approach
def fun_better(nums,traget):
    n = len(nums)
