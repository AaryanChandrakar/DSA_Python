# file: main.py

def find_min(nums):
    """
    Find the minimum in a rotated sorted array (no duplicates).
    Time: O(log n) using binary search.
    """
    left, right = 0, len(nums) - 1

    # If array is not rotated
    if nums[left] <= nums[right]:
        return nums[left]

    while left <= right:
        mid = (left + right) // 2

        # Check if mid is the pivot (minimum)
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return nums[mid]
        if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        # Decide which half to search
        if nums[mid] >= nums[left]:
            # Left half is sorted, minimum in right half
            left = mid + 1
        else:
            # Right half is sorted, minimum in left half
            right = mid - 1

    # Fallback (for safety)
    return nums[0]


if __name__ == "__main__":
    # Change this list to test different inputs
    nums = [4, 5, 6, 7, 0, 1, 2]
    ans = find_min(nums)
    print("Array:", nums)
    print("Minimum element:", ans)
