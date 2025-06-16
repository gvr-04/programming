from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND = "#00563B"
LIGHT = "#ACE1AF"
TIME = "#ceffdf"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
tim = "None"
started = 0
num = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    global started
    reps = 0
    window.after_cancel(tim)
    canvas.itemconfig(timer_text, text="25:00")
    label_t.config(text="Timer")
    started = 0


# ---------------------------- TIMER MECHANISM -------------------- ----------- #
def start_timer():
    global reps
    global started

    if started == 0:
        reps += 1
        if reps % 2 != 0:
            timer(WORK_MIN * 60)
            label_t.config(text="Work", fg=LIGHT)
        else:
            label_t.config(text="Break", fg=LIGHT)
            if reps % 8 == 0:
                timer(LONG_BREAK_MIN * 60)
            else:
                timer(SHORT_BREAK_MIN * 60)
    started = 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def timer(count):
    global tim
    global reps
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    if sec == 0:
        sec = "00"
    str1 = f"{math.floor(count / 60)}:{sec}"
    canvas.itemconfig(timer_text, text=str1)
    if count > 0:
        tim = window.after(1000, timer, count - 1)
    else:
        start_timer()
        tick(math.floor(reps / 2))


def change():
    global num
    global BACKGROUND
    if num % 2 == 0:
        BACKGROUND = "#FF0000"
        canvas.itemconfig(c, image=photo1)
        text = "🌙"
    else:
        BACKGROUND = "#00563B"
        canvas.itemconfig(c, image=photo)
        text = "☀️"
    window.config(bg=BACKGROUND)
    canvas.config(bg=BACKGROUND)
    label_t.config(bg=BACKGROUND)
    b_r.config(bg=BACKGROUND)
    b_s.config(bg=BACKGROUND)
    change_button.config(text=text, bg=BACKGROUND)

    num += 1


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# window.minsize(height=600, width=600)
window.config(padx=50, pady=30, bg=BACKGROUND)
window.title("Pomodoro")

label_t = Label(text="Timer", fg=LIGHT, bg=BACKGROUND, highlightthickness=0, font=(FONT_NAME, 35, "bold"))
label_t.grid(row=0, column=1)
label_t.config(pady=20)


def tick(rep):
    ti = "✔" * rep
    label_c = Label(text=ti, fg=LIGHT, bg=BACKGROUND, highlightthickness=0, font=(FONT_NAME, 35, "bold"))
    label_c.grid(row=3, column=1)


canvas = Canvas(width=300, height=300, bg=BACKGROUND, highlightthickness=0)
photo = PhotoImage(file="new_tomato.png")
photo1 = PhotoImage(file="new_tomato1.png")
c = canvas.create_image(150, 150, image=photo)
timer_text = canvas.create_text(150, 185, fill=TIME, text="25:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


b_s = Button(text="Start", highlightthickness=0, command=start_timer, fg=LIGHT, bg=BACKGROUND)
b_s.grid(row=2, column=0)
change_button = Button(text="☀️", command=change, fg=LIGHT, bg=BACKGROUND, highlightthickness=0)
change_button.grid(row=2, column=1)
b_r = Button(text="Reset", highlightthickness=0, command=reset, fg=LIGHT, bg=BACKGROUND)
b_r.grid(row=2, column=2)

window.mainloop()
