import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")

objs = []
colors = ["violet", "blue", "green", "yellow", "orange", "red"]
top = 100
for i in range(6):
    tim = t.Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.setposition(-200, top)
    top -= 40
    objs.append(tim)

game_on = True
while game_on:
    for j in objs:
        if j.pos()[0] > 200:
            game_on = False
            if bet == j.pencolor():
                print("You have won the bet!!!")
            else:
                print("You have lost the bet!!!")
            break
        j.forward(random.randint(0, 10))

screen.exitonclick()
