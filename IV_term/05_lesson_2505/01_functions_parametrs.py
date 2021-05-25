'''
Позиционные аргументы - аргументы функции, которые находятся в строгой
очередности и смена аргументов фактически влияет на работу функции
НЕ позиционные аргументы - аргументы функции, позиция которых плавает
'''


def power(number, pow):
    return number ** pow


'''
Любой аргумент можно сделать НЕ позиционным (именованным), если просто указать его  имя
'''

print(power(5, 7))  # первый способ вызова
print(power(pow=7, number=5))  # вызов фукнции с именованными аргументами


'''
Аргументы с предустановленным значением
'''


def multiply(number1, number2=2):  # аргумент будет заменен в случае передачи
    # но писать его не необязательно
    # аргументы по умолчанию должны стоять в конце
    return number1 * number2

print(multiply(5, 8))
print(multiply(number2=7, number1=6))
