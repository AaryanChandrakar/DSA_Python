def floor_and_ceil(arr, target):
    """
    arr: sorted list of integers
    target: integer
    returns: (floor_value, ceil_value)
    floor_value = largest value <= target (or -1 if not exists)
    ceil_value  = smallest value >= target (or -1 if not exists)
    """
    n = len(arr)
    floor_val = -1
    ceil_val = -1

    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            # target present → floor and ceil both are target
            floor_val = arr[mid]
            ceil_val = arr[mid]
            return floor_val, ceil_val

        elif arr[mid] > target:
            # candidate for ceil
            ceil_val = arr[mid]
            high = mid - 1

        else:  # arr[mid] < target
            # candidate for floor
            floor_val = arr[mid]
            low = mid + 1

    return floor_val, ceil_val


# Example usage:
if __name__ == "__main__":
    nums = [2, 4, 4, 4, 8, 9, 10, 12, 15]
    target = 6
    f, c = floor_and_ceil(nums, target)
    print("Floor:", f, "Ceil:", c)  # Floor: 4, Ceil: 8

# Time Complexity: O(log n)
# Space Complexity: O(1)
