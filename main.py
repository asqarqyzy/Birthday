import smtplib
import datetime as dt
from random import choice


today = dt.datetime.now()
weekday = today.weekday()
my_email = "nurlybayevaassel@gmail.com"
password = 'fymk ljna lyaj xsul'
with open("quotes.txt") as file:
    quotes = [i.replace('"', "").replace("\n", "") for i in file.readlines()]


if weekday == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='asqarqyzy_a@mail.ru ',
                            msg=f"Subject:Today's quote for u\n\n{choice(quotes)}")
        print("Right")






