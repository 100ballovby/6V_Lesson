from turtle import *

tina = Turtle()
tina.shape('turtle')

tina.fd(100)  # .fd(step), .forward(step) пойти вперед step шагов
tina.lt(45)  # .lt(deg), .left(deg) повернуть влево на deg градусов
tina.bk(120)  # .bk(step), .backward(step) пойти назад step шагов
tina.rt(90)  # .rt(deg), right(deg) повернуть вправо на deg градусов

tina.up()  # не рисовать
tina.fd(150)
tina.down()  # рисовать

done()
