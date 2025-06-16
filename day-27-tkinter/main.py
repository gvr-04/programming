from tkinter import *


def buttoned():
    number = round(int(inp.get()) * 1.609)
    km.config(text=number)


# window
window = Tk()
window.title("hello")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

# km
km = Label(text="0", font=("C059", 15))
km.grid(row=1, column=1)
# miles str
miles = Label(text="miles", font=("C059", 15))
miles.grid(row=0, column=2)
# equal str
miles = Label(text="is equal to ", font=("C059", 15))
miles.grid(row=1, column=0)
# km str
miles = Label(text="km", font=("C059", 15))
miles.grid(row=1, column=2)

# input
inp = Entry(width=8)
inp.insert(END, string="0")
inp.grid(row=0, column=1)

# button
button = Button(text="calculate", command=buttoned)
button.grid(row=2, column=1)

window.mainloop()
