#!/usr/bin/python3
"""Модуль для работы с квадратами."""


class Square:
    """Класс Square, определяющий квадрат."""

    def __init__(self, size=0):
        """Инициализация.

        Обрати внимание: используем self.size (без подчёркиваний),
        чтобы сразу сработал сеттер ниже.
        """
        self.size = size

    @property
    def size(self):
        """Getter: возвращает значение приватного атрибута __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: устанавливает значение __size с проверками."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Вычисляет площадь квадрата."""
        return self.__size ** 2
