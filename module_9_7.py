def is_prime(func):
    def prime_number(a, b, c):
        n = func(a, b, c)
        if 0 < n < 3: return True, n
        for i in range(2, n - 1):
            if n % i == 0: return False, n
        return True, n

    return prime_number


@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result


result = sum_three(2, 3, 6)
print('Простое') if result[0] else print('Составное')
print(result[1])
