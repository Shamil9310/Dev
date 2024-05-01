from math import sqrt
from typing import Optional


def add_numbers(number_one: int, number_two: int) -> int:
    """Возвращяет сумму двух чиссел."""
    return number_one + number_two


def calculate_square_root(number: int) -> float:
    return sqrt(number)


def calc(your_number: int) -> Optional[str]:
    if your_number <= 0:
        return
    return (f'Мы вычислили квадратный корень из введённого вами числа.'
            f' Это будет: {number}')


number_one = 10
number_two = 5
number = calculate_square_root(25.5)


print('Сумма чисел:', add_numbers(number_one, number_two))

print(calc(number))