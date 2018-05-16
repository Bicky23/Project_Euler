list_of_palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        num = i * j
        pal_num = str(num)[::-1]
        if str(num) == pal_num:
            list_of_palindromes.append(num)
        else:
            pass


print(max(list_of_palindromes))
