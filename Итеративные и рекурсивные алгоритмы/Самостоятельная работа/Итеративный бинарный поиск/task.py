from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    # left, right = 0, len(seq) - 1
    #
    # while left <= right:
    #     mid = (left + right) // 2
    #     if seq[mid] == value:
    #         return mid
    #     elif seq[mid] > value:
    #         right = mid - 1
    #     else:
    #         left = mid + 1
    #
    # raise ValueError(f"Элемент {value} не найден в массиве")  # TODO реализовать итеративный алгоритм бинарного поиска

    left = 0
    right = len(seq) - 1

    while left <= right:
        middle_index = left + (right - left) // 2
        middle_value = seq[middle_index]
        if value == middle_value:
            while True:
                if not 0 <= middle_index - 1 < len(seq) or seq[middle_index - 1] != value:
                    break
                else:
                    middle_index -= 1
            return middle_index
        elif middle_value > value:
            right = middle_index - 1
        else:
            left = middle_index + 1

    raise ValueError(f"Элемента {value} нет")