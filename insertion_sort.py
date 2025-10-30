# Insertion Sort
# nums = [3,5,6,4,8,9,10,7,1]
#         0 1 2 4 5 6  7 8 9

"""
nums = [3,5,6,4,8,9,10,7,1]
        
select first value of an array, by i=0

for i=0  [3,5,6,4,8,9,10,7,1]
          ^                     first value is sorted
for i=1  [3,5,6,4,8,9,10,7,1]
            ^                   5 is bigger than 3, 5 is at correct place
for i=2  [3,5,6,4,8,9,10,7,1]
              ^                 6 is bigger than 5, 6 is at correct place
for i=3  [3,5,6,4,8,9,10,7,1]
                ^               4 is smaller than 6, start shifting backword 
                                untill it became bigger than its previous element
for i=4  [3,4,5,6,8,9,10,7,1]
                  ^             8 is at correct place
for i=5  [3,4,5,6,8,9,10,7,1]
                    ^           9 is at correct place
for i=6  [3,4,5,6,8,9,10,7,1] 
                       ^        10 is at correct place
for i=7  [3,4,5,6,8,9,10,7,1]
                         ^      7 is smaller than 10, start shifting
for i=8  [3,4,5,6,7,8,9,10,1]
                           ^    1 is smaller than 10, start shifting
for i=9  [1,3,4,5,6,7,8,9,10] 
                                Now the etire array is sorted                                                    
                
"""
def insertion_sort(nums):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i-1
        while(j>=0 and nums[j]>key):
            nums[j+1]=nums[j]
            j -= 1

        nums[j+1]=key  


nums = [3,5,6,4,8,9,10,7,1]
print("Unsorted Array: ",nums)
insertion_sort(nums)
print("**Insertion Sort Applied**")
print("Sorted Array: ",nums)

#  Time Complexity: 0(n^2)
# Space Complexity: 0(1)