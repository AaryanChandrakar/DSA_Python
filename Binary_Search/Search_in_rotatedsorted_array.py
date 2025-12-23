def search_in_rotated(nums, target):
    """
    Returns index of target in rotated sorted array nums, or -1 if not found.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Found target
        if nums[mid] == target:
            return mid

        # Check which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1      # Target in left half
            else:
                left = mid + 1       # Target in right half
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1       # Target in right half
            else:
                right = mid - 1      # Target in left half

    return -1


# Example of function calling
if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    # Calling the function
    index = search_in_rotated(arr, target)
    print("Index:", index)  # Output: 4

# Time Complexity: O(log n)
# Space Complexity: O(1)