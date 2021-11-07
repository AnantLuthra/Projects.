"""
Author: Anant
Date: 6/11/21
Purpose: Help me getting notified on every relative's birthday or anniversary.
"""

from plyer import notification
import time
import os


def today_date_month():
    full_time = (time.asctime())
    date_month = full_time.split(" ")
    for index, i in enumerate(date_month):
        if index == 1:
            month = i
        if index == 3:
            date1 = i
    return month, date1


def birthday_checker(list):
    month = today_date_month()[0]
    date1 = today_date_month()[1]
    for element in list:
        content = element.split("-")
        if content[0] == month and content[1] == date1:
            t_birthday = content[2]
            return t_birthday
        else:
            pass


def anniversary_checker(list):
    month = today_date_month()[0]
    date1 = today_date_month()[1]
    t_a = False
    for element in list:
        content = element.split("-")
        if content[0] == month and content[1] == date1:
            t_anniversary = content[2]
            return t_anniversary
        else:
            pass


def notification_pusher(string, event, path):
    if event == "Birthday":
        notification.notify(
            title=f"Today is {string}'s birthday",
            message=f"Wish {string} a very happy birthday and give them blessings..",
            app_icon=fr"{path}\birthday_cake.ico",
            timeout=5)

    elif event == "Anniversary":
        couple = string.split("/")
        notification.notify(
            title=f"Today is {couple[0]} and {couple[1]}'s Anniversary.",
            message=f"Wish {couple[0]} and {couple[1]} a very happy Anniversary and give them blessings..",
            app_icon=fr"{path}\heart_valentine.ico",
            timeout=5)


if __name__ == '__main__':
    path = os.getcwd()
    with open("birthday.txt") as f:
        a = f.read()
        birthday_list = a.split("\n")

    with open("anniversary.txt") as f:
        b = f.read()
        anniversary_list = b.split("\n")

    today_birthday = birthday_checker(birthday_list)
    today_anniversar = anniversary_checker(anniversary_list)
    if today_birthday != None:
        today_birthday_list = today_birthday.split("/")
        for i in today_birthday_list:
            notification_pusher(i, "Birthday", path)
            time.sleep(7)
    else:
        pass

    if today_anniversar != None:
        today_anniversay_list = today_anniversar.split("+")
        print(today_anniversay_list)
        for i in today_anniversay_list:
            notification_pusher(i, "Anniversary", path)
            time.sleep(7)
    else:
        pass
