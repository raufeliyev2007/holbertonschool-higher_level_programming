#!/usr/bin/python3
import random
number = random.randint(-10,10)
if 10 > = number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
elif -10< = number < 0:
    print("is negative")
else:
    print("wrong type")
