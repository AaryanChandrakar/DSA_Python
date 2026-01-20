def fun(nums, k):
    n = len(nums)
    k = k%n
    rotated_list = nums[-k:] + nums[:-k]
    return rotated_list


nums = [1,2,3,4,5]
k = 3
print(fun(nums, k))
