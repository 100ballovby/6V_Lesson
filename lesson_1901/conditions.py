'''
if выражение: <- если здесь истина, то выполнять:
    действие_1
    действие_1.1
else:
    действие_2
'''
num = int(input('Введите число: '))

if num % 2 == 0:  # если остаток от деления на 2 равен 0
    print('Ваше число - четное!')
else:  # иначе / в любом другом случае
    print('Ваше число нечетное!')

if num % 3 == 0 and num % 5 == 0:
    print('Ваше число делится и на 3, и на 5.')
else:
    print('Условия не выполнены.')