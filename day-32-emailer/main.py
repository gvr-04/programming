from random import choice
import smtplib
import pandas
import datetime as dt

today = dt.datetime.now().today()
date = str(today.month) + "-" + str(today.day)
b_day = pandas.read_csv('birthdays.csv').to_dict()
dates = [str(b_day["month"][i]) + "-" + str(b_day["day"][i]) for i in b_day["name"]]
file = choice(["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"])

if date in dates:
    name = b_day["name"][dates.index(date)]
    mail = b_day["email"][dates.index(date)]
    with open(file, "r") as f:
        txt = f.read()
    message = txt.replace("[NAME]", name)
    email = ""
    password = ""
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=mail, msg=f"Subject:Happy Birthday!!!\n\n{message}")
    connection.close()
