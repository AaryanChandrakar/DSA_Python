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





