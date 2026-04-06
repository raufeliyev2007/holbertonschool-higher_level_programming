#!/usr/bin/python3
import random
number = random.randint(-10,10)
if 10 >= number > 0:
    print("positive")
elif number == 0:
    print("zero")
elif -10<= number < 0:
    print("negative")
else:
    print("wrong type")
