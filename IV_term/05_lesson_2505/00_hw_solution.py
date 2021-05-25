from turtle import *


def x_angle(t, x, y, angle, side):
    t.goto(x, y)
    t.down()
    for i in range(angle):
        t.fd(side)
        t.lt(360 / angle)
    t.down()


t = Turtle()
t.shape('turtle')
t.up()

x_angle(t, 100, -100, 36, 10)

done()