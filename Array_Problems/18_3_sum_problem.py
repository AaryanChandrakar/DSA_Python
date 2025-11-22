# 3 Sum Problem in an Array
# have to pick 3 element (non-repeating elements), 
# and the sum of those 3 element must be equal to the given number

# nums = [-1,0,1,2,-1,-4] , x=0
"""
The best pick can be [-1,2,-1] , sum=0 == x=0
                     [0,1,-1]  , sum=0 == x=0

We need to return 2d list/array: [[1-,2,-1],[0,1,-1]]
We do not need to return result in order

"""

# Bruteforce Approach

def fun_bruteforce(nums,x):
     n = len(nums)
     my_set = set()
     for i in range(0,n):
          for j in range(i+1,n):
               for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==x:
                         temp = [nums[i],nums[j],nums[k]]
                         temp.sort()
                         my_set.add(tuple(temp))
     return [list(ans) for ans in my_set]
     
nums = [-1,0,1,2,-1,-4]
x=0
print("Result: ",fun_bruteforce(nums,x))
# Time Complexity:  O(n^3)
# Space Complexity: O(no. of triplets)