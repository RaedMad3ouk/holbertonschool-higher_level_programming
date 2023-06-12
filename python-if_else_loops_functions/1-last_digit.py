#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = number % (-10)
else:
    lastdigit = number % 10
if lastdigit == 0:
    str = ('and is 0')

elif lastdigit > 5:
    str = ('and is greater than 5')
else:
    str = ('and is less than 6 and not 0')
print(f'Last digit of {number} is {lastdigit} {str}')
