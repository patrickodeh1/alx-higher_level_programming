#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = abs(number) % 10
else:
    last_digit = number % 10

print(f"Last digit of {number:d} is {last_digit:d}")
