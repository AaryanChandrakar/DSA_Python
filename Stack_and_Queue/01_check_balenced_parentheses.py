class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            else:
                if len(stack)==0:
                    return False
                ch = stack.pop()
                if ( (bracket==')' and ch=='(') or (bracket=='}' and ch=='{') or (bracket==']' and ch=='[') ):
                    continue
                else:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([{}])",
        "(((",
        "{[]}",
    ]

    print("Sample test cases:")
    for expression in test_cases:
        result = solution.isValid(expression)
        print(f"{expression} -> {'Balanced' if result else 'Not Balanced'}")

    expression = input("\nEnter parentheses string: ").strip()
    result = solution.isValid(expression)
    print("Balanced" if result else "Not Balanced")
