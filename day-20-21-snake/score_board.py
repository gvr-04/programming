from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("highscore.txt") as data:
            self.hs = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(280, 0)
        self.goto(0, 270)
        self.hideturtle()
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.hs = max(self.hs, self.score)
        with open("highscore.txt", mode="w") as data:
            data.write(str(self.hs))
        self.write(f"Score: {self.score} Highscore: {self.hs}", align="center", font=("ArcadeClassic", 20, "bold"))

        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("ArcadeClassic", 30, "bold"))
