# Longest Consecutive Sequence 

# nums = [1,99,101,98,2,5,3,99,100]
#        [1,2,3,5,98,99,99,100,101]
# Here longest consecutive sequence is 1,2,3  or 99,100,101
# So, length of longest consecutive sequence is 3

# Bruteforce Approach (using extrspace, convertion: list --> set --> list)
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
    return max(cons_length, max_length)
print("Longest Consecutive Sequence in Array: ",fun(nums))
# Time Complexity:  O(n^2)
# Space Complexity: O(n)
print("------------------------------------------------")

#Bruteforce Approach (without extra space)
def my_fun(nums):
    n = len(nums)
    max_length = 0
    for num in nums:
        length = 1
        while num+1 in nums:
            length+=1
            num+=1
        max_length = max(length, max_length)
    return max_length
print("Max length of consecutive sequece in array is: ",my_fun(nums))
# Time Complexity:  O(n^2)
# Space Complexity: O(1)
print("-------------------------------------------------------")

#Better Approach
 
def fun_better(nusm):
    nums.sort()      # T.C. --> O(n logn)
    n = len(nums)
    count = 0
    longest = 0
    last_smallest = float("-inf")
    for i in range(1,n):    # T.C. --> O(n)
        if nums[i] == nums[i-1]:
            continue
        elif nums[i] == nums[i-1]+1:
            count+=1
        else:
            longest = max(longest, count)
            count = 1    
    return max(longest, count)
print("Longest Consecutive Sequence in Array: ",fun_better(nums))
# Time Complexity:  O(nlogn + n)
# Space Complexity: O(1)
print("------------------------------------------------")

# Optimal Approach
def fun_opt(nums):
    my_set = set()
    n = len(nums)
    for i in range(0,n):
        my_set.add(nums[i])

    longest = 0
    for num in my_set:
        if num-1 not in my_set:
            n = num
            count = 1
            while n+1 in my_set:
                count+=1
                n+=1
        longest = max(longest,count)
    return longest
print("longest Consecutive Sequence in array: ",fun_opt(nums))
# Time Complexity:  O(n+n+n) ~= O(n)
# Space Complexity: O(n)
    
