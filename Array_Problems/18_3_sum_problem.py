# 3 Sum Problem in an Array
# have to pick 3 element (non-repeating elements), 
# and the sum of those 3 element must be equal to the given number

# nums = [-1,0,1,2,-1,-4] ,
"""
The best pick can be [-1,2,-1] , sum==0
                     [0,1,-1]  , sum==0

We need to return 2d list/array: [[1-,2,-1],[0,1,-1]]
We do not need to return result in order

"""
nums = [-1,0,1,2,-1,-4]

# Bruteforce Approach

def fun_bruteforce(nums):
     n = len(nums)
     my_set = set()
     for i in range(0,n):
          for j in range(i+1,n):
               for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                         temp = [nums[i],nums[j],nums[k]]
                         temp.sort()
                         my_set.add(tuple(temp))
     return [list(ans) for ans in my_set]
     
print("Result: ",fun_bruteforce(nums))
# Time Complexity:  O(n^3)
# Space Complexity: O(no. of triplets)
print("--------------------------------------------")

# Better Approach:

def threeSum(nums):
        n = len(nums)
        result = set()
        for i in range(0,n):
            my_set = set()
            for j in range(i+1,n):
                third = -(nums[i]+nums[j])
                if third in my_set:
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(nums[j])
        return [list(ans) for ans in result]
print("Result: ",threeSum(nums))
# Time Complexity:  O(n^2)
# Space Complexity: O(n) + O(no. of triplets)
print("--------------------------------------------")

# Optimal Approach:
"""
Time Complexity can not be reduced, but we can reduce Space Complexity
"""
def threeSum_opt(nums):
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n-2):
            if i != 0 and nums[i]==nums[i-1]:
                continue
            j =i+1
            k =n-1
            while j<k:
                total_sum = nums[i]+nums[j]+nums[k]
                if total_sum < 0:
                    j+=1
                elif total_sum > 0:
                    k-=1
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    result.append(temp)
                    j+=1
                    k-=1

                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return result
print("Result: ",threeSum_opt(nums))
# Time Complexity:  O(nlogn + n^2) =~ O(n^2)
# Space Complexity: O(no. of triplets)