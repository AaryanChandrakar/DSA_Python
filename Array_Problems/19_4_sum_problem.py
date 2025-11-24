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
# Space Complexity: O(n)
print("-------------------------------------------------------------")

# Better Approach
def fun_better(nums,traget):
    nums.sort()
    n = len(nums)
    my_set = set()
    for i in range(0,n):
        for j in range(i+1,n):
            hash_set = set()
            for k in range(j+1,n):
                fourth = target - (nums[i]+nums[j]+nums[k])
                if fourth in hash_set:
                    temp = [nums[i],nums[j],nums[k],fourth]
                    temp.sort()
                    my_set.add(tuple(temp))
                hash_set.add(nums[k])
    result = []
    for i in my_set:
        result.append(list(i))
    return result

print("Result: ",fun_better(nums,target))
# Time Complexity:  O(nlogn + n^3)
# Space Complexity: O(n)
print("----------------------------------------------------------")

# Optimal Approach:
def fun_opt(nums,target):
    n = len(nums)
    result = []
    for i in range(0,n):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            k = j+1
            l = n-1
            while(k<l):
                total = nums[i]+nums[j]+nums[k]+nums[l]
                if total < target:
                    k+=1
                elif total > target:
                    l-=1
                else: 
                    result.append([nums[i],nums[j],nums[k],nums[l]])
                    k += 1
                    l -=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while k<l and nums[l]==nums[l+1]:
                        l-=1
    return result
print("Result: ",fun_opt(nums,target))
# Time Complexity:  O(nlogn + n^3) =~ O(n^3)
# Space Complexity: O(no. of quadruplet)

