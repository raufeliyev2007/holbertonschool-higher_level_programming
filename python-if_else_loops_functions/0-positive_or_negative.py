#!/usr/bin/python3
number = int(input())
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
elif number < 0:
    print(f"{number} is negative")
else:
    print("wrong type")
