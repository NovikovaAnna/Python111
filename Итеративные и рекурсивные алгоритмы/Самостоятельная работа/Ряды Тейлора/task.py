from typing import Union
from itertools import count
from math import factorial


DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    result = term = x
    i = 3
    sign = -1
    while abs(term) > DELTA:
        term = x ** i / factorial(i)
        result += sign * term
        i += 2
        sign *= -1
    return result
    # TODO вычислить sin(x) с помощью разложения сумму бесконечного ряда
