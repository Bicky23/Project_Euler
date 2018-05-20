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


def nth_prime(n):
    count = 1
    num = 3
    while n > count:
        if is_prime(num):
            count += 1
        num += 2
    return num - 2

print(nth_prime(10001))
