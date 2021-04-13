'''Редактирование строк'''

my_array = [14, 92, 13, 58, 25, 61, 26]
my_string = '14, 92, 13,'

my_array[2] = 'тринадцать'
print(my_array)

'''Чтобы заменить символ в строке, используем
метод 
⭐️ - .replace('x', 'y', n) - меняем х на у n раз'''
clean_string = my_string.replace(',', '', 2)
print(clean_string)

