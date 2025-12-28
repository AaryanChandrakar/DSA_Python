def remove_outer_parentheses(s: str) -> str:
    result = []
    depth = 0

    for ch in s:
        if ch == '(':
            # Only add '(' if we are already inside (depth > 0)
            if depth > 0:
                result.append(ch)
            depth += 1
        else:  # ch == ')'
            # We are about to go one level up
            depth -= 1
            # Only add ')' if after decrement we are still inside (depth > 0)
            if depth > 0:
                result.append(ch)

    return ''.join(result)
