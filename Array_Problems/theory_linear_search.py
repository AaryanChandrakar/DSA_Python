# Linear Search
"""
if target exist in array in array, then return the index of firts occurance
if target does not exist in array, the return -1
"""

# nums = [5,3,9,8,,1,4,-10,-100]       target=4
# nums = [10,20,25,10,10,-5,-3,-2,7]   target=10
# nums = [5,3,2,5,6,7,10,1]            target=100

def linear_search(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1

print("If we get -1 as return value, it means target get element does not exist in array.")

nums = [5,3,9,8,1,6,4,-10,-100]
print("Array: ",nums)
print("Target found at index: ",linear_search(nums,4))

nums1 = [10,20,25,10,10,-5,-3,-2,7]
print("Array: ",nums1)
print("Target found at index: ",linear_search(nums1,10))

nums2 = [5,3,2,5,6,7,10,1]
print("Array: ",nums2)
print("Target found at index: ",linear_search(nums2,100))

