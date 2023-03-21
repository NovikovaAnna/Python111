from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    n = len(stairway)
    g = nx.DiGraph()
    for i in range(n):
        for j in range(i + 1, min(n, i + 3)):
            g.add_edge(i, j, weight=stairway[j])
    path = nx.dijkstra_path(g, 0, n - 1)
    return sum(stairway[i] for i in path)
    # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = create_stairway_graph(stairway)   # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    print(stairway_path(stairway_graph))  # 72
