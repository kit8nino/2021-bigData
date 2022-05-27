import math


def calculate(x):
    return x - (2 * math.sin(x) - math.atan(x))


def solve_equation(a, b, e):
    # никаких переменных и циклов быть не должно
    curIter = 1
    x = (a + b) / 2
    y = calculate(x)
    while abs(y - x) > e:
        x = y
        y = calculate(x)
        curIter += 1
    if a < x < b:
        return f"{curIter} step: X = {x}, Y = {2 * math.sin(x) - math.atan(x)}"
    else:
        print('The program cannot calculate Xs with a given accuracy in a given range')
        print('However, X was found in a another range')
        return f"{curIter} step: X = {x}, Y = {2 * math.sin(x) - math.atan(x)}"


print("\nEquation: 2 * sinX - arctgX = 0")
entry = 2.5
end = 2.6
accuracy = float(input("Accuracy of the equation?\n"))

print(solve_equation(entry, end, accuracy))
