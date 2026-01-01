class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionaries to store the mappings
        map_s_to_t = {}
        map_t_to_s = {}
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # Check if there's already a mapping for char_s in map_s_to_t
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:  # Inconsistent mapping
                    return False
            else:
                map_s_to_t[char_s] = char_t
            
            # Check if there's already a mapping for char_t in map_t_to_s
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:  # Inconsistent mapping
                    return False
            else:
                map_t_to_s[char_t] = char_s
        
        return True
    


# Time Complexity:  O(n)
# Space Complexity: O(k) , k = size of character set, 26 for lower case alphabet