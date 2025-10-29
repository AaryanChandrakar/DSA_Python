# Bubble Sort
"""
# Code that works as Best Case 

def bubble_sort(nums):
    n = len(nums)
    
    for i in range(n-2, -1, -1):
        is_swap = False
        
        for j in range(0, i+1):
            
            if nums[j] > nums[j+1]:
            
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True
        
        if not is_swap:
            break
    
    return nums

numbers = [5, 8, 1, 6, 9, 2, 4]
print("Original array:", numbers)
bubble_sort(numbers)
print("Sorted array:", numbers)

#  Time COmplexity (Avg/Worst): 0(n^2)
#  Time Complexity(Best Case): 0(n)
# Space Complexity: 0(1)
"""
#nums = [5,8,1,6,9,2,4]
#index   0 1 2 3 4 5 6

#Note: Bubble sort works upon adjacent swap
"""
Capuring the bigger values and sending them at the last/end side of array, one-by-one

Above statement is performed into parts, means it works in iteration
--> at first the biggest value will move at the last index
--> then second largest value will take place at one index before the last index
and so on, here you can see

At Starting : Here First Outer Loop Starts
[5, 8, 1, 6, 9, 2, 4]
 ^  ^                   5 is smaller than 8, no change required
[5, 8, 1, 6, 9, 2, 4]
    ^  ^                8 is bigger than 1, swap these values
[5, 1, 8, 6, 9, 2, 4]  
       ^  ^             8 is bigger than 6, swap these values
[5, 1, 6, 8, 9, 2, 4]
          ^  ^          8 is smaller tha 9, no change required
[5, 1, 6, 8, 9, 2, 4] 
             ^  ^       9 is bigger than 2, swap these values
[5, 1, 6, 8, 2, 9, 4]   
                ^  ^    9 is bigger than 4, swap these values
[5, 1, 6, 8, 2, 4, 9]
                        Here we can see the bigger value in array 
                        have been sorted, and placed at right index (last index)

Similarly this process will be repeated in iteration untill we get sorted array.

Again we will start : Second outer loop stats here
[5, 1, 6, 8, 2, 4, 9]
 ^  ^                  5 is bigger than 1, swap these numbers
[1, 5, 6, 8, 2, 4, 9]
    ^  ^               5 is smaller than 6, no change requires
[1, 5, 6, 8, 2, 4, 9]
       ^  ^            6 is smaller than 8, no change requires
[1, 5, 6, 8, 2, 4, 9]
          ^  ^         8 is bigger than 2, swap these numbers
[1, 5, 6, 2, 8, 4, 9]    
             ^  ^      8 is bigger than 4, swap thse numbers
[1, 5, 6, 2, 4, 8, 9]
                ^  ^   8 is smaller than 9, no change requires

Again we will start : Third outer loop stats here
[1, 5, 6, 2, 4, 8, 9]
 ^  ^                  1 is smaller than 5, no change requires
[1, 5, 6, 2, 4, 8, 9]
    ^  ^               5 is smaller than 6, no changes equires
[1, 5, 6, 2, 4, 8, 9]
       ^  ^            6 is bigger than 2, no changes required
[1, 5, 6, 2, 4, 8, 9]
          ^  ^         2 is smaller than 4, no chages required
[1, 5, 6, 2, 4, 8, 9]
             ^  ^      4 is smaller than 8, no changes required
[1, 5, 6, 2, 4, 8, 9]            
                ^  ^   8 is smaller than 9, no changes required

Again we will start : Fourth outer loop stats here
[1, 5, 6, 2, 4, 8, 9]
 ^  ^                  1 is smaller than 5, no changes required
[1, 5, 6, 2, 4, 8, 9]
    ^  ^               5 is smaller than 6, no change required
[1, 5, 6, 2, 4, 8, 9]
       ^  ^            6 is bigger than 2, swap these numbers
[1, 5, 2, 6, 4, 8, 9]
          ^  ^         6 is bigger than 4, swap these numbers
[1, 5, 2, 4, 6, 8, 9]
             ^  ^      6 is smaller than 8, no changes required
[1, 5, 2, 4, 6, 8, 9] 
                ^  ^   8 is smaller than 9, no changes required

Again we will start : Fifth outer loop stats here
[1, 5, 2, 4, 6, 8, 9]
 ^  ^                  1 is smaller than 5, no changes required 
[1, 5, 2, 4, 6, 8, 9]
    ^  ^               5 is bigger than 2, swap these numbers 
[1, 2, 5, 4, 6, 8, 9]
       ^  ^            5 is bigger than 4, swap these numbers
[1, 2, 4, 5, 6, 8, 9]
          ^  ^         5 is smaller than 6, no change required 
[1, 2, 4, 5, 6, 8, 9]
             ^  ^      6 is smaller than 8, no change required
[1, 2, 4, 5, 6, 8, 9]
                ^  ^   8 is smaller than 9, no changes required   

"""


