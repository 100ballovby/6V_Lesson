num1 = 5
num2 = 12

print(num1 + num2)  # оператор сложения
print(num1 - num2)  # оператор разности
print(num1 * num2)  # оператор умножения
print(num1 / num2)  # оператор деления -> 10 / 3 = 3.3333

print(num1 ** 2)  # оператор возведения в степень
print(num1 // 2)  # оператор целочисленного деления (без остатка) -> 10 // 3 = 3
print(num1 % 2)  # оператор возврата остатка от деления -> 10 % 3 = 1

num3 = 2.733
print(type(num3))  # узнать тип переменной (число, текст и т.д.)
num3 = int(num3)  # отрезать дробную часть -> 2.99 = 2
print(type(num3), num3)

num3 = 2.733
print(round(num3))  # округлить переменную num3 -> 2.51 = 3