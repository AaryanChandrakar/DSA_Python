# Merge 2 sorted array

# nums1 = [1,1,1,2,4,6,7]
# nums2 = [1,2,3,6,7,8,9,10]
# result =[1,2,3,4,6,7,8,9,10]

# nums1 = [1,1,1,1,1]
# nums2 = [2,2,2,2,2]
# resukt =[1,2]

nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,10]


# Using python function and set:
def merge_2_sorted_array(nums1,nums2):
    result = list(set(nums1) | set(nums2))
    result.sort()
    return result
print("Merged two sorted array without duplicacy: ",merge_2_sorted_array(nums1,nums2))


# Using Loop:
def my_fun(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    i=0
    j=0   
    result = []
    while(i<n and j<m):
        if(nums1[i] <= nums2[j]):
            if(len(result)==0 or result[-1] != nums1[i]):
                result.append(nums1[i])
            i+=1
        else:
            if(len(result)==0 or result[-1] != nums2[j]):
                result.append(nums2[j])
            j+=1

    while(i<n):
        if(len(result)==0 or result[-1] != nums1[i]):
            result.append(nums1[i])
        i+=1
    
    while(j<m):
        if(len(result)==0 or result[-1] != nums2[j]):
            result.append(nums2[j])
        j+=1

    return result
print("Merged two sorted array without duplicacy: ",my_fun(nums1, nums2))



