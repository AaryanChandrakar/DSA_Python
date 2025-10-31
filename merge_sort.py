# Merge Sort

# nums = [3,1,2,4,1,5,2,6,4]
#index    0 1 2 3 4 5 6 7 8
"""
            [3,1,2,4,1,5,2,6,4]
              /             \
        [3,1,2,4]        [1,5,2,6,4]
         /     \          /        \
    [3,1]     [2,4]    [1,5]       [2,6,4]
    /   \     /  \     /   \        /    \  
 [3]   [1]  [2]  [4]  [1]  [5]    [2]   [6,4]
                                        /  \       
                                      [6]   [4]

Merging: 
  [1,3]   [2,4]       [1,5]     [2] [4,6]
     \     /             \       \    / 
    [1,2,3,4]           [1,5]    [2,4,6]
       \                   \       /
        \                 [1,2,4,5,6]
         \                  /
          [1,1,2,2,3,4,4,5,6]

"""

def merge_array(left, right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)
    while(i<n and j<m):
        if (left[i]<=right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if (i<n):
        while (i<n):
            result.append(left[i])
            i+=1
    if (j<m):
        while (j<m):
            result.append(right[j])
            j+=1
    return result



def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    left_arr = nums[:mid]
    right_arr = nums[mid:]
    
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge_array(left,right)


nums = [3,1,2,4,1,5,2,6,4]
print("Unsorted Array: ",nums)

print("**Merge Sort Applied**")
print("Sorted Array: ",merge_sort(nums))
