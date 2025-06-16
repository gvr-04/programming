from time import sleep
import pandas
import turtle as t
from name import New

screen = t.Screen()
screen.title("U.S States Game")
screen.setup(750, 550)
screen.addshape("blank_states_img.gif")
t.shape("blank_states_img.gif")
n = New()

df = pandas.read_csv("50_states.csv")
states = df.state.to_list()
x = df.x.to_list()
y = df.y.to_list()
d = {}
for i in range(len(states)):
    d[states[i]] = (x[i], y[i])

score = 0
game_on = True
answered = 0
title0 = "Name A State In The U.S.A"
title1 = "Correct !!! Name Another State: "
title2 = " Name Another State: "
while game_on:
    sleep(0.1)
    match answered:
        case 0:
            ti = title0
        case 1:
            ti = title1
        case 2:
            ti = title2
        case _:
            ti = title0

    ans = screen.textinput(title=f"Score: {score}/50", prompt=ti)

    if ans is None:
        game_on = False
    else:
        ans = ans.title()

    if ans in d:
        score += 1
        n.writing(state=ans, co_or=d[ans])
        d.pop(ans)
        states.remove(ans)
        answered = 1
    else:
        answered = 2

    if score == 50:
        n.writing(state="Congrats You Won!!!", co_or=(0, 0))
        game_on = False

ds = pandas.Series(states)
# ds.to_csv("learn_these.csv")
t.exitonclick()
