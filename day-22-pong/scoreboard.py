from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.sety(210)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.l_score}    {self.r_score}", align="center", font=("ArcadeClassic", 70, "normal"))

    def goal_l(self):
        self.l_score += 1
        self.write_score()

    def goal_r(self):
        self.r_score += 1
        self.write_score()

    def winner(self):
        if self.l_score == 3:
            self.goto(0, 0)
            self.write("Game Over, Left player wins", align="center", font=("ArcadeClassic", 30, "bold"))
        elif self.r_score == 3:
            self.goto(0, 0)
            self.write("Game Over, Right player wins", align="center", font=("ArcadeClassic", 30, "bold"))
