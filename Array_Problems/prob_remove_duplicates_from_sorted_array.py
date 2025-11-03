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
nums = [1,1,1,2,3,4,4,7,9,9, 9,10]
#index  0 1 2 3 4 5 6 7 8 9 10 11

#Brute force:
# take frequency_map that contains key (quique ele of array)
# for each key you put same value as '0' (zero, bcos we dont require)

def remove_duplicate(nums):
    n = len(nums)
    freq_map = {}
    for i in range(0,n):
        freq_map[nums[i]] = 0
    j = 0
    for k in freq_map:
        nums[j] = k
        j+=1
    return j
print("Array: ",nums)
print("After Removing Duplicates, the unique element remains is: ",remove_duplicate(nums))

#  Time Complexity: 0(2n) ~= 0(n)
# Space Complexity: 0(n)   (worstcase, if all elements are unique)

# Optimal Solution by "Two Pointer":
"""
# nums = [1,1,1,2,3,4,4,7,9,9,9,10]
          ^ ^                       both are same, move 2nd pointer to next element
          ^   ^                     again same, move 2d pointer to next ele
         [1,1,1,2,3,4,4,7,9,9,9,10]
          ^     ^                   both are diff, replace ele pointed by 2nd with element next to 1st pointer
         [1,2,1,1,3,4,4,7,9,9,9,10]
            ^     ^                 again diff, 1st pointer will move, replace            

"""