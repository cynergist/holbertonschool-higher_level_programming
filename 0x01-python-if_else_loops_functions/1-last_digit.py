#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = -(last)
intro = "Last digit of "
six = " and is less than 6 and not 0"
# Output to print Last digit of _number is _truncated number_
# and is EITHER greater than 5, 0, or less than 6 and not 0
if last > 5:
    print("{}{} is {} and is greater than 5".format(intro, number, last))
elif last == 0:
    print("{}{} is {} and is 0".format(intro, number, last))
elif last < 6:
    print("{}{} is {}{}".format(intro, number, last, six))
