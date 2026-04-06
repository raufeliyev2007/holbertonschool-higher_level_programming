import random
number = randint(-10000,10000)
last=number%10
if number<0:
    last=-last
if last<6 and last==0:
    print(f"Last digit of {number} is {last} and is less than 6 and is 0")
elif last<6:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif last>5 and last==0:
    print(f"Last digit of {number} is {last} and is greater than 5 and is 0")
elif last>5:
    print(f"Last digit of {number} is {last} and is greater than 5 and not 0")
