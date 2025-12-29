def remove_outer_parentheses(s):
    result = []
    depth = 0
    for ch in s:
        if ch == '(':
            depth += 1
            if depth > 1:  # logic: add only inner '('
                result.append(ch)
        else:
            depth -= 1
            if depth > 0:  # logic: add only inner ')'
                result.append(ch)
    return ''.join(result)

test_cases = ["(()())(())", "(()())(())", "(()(())(())"]
for s in test_cases:
    print(f'Input:  {s}')
    print(f'Output: {remove_outer_parentheses(s)}')
    print('---')

# Time Complexity: O(n)
# Space Complexity: O(1) (ignoring output storage)
