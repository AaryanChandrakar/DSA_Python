# Find largest element in an array:

nums = [55,32,-97,99,3,67]

# Method: 1
def fun(nums):
    largest = nums[0]
    for i in nums:
        if i>=largest:
            largest = i
    return largest
    
largest_ele = fun(nums)
print("Array: ",nums)
print("Largest Element in Array is: ",largest_ele)
#  Time Complexity: 0(n)
# Space Complexity: 0(1)


# Method: 2
def fun_inf(nums):
    largest = float("-inf")
    for i in nums:
        if i>=largest:
            largest = i
    return largest
    
largest_ele_inf = fun_inf(nums)
print("Array: ",nums)
print("Largest Element in Array is: ",largest_ele_inf)
#  Time Complexity: 0(n)
# Space Complexity: 0(1)
