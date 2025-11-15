# Longest Consecutive Sequence 

# nums = [1,99,101,98,2,5,3,99,100]
#        [1,2,3,5,98,99,99,100,101]
nums = [1,99,101,98,2,5,3,99,100]
def fun(nums):
    dist_nums = list(set(nums))
    dist_nums.sort()
    print(dist_nums)
    n = len(dist_nums)
    cons_length = 1
    max_length = 1

    for i in range(0,n-1):
        if dist_nums[i]+1 == dist_nums[i+1]:
            cons_length+=1
        else:
            max_length = max(max_length,cons_length)
            cons_length = 1
    return max(max_length, cons_length)

print("Longest Consecutive Sequence in Array: ",fun(nums))