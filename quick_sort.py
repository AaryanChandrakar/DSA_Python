# Quick Sort
"""
Step 1: Pick a pivit:
        - It can be the first element   (we'll choose this)
        - It can be the last element
        - It can be middle element
        - It can be any random elements
Step 2: Put at it's correct position/index.
"""

# nums = [4,1,7,6,3,2,8]
# pivit   ^                at firts pivit = 4

def partition(nums,low,high):
    pivot = nums[low]
    i = low
    j = high

    while(i<j):
        while(nums[i]<=pivot and i<=high-1):
            i+=1
        while(nums[j]>pivot and j>=low+1):
            j-=1
        if(i<j):
            nums[i],nums[j] = nums[j],nums[i]
    nums[low],nums[j] = nums[j],nums[low]

    return j

def quick_sort(nums,low,high):
    if(low<high):
        p_index = partition(nums,low,high)
        quick_sort(nums,low,p_index-1)
        quick_sort(nums,p_index+1,high)

nums = [4,1,7,6,3,2,8]
print("Unsorted Array: ",nums)
quick_sort(nums,0,len(nums)-1)
print("**Quick Sort Applied**")
print("Sorted Array: ",nums)

#  Time Complexity:
#                               log(n) --> quick_sort()
#                                    n --> partition()
#  Time Complexity: 0(n * log(n))  (for best and avg case)
#                   0(n^2)         (worst case, if all elements are same)
# Space Complexity: 0(1)        bcos of recursion stack space