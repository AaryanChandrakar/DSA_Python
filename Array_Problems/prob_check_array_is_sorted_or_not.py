# Check if array is sorted or not
# is Yes, then retrun True
# if Not, then return Flase

nums_1 = [3,5,6,8,9,10,20]
nums_2 = [1,2,5,8,3,10,14,15]

def fun(nums):
    n = len(nums)
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            return False
    return True

print("Array: ",nums_1)
print("Array is Sorted: ",fun(nums_1))
print("------------------------------------")
print("Array: ",nums_2)
print("Array is Sorted: ",fun(nums_2))

#  Time complexity: 0(n)
# Space Complexity: 0(1)