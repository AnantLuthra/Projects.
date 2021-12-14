"""
Author: Anant
Date: 6/11/21
Purpose: Help me getting notified on every relative's birthday or anniversary.
"""

from plyer import notification
from datetime import datetime
import os, time


def today_date_month():
    """
    Function to get today's date and month for checking our text file..
    """
    d = datetime.now()
    only_date = str(d.date())
    datetime_list = only_date.split("-")
    month = datetime_list[1]
    date1 = datetime_list[2]
    return month, date1
    
    
def birthday_checker(list):
    """
    This function check today's birthday..
    """
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
    """
    This function check today anniversary..
    """
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
    """
    This fucntion will push notification as today's occassion.. 
    """
    if event == "Birthday":
        notification.notify(
            title=f"Today is {string}'s birthday",
            message=f"Wish {string} a very happy birthday and give them blessings..",
            app_icon=fr"{path}\birthday_cake.ico",
            timeout=12)

    elif event == "Anniversary":
        couple = string.split("/")
        notification.notify(
            title=f"Today is {couple[0]} and {couple[1]}'s Anniversary.",
            message=f"Wish {couple[0]} and {couple[1]} a very happy Anniversary and give them blessings..",
            app_icon=fr"{path}\heart_valentine.ico",
            timeout=12)


if __name__ == '__main__':
    path = os.getcwd() # getting present directory where our text file's our present..
    with open("birthday.txt") as f: # getting data from birthday.txt..
        a = f.read()
        birthday_list = a.split("\n")

    with open("anniversary.txt") as f: # getting data from anniversay.txt..
        b = f.read()
        anniversary_list = b.split("\n")

    today_birthday = birthday_checker(birthday_list)
    today_anniversar = anniversary_checker(anniversary_list)
    
    # Sending today's birthday for notification..
    if today_birthday != None:
        today_birthday_list = today_birthday.split("/")
        for i in today_birthday_list:
            notification_pusher(i, "Birthday", path)
            time.sleep(10)
    else:
        pass
    
    # sending today's aniversary for notification...
    if today_anniversar != None:
        today_anniversay_list = today_anniversar.split("+")
        for i in today_anniversay_list:
            notification_pusher(i, "Anniversary", path)
            time.sleep(10)
    else:
        pass
