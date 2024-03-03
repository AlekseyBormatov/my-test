from math import sqrt
from typing import Union, Optional


def add_numbers(Num_1: int, Num_2: int) -> int:
    return Num_1 + Num_2


def calculate_square_root(number: Union[int, float]) -> float:
    return sqrt(number)


def calc(your_number: Union[int, float]) -> Optional[str]:
    if your_number <= 0:
        return None
    Root = calculate_square_root(your_number)
    return ('Мы вычислили квадратный корень из введённого вами '
            f'числа. Это будет: {Root}')


Num_1: int = 10
Num_2: int = 5

print('Сумма чисел: ', add_numbers(Num_1, Num_2))

print(calc(25.5))
