#!/bin/bash/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print("{} is Negative".format("number"))
elif number > 0:
    print("{} is Positive".format("number"))
else print("{} is Zero".format("number"))
