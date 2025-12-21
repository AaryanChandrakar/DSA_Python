from typing import List, Tuple
import bisect  # used in solution 4 [web:15]


# ------------------------------------------------------------
# Solution 1: Naive linear scan
# ------------------------------------------------------------
# Time:  O(n) – single pass over the array in worst case. [web:21]
# Space: O(1) – only a few extra variables. [web:11]
def first_last_linear(nums: List[int], target: int) -> Tuple[int, int]:
    first = -1
    last = -1
    for i, val in enumerate(nums):
        if val == target:
            if first == -1:
                first = i
            last = i
    return first, last


# ------------------------------------------------------------
# Solution 2: Optimized linear – two directional scans
# ------------------------------------------------------------
# Time:  O(n) – at most two full passes over the array. [web:21]
# Space: O(1). [web:11]
def first_last_two_scans(nums: List[int], target: int) -> Tuple[int, int]:
    n = len(nums)
    first = -1
    last = -1

    # find first
    for i in range(n):
        if nums[i] == target:
            first = i
            break

    if first == -1:
        return -1, -1

    # find last
    for i in range(n - 1, -1, -1):
        if nums[i] == target:
            last = i
            break

    return first, last


# ------------------------------------------------------------
# Solution 3: Single-pass with flags (still O(n))
# ------------------------------------------------------------
# Time:  O(n) – single left-to-right traversal. [web:21]
# Space: O(1). [web:11]
def first_last_single_pass(nums: List[int], target: int) -> Tuple[int, int]:
    first = -1
    last = -1
    seen = False

    for i, v in enumerate(nums):
        if v == target:
            if not seen:
                first = i
                seen = True
            last = i
        elif seen:
            # Since array is sorted, once elements exceed target we can break. [web:21]
            if v > target:
                break

    return first, last


# ------------------------------------------------------------
# Solution 4: Using Python bisect module (binary search)
# ------------------------------------------------------------
# Time:  O(log n) – each bisect call is binary search on sorted list. [web:15]
# Space: O(1) – no extra data structures. [web:11]
def first_last_bisect(nums: List[int], target: int) -> Tuple[int, int]:
    left = bisect.bisect_left(nums, target)
    # check if target exists
    if left == len(nums) or nums[left] != target:
        return -1, -1

    right = bisect.bisect_right(nums, target) - 1
    return left, right


# ------------------------------------------------------------
# Solution 5: Two separate binary searches (iterative)
# ------------------------------------------------------------
# Time:  O(log n) – two binary searches. [web:11][web:19]
# Space: O(1). [web:11]
def _find_first(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            first = mid
            high = mid - 1  # move left to find earlier occurrence. [web:11]
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first


def _find_last(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            last = mid
            low = mid + 1  # move right to find later occurrence. [web:11]
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last


def first_last_binary_search(nums: List[int], target: int) -> Tuple[int, int]:
    return _find_first(nums, target), _find_last(nums, target)


# ------------------------------------------------------------
# Solution 6: Recursive binary search for first & last
# ------------------------------------------------------------
# Time:  O(log n) – recursive binary search depth is logarithmic. [web:11]
# Space: O(log n) – recursion call stack. [web:5]
def _find_first_rec(nums: List[int], target: int, low: int, high: int) -> int:
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        left_ans = _find_first_rec(nums, target, low, mid - 1)
        return mid if left_ans == -1 else left_ans
    elif nums[mid] < target:
        return _find_first_rec(nums, target, mid + 1, high)
    else:
        return _find_first_rec(nums, target, low, mid - 1)


def _find_last_rec(nums: List[int], target: int, low: int, high: int) -> int:
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        right_ans = _find_last_rec(nums, target, mid + 1, high)
        return mid if right_ans == -1 else right_ans
    elif nums[mid] < target:
        return _find_last_rec(nums, target, mid + 1, high)
    else:
        return _find_last_rec(nums, target, low, mid - 1)


def first_last_binary_recursive(nums: List[int], target: int) -> Tuple[int, int]:
    return (
        _find_first_rec(nums, target, 0, len(nums) - 1),
        _find_last_rec(nums, target, 0, len(nums) - 1),
    )


# ------------------------------------------------------------
# Optional: unified driver to quickly test all methods
# ------------------------------------------------------------
def test_all(nums: List[int], target: int):
    print("Array:", nums)
    print("Target:", target)
    print("Linear:", first_last_linear(nums, target))
    print("Two scans:", first_last_two_scans(nums, target))
    print("Single pass:", first_last_single_pass(nums, target))
    print("Bisect:", first_last_bisect(nums, target))
    print("Binary iterative:", first_last_binary_search(nums, target))
    print("Binary recursive:", first_last_binary_recursive(nums, target))


if __name__ == "__main__":
    arr = [1, 2, 4, 4, 4, 5, 7, 7, 9]
    x = 4
    test_all(arr, x)
