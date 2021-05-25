'''
Чтобы передать функции неограниченное количество элементов,
необходимо использовать звездочки.
*args - список аргументов
**kwargs - список именованных аргументов

На примере задачи. Дан список чисел, длина списка неизвестна,
сложите все числа в списке между собой. Верните сумму.
'''
from random import randint


n = []
for number in range(randint(1, 70)):
    n.append(randint(-100, 100))

print(n)


def sum_list(*numbers):
    '''Функция получает любое количество аргументов'''
    print(type(numbers))
    s = 0
    for i in numbers:
        s += i
    return s

print(sum_list(4, 6, 7, 2))  # можно указывать любое количество чисел
print(sum_list(*n))  # распаковка списка (достать из него только числа и убрать скобки)


def smth(**kwargs):
    '''Именованные аргументы в неограниченном количстве'''
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(f'Key: {key}\nValue: {value}')

smth(name='Jagor', Age=26, Hobby='Programming', Pet='Cat')
