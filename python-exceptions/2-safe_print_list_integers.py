#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Если i >= len(my_list), здесь упадет IndexError
            # Это именно то, что нужно по условию
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Пропускаем только ошибки типа (не целое число)
            continue
    print("")
    return count
