nums = [1,3,5,6,9,12,16,19,22,25]
#index  0 1 2 3 4  5  6  7  8  9 
target = 20

# Bruteforch Approach (Linear Search)
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i]>=target:
            return i
    return -1
print(target,"can be inserted at index: ",linear_search(nums,target))
# Time Complexity: O(n)
# Space Complexity: O(1)
print("-----------------------------------------------")

# Binary Search Approach
def binary_search(nums,target):
    n = len(nums)
    lb = n
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if target<=nums[mid]:
            high = mid-1
            lb = mid
        else:
            low = mid+1
    return lb
print(target,"can be inserted at index: ",binary_search(nums,target))
# Time Complexity: O(log2(n))
# Space Complexity: O(1)
# Note: This approach can also be implemented using recursion.
#       We can apply binary search to sorted arrays to find the lower/upper bound index of the target element.
