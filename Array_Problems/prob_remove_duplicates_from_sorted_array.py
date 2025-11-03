# Remove duplicates from sorted array (In Place)



"""
first check the current element, 
    is it equal to next element, 
        if yes then, just leave and move to next iteration
        if no then, count it as unique element
"""
"""
def removeDuplicates(nums):
    n = len(nums)
    if n == 0:
        return 0
    i = 0
    for j in range(1, n):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

nums = [1,1,2,2,3,3,4,5,5]
new_length = removeDuplicates(nums)
print("New length:", new_length)
print("Array after removing duplicates:", nums[:new_length])

#  Time Complexity: 0(n)
# Space Complexity: 0(1)

"""
nums = [1,1,1,2,3,4,4,7,9,9,9,10]

