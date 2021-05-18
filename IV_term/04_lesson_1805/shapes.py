def triag(t, a):
    from math import sqrt
    hyp = a * sqrt(2)
    t.fd(a)
    t.lt(135)
    t.fd(hyp)
    t.lt(135)
    t.fd(a)

def colored_square(t, length, x, y, bg='black', color='black'):
    """Функция рисования квадрата"""
    t.goto(x, y)  # переместить черепашку в x, y
    t.down()  # опустить перо (начать рисовать)
    t.color(color)  # задать черепашке цвет через параметр (по умолчанию - черный)
    t.fillcolor(bg)
    t.begin_fill()
    for i in range(4):
        t.fd(length)
        t.rt(90)
    t.end_fill()
    t.up()  # поднять перо (перестать рисовать)


def colored_triangle(t, length, x, y, thickness, bg='black', color='black'):
    t.goto(x, y)
    t.pensize(thickness)
    t.down()
    t.color(color)
    t.fillcolor(bg)
    t.begin_fill()
    for i in range(3):
        t.fd(length)
        t.lt(120)
    t.end_fill()
    t.up()
    t.pensize(1)


def colored_rectangle(t, length, x, y, bg='black', color='black'):
    t.goto(x, y)
    t.color(color)
    t.down()
    t.fillcolor(bg)
    t.begin_fill()
    for i in range(2):
        # рисую длинную сторону
        t.fd(length)
        t.rt(90)
        # рисую короткую сторону
        t.fd(length / 2)
        t.rt(90)
    t.end_fill()
    t.up()
