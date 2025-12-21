# Find the first and lsat occurance of an element in a sorted array
target = 4
nums = [1, 2, 4, 4, 4, 8, 12, 13, 18, 19]
#index: 0  1  2  3  4  5   6   7   8   9

def first_and_last_occurance(nums, target):
    n = len(nums)
    first = -1
    last = -1
    for i in range(n):
        if nums[i]==target:
            if first == -1:
                first = i
            last = i
    return first, last

f, l = first_and_last_occurance(nums, target)
print("First Index: ",f," & Last Index: ",l)
# Time Complexity: O(n)
# Space Complexity: O(1)

print("----------------------------------------------------")

def fun_lb(nums, target):
    n = len(nums)
    lb = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid]>=target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb

def fun_ub(nums, target):
    n = len(nums)
    ub = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid]>target:
            ub = mid
            high = mid-1
        else:
            low = mid+1
    return ub-1

low_b , up_b = fun_lb(nums, target), fun_ub(nums, target)
print("Lower Bound: ",low_b," & Upper Bound: ",up_b)
# Time Complexity: O(2 log n) =~ O(log n)
# Space Complexity: o(1)