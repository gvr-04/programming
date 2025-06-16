from turtle import Turtle


class New(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def writing(self, state, co_or):
        self.goto(co_or)
        self.write(arg=state, align="center", font=("C059", 10, "bold"))
