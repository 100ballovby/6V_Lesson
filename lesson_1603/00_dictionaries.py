'''
Словарь - это набор пар ключ:значение.
название = {
    'ключ1':'значени1',
    'ключ2':'значени2',
    ...
}
'''

user = {
    'name': 'Zodiac',
    'surname': 'Zodiacovich',
    'email': 'zody@example.com',
    'age': 43,
    'gender': 'male',
    'phone': '+375291234567',
}

'''Чтобы обратиться к элементу словаря, нужно написать 
название словаря и в [] указать ключ, который нам нужен'''
print(user['email'])

'''Перебор словаря'''
# Достать все ключи - метод .keys()
for key in user.keys():
    print(key)
print()
# Достать все значения - метод .values()
for value in user.values():
    print(value)
print()
# Достать все одновременно - метод .items()
for key, value in user.items():
    print('Ключ: ', key)
    print('Значение: ', value)
    print()