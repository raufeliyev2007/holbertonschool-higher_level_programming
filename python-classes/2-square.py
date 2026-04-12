#!/usr/bin/python3
"""Модуль для работы с квадратами."""


class Square:
    """Класс Square, определяющий квадрат с валидацией размера."""

    def __init__(self, size=0):
        """Инициализация нового квадрата.

        Args:
            size (int): Размер стороны квадрата (по умолчанию 0).

        Raises:
            TypeError: Если size не является целым числом.
            ValueError: Если size меньше 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
