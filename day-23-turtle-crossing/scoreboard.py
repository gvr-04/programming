from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(270)
        self.setx(-240)
        self.level = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.level += 1
        self.write(f"level: {self.level}", align="center", font=("ArcadeClassic", 20, "normal"))

    def g_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("ArcadeClassic", 20, "normal"))

    def won(self):
        self.goto(0, 0)
        self.write("CONGRATS !!! You Won", align="center", font=("ArcadeClassic", 20, "normal"))
