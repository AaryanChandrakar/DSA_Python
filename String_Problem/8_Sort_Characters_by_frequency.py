def sort_characters_by_frequency(s):
    result = ""
    hash_map = {}
    for ch in s:
        hash_map[ch] = hash_map.get(ch, 0) + 1
    sorted_hash_map = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
    for ch, freq in sorted_hash_map:
        result += ch * freq
    return result

print(sort_characters_by_frequency("tree"))
print(sort_characters_by_frequency("cccaaa"))
print(sort_characters_by_frequency("Aabb"))
print(sort_characters_by_frequency("Aaryan"))
print(sort_characters_by_frequency("hhheeellllggooooeeeeeeeee"))

#  Time Complexity: O(n) + O(nlogn) + O(n) = O(nlogn)
# Space Complexity: O(n) 
