# aababbbbaaaaabbbabb
"""
a --> start: 0, end: 16, max diff: 16
b --> start: 17, end:18, least diff: 0

a+b = 16+0 = 16
"""

def fun(s):
    n = len(s)

    first_index_a = s.find('a')
    last_index_a = s.rfind('a')
    x = last_index_a - first_index_a

    b_indeces = []
    for i in range(n):
        if s[i] == 'b':
            b_indeces.append(i)

    y = float('inf')
    for i in range(1, len(b_indeces)):
        y = min(y, b_indeces[i] - b_indeces[i-1])

    return x+y


print(fun("aabaa"))
print(fun("aabaaaaaaaaaaaaaabaaab"))
print(fun("aaaaaaabbbbbbbbbbbb"))
print(fun("abaabaabababababababab"))
print(fun("abababaaaaaabbb"))
