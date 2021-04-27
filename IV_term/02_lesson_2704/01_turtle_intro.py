'''
import library_name --> library_name.function
import library_name as ln --> ln.function
from library_name import fun1, fun2, fun3 --> fun1()
в этом случае вы можете пользоваться только теми функциями,
которые импортировали
from library_name import * --> импортировать все

НЕ называйте файлы именем библиотек.
Например: library: turtle, file: turtle.py - нельзя
library: turtle, file: turtle_tutorial.py - можно
'''
from turtle import *  # импорт - 1 шаг

# 2 шаг - экземпляр черепашки
tina = Turtle()  # <- это ваша черепашка
tina.shape('turtle')
# весь код черепашки пишем туть

done()  # 3 шаг - не дать окну закрыться
