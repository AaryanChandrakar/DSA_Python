# Move zeros to the end of the array (maintain the order of non-zero elements)
# In-place operation must be performed, no return value required

# nums = [1,0,2,3,0,0,3,5,1]
#         0 1 2 3 4 5 6 7 8 

# resulttant array : [1,2,3,3,5,1,0,0,0]  (order remains same of non-zero elements)
#                     0 1 2 3 4 5 6 7 8


# Normal Solution:
nums = [1,0,2,3,0,0,3,5,1]
temp = []
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

# Time Complexity:  O(n+n) ~= O(n)
# Space Complexity: O(n)
print("-----------------------------------------")

# Optimal Solution:
nums2 = [1,2,0,4,0,0,3,5,1]

def my_fun(nums2):
    if len(nums2)==1:
        return

    i=0
    while(i<len(nums2)):
        if nums2[i]==0:
            break
        i+=1

    if i==len(nums2):
        return 

    j=i+1
    while(j<len(nums2)):
        if(nums2[j] != 0):
            nums2[i],nums2[j] = nums2[j],nums2[i]
            i+=1
        j+=1

print("Original Array:        ",nums2)
my_fun(nums2)
print("Array after Operation: ",nums2)

# Time Complexity:  O(n)
# Space Complexity: O(1)

print("-------------------------------------------")

#Pythinic Code
nums = [4,5,0,8,0,7,0,1,0,6,0,0,4,9]

def fun(nums):
    n = len(nums)
    non_zero_ele = [i for i in nums if i!=0]
    zeros = [0] * nums.count(0)
    return non_zero_ele + zeros

print(fun(nums))