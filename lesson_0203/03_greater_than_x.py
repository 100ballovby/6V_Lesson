'''Task 3. Найти все числа в списке, которые больше X.
Х вводится пользователем с клавиатуры.
'''

x = int(input('Введите число: '))
n = [123, 12, 56, 34, 87, 9, 10, 413]

for number in n:
    if x < number:
        print(number)

g_x = [number for number in n if number >= x]
print(g_x)