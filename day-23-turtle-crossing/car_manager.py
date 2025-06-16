from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self, lvl):
        self.lst = []
        self.dist = STARTING_MOVE_DISTANCE
        self.create(lvl)

    def create(self, level):
        car = Turtle("square")
        car.color(choice(COLORS))
        car.penup()
        car.setheading(180)
        car.shapesize(1, 2, 1)
        car.setx(300)
        car.sety(randint(-200, 250))
        self.lst.append(car)
        self.dist = STARTING_MOVE_DISTANCE + (level-1) * MOVE_INCREMENT

    def move(self):
        for i in self.lst:
            i.forward(self.dist)
