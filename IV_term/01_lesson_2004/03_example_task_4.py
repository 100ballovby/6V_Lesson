'''Task 4. Вводится строка. Найти и убрать из строки все знаки препинания,
пробелы. Привести все буквы к нижнему регистру (сделать маленькими)'''
import string

restricted = string.punctuation + ' '
# собираю все знаки препинания
message = input('Введите что-то: ').strip().lower()

for symbol in restricted:
    message = message.replace(symbol, '')

print(message)
