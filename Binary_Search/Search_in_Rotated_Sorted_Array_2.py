def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        # If target is found
        if nums[mid] == target:
            return True

        # Handle duplicates: nums[low], nums[mid], nums[high] are same
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue

        # Left part is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right part is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False
nums = [2,5,6,0,0,1,2]
target = 0
print(search(nums, target))   # True

target = 3
print(search(nums, target))   # False

# Time Complexity: O(log n) on average, O(n) in the worst case due to duplicates
# Space Complexity: O(1)
