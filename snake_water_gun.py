# 1="Snake"
# 3="Gun"
# 2="Water"
# RandomNum=random.randint(1,3)
# print(RandomNum)
import random
from playsound import playsound
cpoints = 0
upoints = 0
print("Welcome to my game , read instructions carefully and enjoy the game :))")
print("Choose from the following each time.. \nS:- For Snake\nW:- For Water\nG:- For Gun")
print("Remember to write your choise in Capital each time otherwise your choice will not be taken by the computer")
for i in range(10):
    objects = ["Snake", "Water", "Gun"]
    computer = random.choice(objects)
    user = input("Now enter your choice: ")
    if user == "S" and computer == "Snake":
        print("Same choice", "\t\t\t\t\t\tYou=", upoints, ",Computer=", cpoints)
        playsound('D:\\game sounds\\same choice1.mp3')
    elif user == "S" and computer == "Water":
        upoints+=1
        print("Results\nYou-Snake", "Computer-", computer,"\t\t\t\tYou=",upoints,",Computer=",cpoints)
        playsound('D:\\game sounds\\u get point.mp3')
    elif user == "S" and computer == "Gun":
        cpoints += 1
        print("Results\nYou-Snake", "Computer-", computer, "\t\t\t\tYou=",upoints,",Computer=",cpoints)
        playsound('D:\\game sounds\\C get point.mp3')
    elif user == "W" and computer == "Snake":
        cpoints += 1
        print("Results\nYou-Water", "Computer-", computer, "\t\t\t\tYou=", upoints, ",Computer=", cpoints)
        playsound('D:\\game sounds\\C get point.mp3')
    elif user == "W" and computer == "Water":
        print("Same choice", "\t\t\t\t\t\tYou=", upoints, ",Computer=", cpoints)
        playsound('D:\\game sounds\\same choice1.mp3')
    elif user == "W" and computer == "Gun":
        upoints+=1
        print("Results\nYou-Water", "Computer-", computer, "\t\t\t\tYou=", upoints, ",Computer=", cpoints)
        playsound('D:\\game sounds\\u get point.mp3')
    elif user == "G" and computer == "Snake":
        upoints+=1
        print("Results\nYou-Gun", "Computer-", computer, "\t\t\t\tYou=", upoints, ",Computer=", cpoints)
        playsound('D:\\game sounds\\u get point.mp3')
    elif user == "G" and computer == "Water":
        cpoints+=1
        print("Results\nYou-Gun", "Computer-", computer, "\t\t\t\tYou=", upoints, ",Computer=", cpoints)
        playsound('D:\\game sounds\\C get point.mp3')
    elif user == "G" and computer == "Gun":
        print("Same choice", "\t\t\t\t\t\tYou=", upoints, ",Computer=", cpoints)
        playsound('D:\\game sounds\\same choice1.mp3')
    else:
        print("Invalid input !!! Enter S or W or G")
print("Final Results","You=", upoints, ",Computer=", cpoints)
if upoints<cpoints:
    print("Computer Wins !!! Better luck next time")
    playsound('D:\\game sounds\\You lose sound.mp3')
elif upoints>cpoints:
    print("You Won the match!!! Congratulations !!!")
    playsound('D:\\game sounds\\Kids Cheering.mp3')
else:
    print("Match draw !! Your played very well...")
    playsound('D:\\game sounds\\match draw.mp3')

# from playsound import playsound
# playsound('D:\\d data\\tunes 3\\Jarico - Landscape [NCS BEST OF].mp3')

# import math
# import datetime
# print(datetime.datetime.now())
# print(math.sin(30))
