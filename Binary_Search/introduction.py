# Sorted Array / List
# A sorted array or list is a collection of elements arranged in a specific order, typically in ascending or descending order.
# This ordering allows for efficient searching, insertion, and deletion operations.
# Example:
nums = [2,4,6,7,9,11,18,19]
target = 6

# Normal Binary Search Approach
def binary_search(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low = mid+1
        else:
            high = mid-1   
    return -1

print("Target",target,"is at index: ",binary_search(nums,target))
# Time Complexity:  O()
# Space Complexity: O()
print("-----------------------------------------------")

# Recursive Solution for Binary Search

