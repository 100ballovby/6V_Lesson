a = input('Введите целое число: ')

while type(a) != int:
    try:
        a = int(a)
    except:
        print('Вы ввели не целое число!')
        a = input('Введите целое число: ')