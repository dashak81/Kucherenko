import math

# Исходные данные
x1 = 0
xn = 2
dx = 0.1
a = 2.1
b = 0.3

# Вычисление значений функции
x = x1
while x <= xn:
    y = math.cos(a * x**2) / (1 + math.tan(b * x)**3)
    print(f"x = {x:.1f}, y = {y:.5f}")
    x += dx