from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-80, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create()
        self.tail()
        self.head = self.segments[0]
        self.head.shape("circle")
        self.head.color("dark sea green")

    def add_segment(self, position, direction):
        segment = Turtle("square")
        segment.color("medium sea green")
        segment.penup()
        segment.goto(position)
        segment.setheading(direction)
        self.segments.append(segment)

    def tail(self):
        self.segments[-2].shape("square")
        self.segments[-2].shapesize(1, 1, 1)
        self.segments[-2].hideturtle()
        self.segments[-3].showturtle()
        self.segments[-1].shape("triangle")
        self.segments[-1].shapesize(1, -2, 1)

    def create(self):
        for position in POSITIONS:
            self.add_segment(position, 0)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            prev_seg = self.segments[i - 1]
            self.segments[i].goto(prev_seg.pos())
            self.segments[i].setheading(prev_seg.heading())
        self.head.forward(10)

    def wall_right(self):
        self.head.goto(-280, self.head.ycor())

    def wall_left(self):
        self.head.goto(280, self.head.ycor())

    def wall_up(self):
        self.head.goto(self.head.xcor(), -280)

    def wall_down(self):
        self.head.goto(self.head.xcor(), 280)

    def detect_collision(self):
        for i in self.segments[1:]:
            if self.head.distance(i) < 5:
                return True

    def north(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def south(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def west(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def east(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
