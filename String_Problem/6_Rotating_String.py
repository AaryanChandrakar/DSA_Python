def rotate_string(s1, s2):
    if len(s1) != len(s2):
        return False
    temp = s1 + s2
    if s2 in temp:
        return True
    else:
        return False

print(rotate_string("abcde", "cdeab"))
print(rotate_string("aaryan", "naarya"))
print(rotate_string("aaryan", "ayush"))

