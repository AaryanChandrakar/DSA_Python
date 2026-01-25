def roman_to_integer(s):
    letter = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    n = len(s)
    result = 0
    for i in range(n):
        if i<n-1 and letter[s[i]]<letter[s[i+1]]:
            result = result - letter[s[i]]
        else:
            result = result + letter[s[i]]
    return result

print(roman_to_integer("MCMXCIV"))
print(roman_to_integer("LVIII"))
print(roman_to_integer("MCMXCIV"))
print(roman_to_integer("MCMXCIV"))


        