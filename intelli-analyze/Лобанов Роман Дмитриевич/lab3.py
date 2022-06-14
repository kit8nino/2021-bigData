import math
print('Вариант ', len('Лобанов Роман Дмитриевич') % 5)
print("Функция: 2 * sinX - arctgX = 0")

def f(x):
    return x + (2 * math.sin(x) - math.atan(x)) * (2 / (2.5 + 2.6))

def solution(x, eps):
    if abs(f(x) - x) > eps:
        return solution(f(x), eps)
    else:
        return x

epsilon = float(input("Введите погрешность"))
print("x = ", solution((2.5 + 2.6) / 2, epsilon))
