'''
Параметры:
1. Черепашка
2. Длина стороны
3. координата х
4. координата у
5. Цвет
'''


def square(t, length, x, y, color='black'):
    """Функция рисования квадрата"""
    t.goto(x, y)  # переместить черепашку в x, y
    t.down()  # опустить перо (начать рисовать)
    t.color(color)  # задать черепашке цвет через параметр (по умолчанию - черный)
    for i in range(4):
        t.fd(length)
        t.rt(90)
    t.up()  # поднять перо (перестать рисовать)


def triangle(t, length, x, y, thickness, color='black'):
    t.goto(x, y)
    t.pensize(thickness)
    t.down()
    t.color(color)
    for i in range(3):
        t.fd(length)
        t.lt(120)
    t.up()
    t.pensize(1)


def rectangle(t, l1, l2, x, y, color='black'):
    t.goto(x, y)
    t.color(color)
    t.down()
    for i in range(2):
        # рисую длинную сторону
        t.fd(l1)
        t.rt(90)
        # рисую короткую сторону
        t.fd(l2)
        t.rt(90)
    t.up()
