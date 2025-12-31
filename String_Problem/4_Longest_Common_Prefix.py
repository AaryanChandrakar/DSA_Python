# Longest Common Prefix in the given array of string
# This problem can be solved using vertical scanning

def fun(strs):
    if len(strs)==0:
        return ""
    
    result = ""
    base = strs[0]
    for i in range(0,len(base)):
        for word in strs[1:]:
            if i==len(word) or word[i] != base[i]:
                return result
        result += base[i]
    return result

strs = ["flow","flower","flowers"]
output = fun(strs)
print(output)

# Time Complexity:  O(m * n)
# Space Complexity: O(1)