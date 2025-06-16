from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shapesize(5, 1, 1)
        self.shape("square")
        self.color("white")
        self.penup()
        self.x = x
        self.goto(self.x, 0)

    def up(self):
        self.sety(self.ycor()+20)

    def down(self):
        self.sety(self.ycor()-20)

    def reset_pos(self):
        self.goto(self.x, 0)
