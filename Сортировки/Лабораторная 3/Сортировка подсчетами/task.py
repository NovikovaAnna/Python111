from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    if not container:
        return container
    max_value = max(container)
    counts = [0] * (max_value + 1)
    for value in container:
        counts[value] += 1
    result = []
    for value in range(max_value + 1):
        result.extend([value] * counts[value])
    return result



