# Bubble Sort
"""
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
"""
#nums = [5,8,1,6,9,2,4]
#index   0 1 2 3 4 5 6

#Note: Bubble sort works upon adjacent swap
"""
Capuring the bigger values and sending them at the end side of array, one-by-one

"""


