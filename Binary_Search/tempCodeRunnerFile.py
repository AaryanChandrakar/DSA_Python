
            high=mid-1
        else:
            low=mid+1
    return ub
print("Upper Bound: ",upper_bound(nums,target))
# Time Complexity:  O(log2(n))
# Space Complexity: O(1)
