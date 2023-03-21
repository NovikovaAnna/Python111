from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """

    # Создаем таблицу n x m и заполняем ее единицами
    paths = [[1] * m for _ in range(n)]

    # Рассчитываем количество маршрутов до каждой клетки
    for i in range(1, n):
        for j in range(1, m):
            paths[i][j] = paths[i - 1][j] + paths[i][j - 1] + paths[i - 1][j - 1]

    return paths


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
