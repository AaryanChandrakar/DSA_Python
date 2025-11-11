# Find the missing number


# Bruteforce Approach:
def find_missing_number(nums):
    n = len(nums)
    for i in range(0,n+1):          # --> T.C = O(n)
        if i not in nums:           # --> T.C = O(n)
            return i
    return -1
nums = [1,0,3,4]
print("Missing Element: ",find_missing_number(nums))
nums1 = [9,6,4,2,3,5,7,0,1]
print("Missing Element: ",find_missing_number(nums1))
nums2 = [3,0,1]
print("Missing Element: ",find_missing_number(nums2))
nums3 = [0,1,2,3,4]
print("Missing Element: ",find_missing_number(nums3))
# Time Complexity:  O(n)
# Space Complexity: O(1)
print("----------------------------------------------")


# Better Approach (using dictionary)
def fun_better_solution(nums):
    n = len(nums)
    freq = {}
    for i in range(0, n+1): #-> O(n)
        freq[i] = 0         #-> O(1)
    for num in nums:        #-> O(n)
        freq[num] = 1       #-> O(1)
    for k,v in freq.items():#-> O(n)
        if v==0:            #-> O(1)
            return k
print("Missing value in array is: ",fun_better_solution(nums))
print("Missing value in array is: ",fun_better_solution(nums1))
print("Missing value in array is: ",fun_better_solution(nums2))
print("Missing value in array is: ",fun_better_solution(nums3))
# Time Complexity = O(3n)
# Space Complexity = O(n)
print("------------------------------------------------")



#Optimal Solution
def fun_optimal_solution(nums):
    n = len(nums)
    return (n*(n+1)/2) - sum(nums)
print('Missing Element: ',fun_optimal_solution(nums))
print("Missing Element: ",fun_optimal_solution(nums1))
print("Missing Element: ",fun_optimal_solution(nums2))
print("Missing Element: ",fun_optimal_solution(nums3))
# Time Complexity:  O(n)
# Space Complexity: O(1)

