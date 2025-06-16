from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("PONG")
s.tracer(0)
s.listen()

l_p = Paddle(-350)
r_p = Paddle(350)

b = Ball()
sc_board = ScoreBoard()

s.onkey(l_p.up, "w")
s.onkey(l_p.down, "s")
s.onkey(r_p.up, "o")
s.onkey(r_p.down, "l")

game_on = True
while game_on:
    if sc_board.r_score == 3 or sc_board.l_score == 3:
        sc_board.winner()
        game_on = False
    sleep(b.time)
    s.update()
    b.coll_p(l_p)
    b.coll_p(r_p)
    b.coll_wall()
    b.move()
    if b.lost():
        if b.xcor() >= 380:
            sc_board.goal_l()
        else:
            sc_board.goal_r()
        b.reset_pos()
        l_p.reset_pos()
        r_p.reset_pos()
        sleep(2.5)

s.exitonclick()
