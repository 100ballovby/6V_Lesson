'''
Ошибки - это когда вы налажали.
Неправильное использование конструкций языка.

Исключение - это когда налажали НЕ вы.
Код написан правильно, но пользуются
ей неправильно.

if 2 + 3 = 5
    print('DA') <- ошибка = вместо == и не стоит : в конце условия

a = int(input('Введите целое число: '))
5.6 <- исключение
'''

x = int(input('Введите число: '))
if x > 10:
    raise Exception('x должна быть меньше 10')
