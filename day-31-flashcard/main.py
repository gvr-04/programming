from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
q, a = "", ""
lst = []


def next_que():
    global q, a, showing
    window.after_cancel(showing)
    q, a = get_word()
    screen.itemconfig(img, image=photo_f)
    screen.itemconfig(title, text="French", fill="Black")
    screen.itemconfig(text2, text=q, fill="Black")
    showing = window.after(5000, show_ans)


def get_word():
    obj = pandas.read_csv("data/french_words.csv").to_dict()
    qno = randint(0, len(obj["French"]) - 1)
    if len(obj["French"]) == 0:
        return "Congrats", "You did it!!!!"
    question, answer = obj["French"][qno], obj["English"][qno]
    obj["English"].pop(qno)
    obj["French"].pop(qno)
    return question, answer


def show_ans():
    screen.itemconfig(img, image=photo_b)
    screen.itemconfig(title, text="English", fill="White")
    screen.itemconfig(text2, text=a, fill="White")


# window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=40, pady=20)
showing = window.after(5000, show_ans)

# Card
screen = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
photo_f = PhotoImage(file="images/card_front.png")
photo_b = PhotoImage(file="images/card_back.png")
img = screen.create_image(400, 275, image=photo_f)
title = screen.create_text(400, 160, text="", font=("Arial", 30, "normal"))
text2 = screen.create_text(400, 275, text=q, font=("Arial", 40, "bold"))
screen.grid(row=0, column=0, columnspan=2)

# buttons
r = PhotoImage(file=r"images/right.png")
w = PhotoImage(file=r"images/wrong.png")
right = Button(image=r, compound=TOP, highlightthickness=0, command=next_que, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR)
right.grid(row=1, column=0)
wrong = Button(image=w, compound=TOP, highlightthickness=0, command=next_que, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR)
wrong.grid(row=1, column=1)

next_que()
window.mainloop()
