"""
Author: Anant
Date: 6/11/21
Purpose: Help me getting notified on every relative's birthday or anniversary.
"""

from datetime import date
from plyer import notification
import time


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
    pass


def anniversary_checker(list):
    pass


def notification_pusher(string):
    pass


if __name__ == '__main__':
    with open("birthday.txt") as f:
        a = f.read()
        birthday_list = a.split("\n")

    with open("anniversary.txt") as f:
        b = f.read()
        anniversary_list = b.split("\n")

    today_birthday = birthday_checker(birthday_list)
    today_anniversar = anniversary_checker(anniversary_list)
