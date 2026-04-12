#!/usr/bin/python3
"""Модуль для работы с квадратами."""


class Square:
    """Класс Square, определяющий квадрат."""

    def __init__(self, size=0):
        """Инициализация нового квадрата.

        Args:
            size (int): Размер стороны квадрата.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Вычисляет и возвращает текущую площадь квадрата.

        Returns:
            int: Площадь квадрата (size в квадрате).
        """
        return self.__size ** 2
