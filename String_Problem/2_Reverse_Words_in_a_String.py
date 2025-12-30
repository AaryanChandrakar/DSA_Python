# Reverse the words in a given string.

# Way 1: Using built-in functions
def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

s = "  Hello   World  "
print(f'Input:  "{s}"')
print(f'Output: "{reverse_words(s)}"')
print('---')
# Time Complexity: O(n)
# Space Complexity: O(n)
