'''Самый большой и самый маленький'''
n = [123, 12, 56, 34, 87, 9, 10, 413]
max = n[0]  # здесь храню максимум
min = n[0]  # здесь храню минимум
for number in n:  # перебираю числа в списке
    if max < number:  # если число из списка больше максимума
        max = number  # переназначить максимум
    if min > number:  # если число из списка меньше минимума
        min = number  # переназначить минимум
    # повторять, пока числа не закончатся
print('Самый большой элемент: ', max)
print('Самый маленький элемент: ', min)