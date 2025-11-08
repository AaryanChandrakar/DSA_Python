# Right rotate an Array by K places

# nums = [3,9,5,6,7,2]  , let k=3
#        [2,3,9,5,6,7]  # first right rotation
#        [7,2,3,9,5,6]  # second right rotation
#        [6,7,2,3,9,5]  # third right rotation
# if k = 4,5,6 respectively
#        [5,6,7,2,3,9]  # fourth right rolation
#        [9,5,6,7,2,3]  # fifth right rotation
#        [3,9,5,6,7,2]  # sixth right rotation, array in original format
# if = 7 [2,3,9,5,6,7]  # just like k=1
# we need to apply modulas operator 

nums = [3,9,5,6,7,2]
k = 3

# Bruteforce Approach
n = len(nums)
rotation = k % n
print("Original Array: ",nums)
for i in range(rotation):
    e = nums.pop()
    nums.insert(0,e)
print(k,"Times Right Rotated Array: ",nums)

#  Time Complexity: O(r*n)  , for loop = r (rotation)
#                    inserting an ele in an array = n
# Space Complexity: O(1)

print("-------------------------------------------------")

#Better Approach using slicing:
nums2 = [3,9,5,6,7,2,10,9]
k=3

n = len(nums2)
k = k%n
print("Original Array: ",nums2)
nums2[:] = nums2[n-k:] + nums2[:n-k]
print(k,"Times Right Rotated Array (using slicing): ",nums2)

# Time Complexity: O(k + n-k) ~= O(n)
# Space Complexity: O(1)
print("----------------------------------------")

#Optimal Approach
def reverse_fun(nums2,left,right):
    while(left<right):
        nums2[left],nums2[right] = nums2[right],nums2[left]
        left+=1
        right-=1

nums2 = [3,9,5,6,7,2,10,9]
k=2
n=len(nums2)
print("Original Array: ",nums2)
reverse_fun(nums2,n-k,n-1)
reverse_fun(nums2,0,n-k-1)
reverse_fun(nums2,0,n-1)
print(k,"Times Rotated Array: ", nums2)

# Time Complexity:
"""
Reverse last k elements = k/2
Reverse remaining ele = (n-k)/2
Reverse whole array = n/2
 k       n-k       n        2n
---  +  -----  +  ---  ==> ----  ==> n
 2        2        2        2
"""

# Time Complexity:  O(n)   
# Space Complexity: O(1)

