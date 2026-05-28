import math


def square(side):
    area = side * side
    if side % 1 == 0:
        return math.ceil(area)
    return area


side1 = float(input("Введите сторону: "))
print(f"Площадь квадрата: {square(side1)}")
