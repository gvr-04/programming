import turtle as t


def forward():
    arr.forward(10)


def backwards():
    arr.backward(10)


def clockwise():
    arr.right(10)


def counter_clockwise():
    arr.left(10)


def clear():
    arr.clear()
    arr.penup()
    arr.setposition(0, 0)
    arr.pendown()
    arr.setheading(0)


arr = t.Turtle()
screen = t.Screen()
screen.listen()

screen.onkey(fun=forward, key="w")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=backwards, key="s")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
