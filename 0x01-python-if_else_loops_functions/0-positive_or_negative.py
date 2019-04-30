#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#if number is greater than 0: is positive
if number > 0:
    print(number, "is positive")
#if number is 0: is zero
elif number == 0:
    print(number, "is zero")
#if number is less than 0: is negative
else:
    print(number, "is negative")
