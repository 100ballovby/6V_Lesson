from turtle import *
from random import choice  # функция дергает случайное значение из коллекции

tina = Turtle()
tina.shape('turtle')
screen = Screen()  # создал переменную для экрана
screen.bgcolor('black')  # цвет фона экрана
tina.color('white')  # цвет черепашки
colors = ['#3eb489', '#8de3cb', '#5ba65b', '#ffff85',
          '#ffdb29', '#ff2400', '#8b00ff', '#4d0099', '#00945b']

steps = 5  # количество шагов
thickness = 1  # толщина пера

for i in range(100):
    tina.color(choice(colors))  # устанавливаем случайный цвет
    tina.pensize(thickness)  # устанавливаем толщину пера
    tina.fd(steps)  # указываем количество шагов
    tina.rt(90)  # поворот

    steps += 7  # увеличиваю количество шагов
    thickness += 0.1  # увеличиваю толщину линии

done()
