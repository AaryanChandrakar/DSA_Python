#s = nitin    # this word is palindrom, in this case return 'True'

#s2 = mom     # this word is palindrm, return 'True'

# First we will solve this by loop, later we will solve this by recursion
def is_palindrom(s):
    """
    we are not treating l and r as parameter, 
    but it is necessary to have these pointers l and s to be in parameter in case of recursion
    """
    l = 0
    r = len(s)-1

    while(l <= r):
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    
    return True
s = "nitin"
print(s,"is palindrom: ",is_palindrom(s))

s2 = "abcdeedcba"
print(s2,"is palindrom: ",is_palindrom(s2))

#  Time complexity : 0(n/2) ~= 0(n)
# Space Complexity : 0(1)


# Now let's sove it by recursion

def is_palindrom_rec(s,l,r):

    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    
    return is_palindrom_rec(s,l+1,r-1)


s3 = "nitin"
print(s3,"is palindrom (using recursion): ",is_palindrom_rec(s3,0,len(s3)-1))

s4 = "Aaryan"
print(s4,"is palindrom (using recursion): ",is_palindrom_rec(s4,0,len(s4)-1))

s5 = "AABCDEA"
print(s5,"is palindrom (using recursion): ",is_palindrom_rec(s5,0,len(s5)-1))

#  Time Complexity : 0(n/2) ~= 0(n)
# Space Complexity : 0(n/2) ~= 0(n)  --> It is Stack Space


