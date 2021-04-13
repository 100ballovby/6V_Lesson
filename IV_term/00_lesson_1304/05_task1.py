user_string = input('Введите строку: ')
freq = {}  # частота букв в слове

for letter in user_string:
    keys = freq.keys()  # сохраню ключи из словаря
    if letter in keys:
        freq[letter] += 1
    else:
        freq[letter] = 1
print(freq)
