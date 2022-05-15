import math
import numpy as np


def calculateEquation(x):
    return 2 * math.sin(x) - math.atan(x)


def epsilon(x):
    return abs(calculateEquation(x) - calculateEquation(calculateEquation(x)))


def solve_equation(x, e):
    if epsilon(x) > e:
        return solve_equation(calculateEquation(x), e)
    else:
        return calculateEquation(x)


print("\nEquation: 2 * sinX - arctgX = 0")
a = 2.5
b = 2.6
accuracy = float(input("Accuracy of the equation?\n"))



print("x = ", solve_equation(x, accuracy))
