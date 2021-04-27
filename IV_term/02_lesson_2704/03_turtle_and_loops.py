from turtle import *

tina = Turtle()
tina.shape('turtle')
tina.speed(0)  # диапазон от 1 до 10, 0 - это 10
tina.pensize(5)  # выбрать размер пера, по умолчанию - 1


# квадрат
for i in range(4):
    tina.fd(100)
    tina.rt(90)

tina.up()
tina.goto(100, -50)  # goto(x, y) - переместить черепаху в координаты x, y
tina.down()
# круг
for i in range(36):
    tina.fd(10)
    tina.rt(10)

tina.up()
tina.goto(0, 0)
tina.down()

# треугольник
tina.fillcolor('yellow')  # цвет заливки
tina.begin_fill()  # начать закрашивать
for i in range(3):
    tina.fd(100)
    tina.lt(120)
tina.end_fill()  # закончить закрашивать

done()
