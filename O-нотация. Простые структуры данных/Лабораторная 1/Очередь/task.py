"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало очереди (front) находится в индексе 0
        Конец очереди (rear) находится в индексе -1, если очередь не пуста
        """
        self.items = []
        self.front = 0
        self.rear = -1

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self.items.append(elem)
        self.rear += 1 # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if self.front > self.rear:
            raise IndexError("Queue is empty")
        item = self.items[self.front]
        self.front += 1
        return item
        # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Index must be an integer")
        if self.front + ind > self.rear:
            raise IndexError("Index out of range")
        return self.items[self.front + ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        self.items = []
        self.front = 0
        self.rear = -1

    def __len__(self):
        """ Количество элементов в очереди. """
        return self.rear - self.front + 1
