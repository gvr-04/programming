import json.decoder
from tkinter import *
from tkinter import messagebox
from json import dump, load
from random import randint, choice, shuffle
import pyperclip


# logic
def search():
    try:
        with open('data.json', 'r') as file_data:
            web = web_inp.get()
            data = load(file_data)[web]["password"]
    except (KeyError, json.decoder.JSONDecodeError, FileNotFoundError):
        messagebox.showerror("Error", "No password found for this website")
    else:
        password_inp.delete(0, END)
        messagebox.showinfo(web, f'Email: {email_inp.get()}\nPassword: {data}')
        pyperclip.copy(data)


def gen_b():
    password_inp.delete(0, END)
    password_inp.insert(END, gen_pass())


def add_b():
    lst = [web_inp.get(), email_inp.get(), password_inp.get()]
    dis = "\n".join(lst)
    dic = {lst[0]: {"email": lst[1], "password": lst[2]}}
    if "" in lst:
        messagebox.showinfo(title="Oops", message="Leave no empty blanks...\n空白を残さないでください...")
    else:
        ye = messagebox.askokcancel(title=web_inp.get(), message=f"Are You Sure About The Following?\n\n{dis}")
        if ye:
            try:
                with open("data.json", "r") as data_file:
                    data = load(data_file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", "w") as data_file:
                    dump(dic, data_file, indent=4)
            else:
                data.update(dic)
                with open("data.json", "w") as data_file:
                    dump(data, data_file, indent=4)
            finally:
                web_inp.delete(0, END)
                password_inp.delete(0, END)


def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)
    password_letter = [choice(letters) for _ in range(nr_letters)]
    password_symbol = [choice(symbols) for _ in range(nr_symbols)]
    password_number = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)
    new_password = "".join(password_list)
    pyperclip.copy(new_password)
    return new_password


# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#FFFFFF")

# image
canvas = Canvas(width=200, height=220, bg="#FFFFFF", highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# website
website = Label(text="Website:", highlightthickness=0, bg="#FFFFFF")
website.grid(row=1, column=0)
web_inp = Entry(width=24, highlightthickness=0)
web_inp.focus()
web_inp.grid(row=1, column=1)
search_button = Button(text="Search", highlightthickness=0, command=search, width=7)
search_button.grid(row=1, column=2)

# email
email = Label(text="Email/Username:    ", highlightthickness=0, bg="#FFFFFF")
email.grid(row=2, column=0)
email_inp = Entry(width=35, highlightthickness=0)
email_inp.insert(END, "hahaa.v8@gmail.com")
email_inp.grid(row=2, column=1, columnspan=2)

# pass
password = Label(text="Password:", highlightthickness=0, bg="#FFFFFF")
password.grid(row=3, column=0)
password_inp = Entry(width=24, highlightthickness=0)
password_inp.grid(row=3, column=1)
gen_button = Button(text="Gen Pass", command=gen_b, highlightthickness=0)
gen_button.grid(row=3, column=2)

# add
add_button = Button(text="Add", command=add_b, width=32, highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
