def isAnagram(s, t):
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        if s_sorted == t_sorted:
            return True
        else: 
            return False

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("Love", "evoL"))
print(isAnagram("sun", "moon"))

#  Time Complexity: O(nlogn)
# Space Complexity: O(n)