def larget_oddNuber(s):
    n = len(s)
    for i in range(n-1, -1, -1):
        if int (s[i]) % 2 == 1:
            return s[:i+1]
    return ""   
test_cases = ["52", "4206", "35427", "1234", "2468", "9876543210"]
for s in test_cases:
    print(f'Input:  {s}')
    print(f'Output: {larget_oddNuber(s)}')
    print('---')

    # Time Complexity: O(n)
    # Space Complexity: O(1)
