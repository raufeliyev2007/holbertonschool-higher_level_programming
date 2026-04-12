#!/usr/bin/python3
"""Модуль для работы с квадратами."""


class Square:
    """Класс Square, определяющий квадрат."""

    def __init__(self, size=0):
        """Инициализация нового квадрата.

        Args:
            size (int): Размер стороны квадрата.
        """
        self.size = size

    @property
    def size(self):
        """Getter для извлечения размера."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter для установки размера с валидацией."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Вычисляет площадь квадрата."""
        return self.__size ** 2

    def my_print(self):
        """Печатает квадрат символами # в stdout.
        Если size равен 0, печатает пустую строку.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
