from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.north, key="w")
screen.onkey(fun=snake.west, key="a")
screen.onkey(fun=snake.south, key="s")
screen.onkey(fun=snake.east, key="d")

game_on = True
while game_on:
    screen.update()
    sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        score.refresh_score()
        food.refresh()
        snake.add_segment(snake.segments[-1].position(), snake.segments[-1].heading())
        snake.tail()

    if snake.head.xcor() > 280:
        snake.wall_right()

    if snake.head.xcor() < -280:
        snake.wall_left()

    if snake.head.ycor() > 280:
        snake.wall_up()

    if snake.head.ycor() < -280:
        snake.wall_down()

    if snake.detect_collision():
        score.game_over()
        game_on = False

screen.exitonclick()
