def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        i = 3
        while i < n:
            if n % i == 0:
                return False
            i += 2
        return True

def sum_prime(n):
    prime_list = [2]
    num = 3
    while n > num:
        if is_prime(num):
            prime_list.append(num)
        num += 2
    return sum(prime_list)

print(sum_prime(2000000))
