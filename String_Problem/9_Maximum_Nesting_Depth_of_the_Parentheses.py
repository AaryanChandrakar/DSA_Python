def fun(s):
    max_depth = 0
    curr_depth = 0
    for brack in s:
        if brack == "(":
            curr_depth += 1
        elif brack == ")":
            curr_depth -= 1
        max_depth = max(max_depth, curr_depth)
    return max_depth

print(fun("(1+(2*3)+((8)/4))+1)"))
print(fun("(((())))(()))"))
print(fun("()()"))
print(fun("(())()"))

