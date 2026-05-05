def lengthOfLongestSubstring(s: str) -> int:
        maxi = 0
        my_dict = {}
        left = 0
        right = 0
        n = len(s)

        while right < n:
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]]+1)


            my_dict[s[right]] = right
            maxi = max(maxi, right-left+1)
            right += 1
            
        return maxi


s = "abcabcbb" # Expected output for this string: 3
result = lengthOfLongestSubstring(s)
print(result)

s1 = "bbbbb"
print(lengthOfLongestSubstring(s1))