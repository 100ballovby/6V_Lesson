guests = ['Mike', 'Nick', 'Alexandr']
''' простой способ
print(guests[0], 'welcome to my party!')
print(guests[1], 'welcome to my party!')
print(guests[2], 'welcome to my party!')
'''
# способ сложнее.
for guest in guests:
    print(guest, 'welcome to my party!')
# берем каждого гостя и выводим для него сообщение

print(guests[2], ' cant come to my party.')
# гость с номером 2 прийти не может

guests[2] = 'Sveta' # я переписываю гостя 2 в списке
for guest in guests:
    print(guest, 'welcome to my party!')

print('-----There is some new guests-----')
guests.insert(0, 'Victor') # вставляю на 0 место нового гостя
guests.insert(2, 'Valery') # вставляю на 2 место нового гостя
guests.append('NAlexey') # добавляю в конец списка нового гостя
for guest in guests:
    print(guest, 'welcome to my party!')

print('----There might be only 2 guests----')

while len(guests) > 2:
    print(guests.pop(), 'sorry.')
# пока длина списка больше 2
# удалять из списка человека (с конца)
# и одновременно выводить сообщение

for guest in guests:
    print(guest, 'welcome to my party!')




