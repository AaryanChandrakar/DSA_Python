# Lower Bound: Smallest index such that nums[i]>=target
# Upper Bound: Larget index such that nums[i]<=tareget

nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]

n = len(nums)
lb = n
low = 0, high = n-1
while low<high:
    mid = (low+high) // 2
    if nums[mid] >= target:
        lb = mid
        high = mid-1
    else:
        low = mid+1
return lb




n = len(nums)
ub = n
low = 0, high=n-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]>=target:
        ub=mid
        high=mid-1
    else:
        low=mid+1
return ub


# Time Complexity: O(log2(n))