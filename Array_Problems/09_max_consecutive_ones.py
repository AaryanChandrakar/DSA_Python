# Max Consecutive Ones (in binaru array)

nums = [1,1,0,1,0,1,1,1,1,0,1,1]   #output: 4

def max_consicutive_ones(nums):
    count = 0
    max_count = 0
    for i in nums:
        if i == 1:
            count+=1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count
print("Max Consicutive 1's: ",max_consicutive_ones(nums))
# Time Complexity:  O(n)
# Space Complexity: O(1)

