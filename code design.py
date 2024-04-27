from math import sqrt


def add_numbers(number_one, number_two):
    return number_one + number_two


def сalculatesquareroot(number):
    return sqrt(number)


def calc(your_number):
    if your_number <= 0:
        return
    return (f'Мы вычислили квадратный корень из введённого вами числа.'
    f' Это будет: {сalculatesquareroot(your_number)}')


number_x = 10
number_y = 5

print('Сумма чисел: ', add_numbers(number_x, number_y))

print(calc(25.5))
