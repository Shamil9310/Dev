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
    return 'Мы вычислили квадратный корень из введённого вами числа. \
Это будет:', calculate_square_root(your_number)


number_one = 10
number_two = 5

print('Сумма чисел:', add_numbers(number_one, number_two))

print(calc(25.5))