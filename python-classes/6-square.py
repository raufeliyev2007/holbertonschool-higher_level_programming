#!/usr/bin/python3
"""Модуль для работы с квадратами."""


class Square:
    """Класс Square, определяющий квадрат."""

    def __init__(self, size=0, position=(0, 0)):
        """Инициализация.

        Args:
            size (int): Размер стороны.
            position (int, int): Координаты квадрата.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter для размера."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter для размера с валидацией."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter для позиции."""
        return self.__size_position

    @position.setter
    def position(self, value):
        """Setter для позиции с валидацией кортежа из 2 целых чисел > 0."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size_position = value

    def area(self):
        """Возвращает площадь."""
        return self.__size ** 2

    def my_print(self):
        """Печатает квадрат с учетом позиции."""
        if self.__size == 0:
            print("")
            return

        # Печатаем пустые строки сверху (position[1])
        for _ in range(self.__size_position[1]):
            print("")

        # Печатаем сам квадрат с отступом слева (position[0])
        for _ in range(self.__size):
            print(" " * self.__size_position[0] + "#" * self.__size)
