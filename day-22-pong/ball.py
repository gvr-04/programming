from turtle import Turtle
from random import randint, choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_pos()
        self.time = 0.06

    def reset_pos(self):
        self.goto(0, 0)
        lst = [randint(-25, 25), randint(130, 202)]
        self.setheading(choice(lst))

    def coll_p(self, obj):
        if (self.xcor() < -325 or self.xcor() > 325) and self.distance(obj) < 45:
            self.time *= 0.9
            self.setheading(180 - self.heading())

    def lost(self):
        if self.xcor() > 390 or self.xcor() < -390:
            self.time = 0.06
            return True
        else:
            return False

    def coll_wall(self):
        if self.ycor() < -280 or self.ycor() > 280:
            if self.heading() < 90 or self.heading() > 270:
                self.setheading(-self.heading())
            else:
                self.setheading(360 - self.heading())

    def move(self):
        self.forward(15)
