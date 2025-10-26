# Selection Sort (Ascending Order)

#nums = [5,7,8,4,1,6,9,2]
#        0 1 2 3 4 5 6 7

# Logic Building:
"""
Just consider first value is the smallest value in array. (store inside variable 'i')
take next element inside variable 'j'
compare next value 'j' with previous smallest value 'i'

if 'j' is bigger than 'i' ---> update j by shifting one index towards right side

if 'j' is  smaller than 'i' ---> update variable 'i' that cantains smallest value, 
                                  continue it till end index value
                                  at the end of iteration, when you cant find another smallest value
                                  that means you already have smallest value, then swap that value with value present at index '0'
                                   
                                  Then restart this from index '1' bcos you already have sorted value at index '0'
                                  and 'j' will start with updated index which is '2'

"""

def selection_srot(nums):
    n=len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]


nums = [5,7,8,4,1,6,9,2]
print("Undorted Array: ",nums)
selection_srot(nums)
print("Sorted Array: ",nums)

#  Time Complexity = 0(n^2)
# Space Complexity = 0(1)
