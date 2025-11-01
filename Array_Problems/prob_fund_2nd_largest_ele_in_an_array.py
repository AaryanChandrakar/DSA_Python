# Find the 2nd largest number in an array
# Without sorting

nums = [55,32,97,-55,45,32,88,21]

# 1. Normal Solution
def fun(nums):
    largest = float("-inf")
    s_largest = float("-inf")

    for i in nums:
        if i>largest:
            largest = i
        
    for i in nums:
        if i>s_largest and i<largest:
            s_largest = i
    return s_largest

print('Array: ',nums)
sec_lar_ele = fun(nums)
print("Secodn Largest Element in an Array is: ",sec_lar_ele)
#  Time Complexity: 0(n+n) = 0(2n) ~= 0(n)
# Space Complexity: 0(1)


# 2. Optimal Solution: 
def fun_opt(nums):
    largest = float("-inf")
    s_largest = float("-inf")

    for i in nums:
        if (i>largest):
            s_largest = largest
            largest = i
        elif(i>s_largest and i != largest):
            s_largest = i
    return s_largest

print("Array: ",nums)
sec_lar_ele_opt = fun_opt(nums)
print("Second Largest Element in an Array: ",sec_lar_ele_opt)

#  Time Complexity: 0(n)
# Space Complexity: 0(1)
