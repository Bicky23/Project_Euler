num_list = [i for i in range(1,101)]

sum_of_squares = sum([i**2 for i in num_list])
square_of_sum = (sum(num_list))**2

res = square_of_sum - sum_of_squares
print(res)
