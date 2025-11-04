# Approach 1: Using slicing
def right_rotate_by_one(nums):
    n = len(nums)
    # This updates the list in place
    nums[:] = [nums[-1]] + nums[:n-1]

# Example usage:
arr = [7, 4, 2, 10, 5, 3, 1, 6]
right_rotate_by_one(arr)
print(arr)   # Output: [6, 7, 4, 2, 10, 5, 3, 1]

#  Time Complexity: 0(n)
# Space Complexity: 0(n)

# --------------------------------

# Approach 2: Without slicing (using a loop)
def right_rotate_by_one_loop(nums):
    n = len(nums)
    temp = nums[-1]
    for i in range(n - 2, -1, -1):
        nums[i + 1] = nums[i]
    nums[0] = temp

# Example usage:
arr2 = [7, 4, 2, 10, 5, 3, 1, 6]
right_rotate_by_one_loop(arr2)
print(arr2)  # Output: [6, 7, 4, 2, 10, 5, 3, 1]

#  Time Complexity: 0(n)
# Space Complexity: 0(1)