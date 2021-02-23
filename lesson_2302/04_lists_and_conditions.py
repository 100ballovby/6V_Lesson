import random

random_list = [random.randint(10, 10000) for i in range(20)]
print(random_list)

divide_by_7 = []
for number in random_list:
    # перебираю каждое число в списке random_list
    if number % 7 == 0:
        divide_by_7.append(number)
print(len(divide_by_7), 'Чисел делятся на 7.')
print(divide_by_7)