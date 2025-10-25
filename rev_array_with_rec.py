nums = [5,7,3,2,6,1,5,9]
#       0 1 2 3 4 5 6 7

# reverse an array using recursion from starting to ending
rev_nums = [9,5,1,6,2,3,7,5]
# reverse an array using recursion from index 2 to index 5
rev_nums_through_index = [5,7,1,6,2,3,5,9]


def reverse_an_array_using_recursion(nums,l,r):
    if l >= r:
        return
    nums[l],nums[r] = nums[r],nums[l]
    reverse_an_array_using_recursion(nums,l+1,r-1)

reverse_an_array_using_recursion(nums,0,len(nums)-1)
print("Reversed Array is for 'nums' is :",nums)

# Now calling that function with diff indexs (l=2 and r=5)

nums2 = [5,7,3,2,6,1,5,9]
reverse_an_array_using_recursion(nums2,2,5)
print("Revesred array for 'nums2' with l=2 amd r=5 is:",nums2)


#  Time complexity : 0(n/2) ~= 0(n)
# Space Complexity : 0(n)
