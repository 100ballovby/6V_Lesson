# 4-3 используйте цикл for для вывода чисел от 1 до 20 включительно.
for i in range(1, 21):  # 1, x
    print(i, end=' ')  # выводить числа в строку - end() - чем заканчивается вывод

print('\n4-5')
# 4-5. min(), max(), sum()
million = [i for i in range(1, 1000001)]
print('Наименьшее: ', min(million))
print('Набольшее', max(million))
print('Сумма', sum(million))

print('\n4-6')
# 4-6 нечетные числа 1-20
for number in range(1, 22, 2):
    print(number, end=' ')

print('\n\n4-7')
# 4-7 кубы
for i in range(1, 11):
    print(i ** 3, end=' ')

print('\n\n4-9')
# 4-9 comprehesion
cubes = [i ** 3 for i in range(1, 11)]
print(cubes)