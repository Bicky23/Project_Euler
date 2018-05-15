seq = [1,2]
first_num = 1
last_num = 2
res = 0
while last_num <= 4000000:
    new_num = first_num + last_num
    first_num, last_num = last_num, new_num
    if first_num % 2 == 0:
        res += first_num

print(res)
