#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
remainder = abs(number) % 10
if number < 0:
    remainder = - remainder
if remainder > 5:
    print(f"Last digit of {number:d} is {remainder:d} and is greater than 5")
elif remainder == 0:
    print(f"Last digit of {number:d} is {remainder:d} and is 0")
elif remainder < 6 and remainder != 0:
    print(f"Last digit of {number:d} is {remainder:d} and is less" +
          " than 6 and not 0")
else:
    pass
