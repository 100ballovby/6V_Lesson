'''Кортеж - то же самое, что и список, только в
круглых скобках и не может изменяться'''

my_tuple = ('param1', 'param2', 'param3', 'param4')
# ^ - это кортеж
try:
    my_tuple[1] = 'parametr'
    print(my_tuple)
except:
    print('Заменять элементы нельзя!')

my_tuple = ('new_param1', 'new_param2', 'new_param3', 'new_param4')
print('Я заменил кортеж!', my_tuple)