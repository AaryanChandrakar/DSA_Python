# Remove duplicates from sorted array (In Place)

"""
first check the current element, 
    is it equal to next element, 
        if yes then, just leave and move to next iteration
        if no then, count it as unique element
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

print("---------------------------------------------------------------------")

# Optimal Solution by "Two Pointer":
"""
# nums = [1,1,1,2,3,4,4,7,9,9,9,10]
          ^ ^                       both are same, move 2nd pointer to next element
          ^   ^                     if we dont find diff element, move the 2nd pointer to next ele
         [1,1,1,2,3,4,4,7,9,9,9,10]
          ^     ^                   both are diff, replace ele (pointed by 2nd pointer) with element next to 1st pointer
                                    then shift the 1st pointer to next element (newly replaced value) and move the 2nd pointer
         [1,2,1,1,3,4,4,7,9,9,9,10]
            ^     ^                 again diff values, move first pointer, replace value (currently pointed by 1st pointer) with 2nd pointer value
                                    then move next the 2nd pointer
         [1,2,3,1,1,4,4,7,9,9,9,10]
              ^     ^                diff, do the same steps as previous

         [1,2,3,4,1,1,4,7,9,9,9,10]
                ^     ^              not diff value, just move the 2nd pointer at next value

         [1,2,3,4,1,1,4,7,9,9,9,10]
                ^       ^            diff values, do incremetation for pointers and do swapping

         [1,2,3,4,7,1,4,1,9,9,9,10]
                  ^       ^          diff values, do increment for pointer, do swapping

         [1,2,3,4,7,9,4,1,1,9,9,10]
                    ^       ^        not diff values, just move the 2nd pointer

         [1,2,3,4,7,9,4,1,1,9,9,10]   
                    ^         ^      not diff values, just move the 2nd pointer  

         [1,2,3,4,7,9,4,1,1,9,9,10]
                    ^            ^   diff values, 2nd pointer is at last index, just perform swapping

         [1,2,3,4,7,9,10,1,1,9,9,4]  
                       ^              total 7 unique elements are there , return the pointer index + 1                                        
                              
                        
"""
def my_fun(nums1):
    n = len(nums1)
    if n==1:
        return 1
    i = 0
    j = i+1

    while(j<n):
        if nums1[j] != nums1[i]:
            i+=1
            nums1[i],nums1[j] = nums1[j],nums1[i]
        j+=1
    return i+1

nums1 = [1,1,1,2,3,4,4,7,9,9,9,9,10,10]

print("No. of Unique Elements: ",my_fun(nums1))


# Time Complexity : O(n)
# Space Complexity: O(1)
