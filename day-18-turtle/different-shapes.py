import turtle as t
from random import randint

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


x, y = -400, -400
tim.penup()
tim.goto(x, y)


for i in range(25):
    for j in range(25):
        tim.dot(20, (randint(0, 255), randint(0, 255), randint(0, 255)))
        x += 100/3
        tim.goto(x, y)
    x, y = -400, y+100/3
    tim.goto(x, y)
tim.hideturtle()

screen = t.Screen()
screen.exitonclick()
