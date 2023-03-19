"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """

    n = len(arr)
    if n == 0:
        raise ValueError("Массив пустой")

    min_index = 0
    for i in range(1, n):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index
   # TODO реализовать итеративный линейный поиск
