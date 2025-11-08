# Move zeros to the end of the array (maintain the order of non-zero elements)
# In-place operation must be performed, no return value required

# nums = [1,0,2,3,0,0,3,5,1]
#         0 1 2 3 4 5 6 7 8 

# resulttant array : [1,2,3,3,5,1,0,0,0]  (order remains same of non-zero elements)
#                     0 1 2 3 4 5 6 7 8

nums = [1,0,2,3,0,0,3,5,1]
temp = []
count_zeros = 0

for i in nums:
    if(i != 0):
        temp.append(i)

print("Original Array:        ",nums)
for i in range(len(nums)):
    if i < len(temp):
        nums[i] = temp[i]
    else:
        nums[i] = 0           
print("Array after operation: ",nums)

# Time Complexity:  O(n)
# Space Complexity: O(n)