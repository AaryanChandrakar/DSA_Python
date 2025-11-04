# Approach 1: Using slicing
def right_rotate_by_one(nums):
    n = len(nums)
    # This updates the list in place
    nums[:] = [nums[-1]] + nums[:n-1]

# Example usage:
arr = [7, 4, 2, 10, 5, 3, 1, 6]
right_rotate_by_one(arr)
print(arr)   # Output: [6, 7, 4, 2, 10, 5, 3, 1]

