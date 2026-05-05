def longestOnes(nums: list[int], k: int) -> int:
    n = len(nums)
    left = 0
    right = 0
    zeros = 0
    maxi = 0
    while right < n:
        if nums[right]==0:
            zeros += 1
        if zeros > k:
            if nums[left]==0:
                zeros -= 1
            left += 1
        if zeros <= k:
            maxi = max(maxi, right-left+1)
        right+=1
    return maxi

nums = [1,1,1,0,0,0,1,1,1,1,0] #Output must be 6
k = 2
print(longestOnes(nums,k))

nums=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1] #Output must be 10
k = 3
print(longestOnes(nums,k))