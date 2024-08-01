class StepValueError(ValueError):

    def __init__(self, message):
        self.message = message


def is_prime(func):
    def prime_number(a, b, c):
        n = func(a, b, c)
        if n < 1: raise StepValueError('ERROR!!! Сумма трёх исходных чисел не может быть меньше 1')
        if 0 < n < 3: return True, n
        for i in range(2, n - 1):
            if n % i == 0: return False, n
        return True, n

    return prime_number


@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result


a, b, c = 1, -2, 1

try:
    result = sum_three(a, b, c)
    print('Простое') if result[0] else print('Составное')
    print(result[1])
except StepValueError as exc:
    print(f'Недопустимое число: {exc.message}')
