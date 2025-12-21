# Lower Bound: Smallest index-i such that nums[i]>=target
# Upper Bound: Smallest index-i such that target<nums[i]

nums = [1,1,1,2,3,3,5,6,7,7, 7, 9, 12, 12, 13]
#index  0 1 2 3 4 5 6 7 8 9 10 11  12  13  14
target = 7

def lower_bound(nums, target):
    n = len(nums)
    lb = n
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb
print("Lower Bound: ",lower_bound(nums,target))
# Time Complexity:  O(log n)
# Space Complexity: O(1)



def upper_bound(nums, target):
    n = len(nums)
    ub = n
    low = 0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return ub
print("Upper Bound: ",upper_bound(nums,target))
# Time Complexity:  O(log n)
# Space Complexity: O(1)
