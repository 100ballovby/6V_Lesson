'''Task 0. Вводится строка. Необходимо посчитать
количество больших букв. Например:
[in]--> Привет, Андрей!
[out]--> 2
'''

message = input('Введите что-то: ')
# храню передаваемое сообщение

big = 0
bl = []
for letter in message:
    if letter.isupper():
        big += 1
        bl.append(letter)

print(f'В строке {big} больших букв.')
print(f'Большие буквы: {bl}')
