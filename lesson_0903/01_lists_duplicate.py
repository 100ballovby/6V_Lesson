from random import randint

first_list = []  # создаем пустой список и наполняем его элементами
for number in range(15):
    first_list.append(randint(1, 10))

print(first_list)  # в списке есть повторяющиеся числа.
# уберите дубликаты
second_list = []
# вот сюда записать уникальные числа

for every_number in first_list:  # для каждого числа в списке
    if every_number in second_list:  # если число есть во втором списке
        pass  # ничего не делать
    else:  # если числа во втором списке нет
        second_list.append(every_number)  # добавить его
print('Уникальные: ', second_list)

print('уникальные', set(first_list))
