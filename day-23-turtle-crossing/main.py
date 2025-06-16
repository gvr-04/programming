import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("dim gray")
screen.listen()

pl = Player()
sc = Scoreboard()
cars = CarManager(sc.level)

screen.onkey(pl.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if randint(1, 6) == 1:
        cars.create(sc.level)
    if pl.finished():
        sc.refresh()
    for j in cars.lst:
        if j.distance(pl) < 20:
            game_is_on = False
            sc.g_over()
    if sc.level == 4:
        game_is_on = False
        sc.won()
    cars.move()

screen.exitonclick()
