#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Если индекс вне диапазона, просто возвращаем список без изменений
    if 0 <= idx < len(my_list):
        # Эта команда меняет САМ список, который передали в функцию
        del my_list[idx]
    return my_list
