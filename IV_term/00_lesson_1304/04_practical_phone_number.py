'''Написать программу, которая собирает номера телефонов
и приводит их к виду XXXYYXXXXXXX'''
import string

restricted = string.punctuation + ' '
# здесь хранятся все знаки препинания
phone = input('Введите номер телефона: ')
clear_number = ''

for element in phone:
    if element not in restricted:
        clear_number += element
print(clear_number)

'''Допишите программу таким образом, чтобы номер телефона мог начинаться
только на 375, а его длина была только 12 символов.'''
