# Problem: Isomorphic Strings

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping_s_to_t = {}
    mapping_t_to_s = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        if char_s in mapping_s_to_t:
            if mapping_s_to_t[char_s] != char_t:
                return False
        else:
            mapping_s_to_t[char_s] = char_t

        if char_t in mapping_t_to_s:
            if mapping_t_to_s[char_t] != char_s:
                return False
        else:
            mapping_t_to_s[char_t] = char_s

    return True


print(is_isomorphic("egge", "adda"))  # True
print(is_isomorphic("foo", "bar"))  # False
print(is_isomorphic("paper", "title"))  # True

# Time Complexity: O(n), where n is the length of the strings.
# Space Complexity: O(1), since the character set is fixed (ASCII).