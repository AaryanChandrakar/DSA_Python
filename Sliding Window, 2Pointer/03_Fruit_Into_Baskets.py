def totalFruit(fruits: list[int]) -> int:
    my_d = {}
    left = 0
    right = 0
    n = len(fruits)
    max_length = 0
    while right < n:
        my_d[fruits[right]] = my_d.get(fruits[right], 0) + 1
        if len(my_d) > 2:
            my_d[fruits[left]] -= 1
            if my_d[fruits[left]] == 0:
                del my_d[fruits[left]]
            left += 1
        if len(my_d) <= 2:
            max_length = max(max_length, right - left + 1)
        right = right + 1
    return max_length


fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(totalFruit(fruits))