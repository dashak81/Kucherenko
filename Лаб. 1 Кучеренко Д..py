import math
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))
if abs(x)**(1/3) == 0 and y == 0:
    print("Значение выражения не может быть вычислено")
elif math.e**(abs(x-y))!= 0:
    a1 = y**(abs(x)**(1/3))
    a2 = math.cos(y)**3
    a3 = abs(x-y)*(1+math.sin(x)**2)/math.e**(abs(x-y))
    s = a1 + a2 * a3
    print("Результат ", s)
else:
    print("Значение выражения не может быть вычислено")

