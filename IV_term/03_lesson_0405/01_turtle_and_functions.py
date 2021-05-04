from turtle import *
from shapes import *

tina = Turtle()
tina.shape('turtle')
tina.up()

rectangle(tina, 100, 50, -200, 200, 'purple')

square(
    color='green', length=70,
    t=tina, x=-30, y=100
)
triangle(tina, 40, 100, -50, 6, 'red')
square(tina, 70, 30, 90, 'yellow')
triangle(tina, 100, -70, -45, 10, 'cyan')
square(tina, 23, -100, -100, 'pink')



done()