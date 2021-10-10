from win32com.client import Dispatch
speak=Dispatch("SAPI.SpVoice")
import random
list = ["Anamika", "Ananya", "Aradhya", "Khushi", "Devyanshi", "Nishaa"]
def truth_teller(name, gender):
    if gender == "m":
        girl = random.choice(list)
        speak.Speak(f"{name} I know what is the name of your crush, is her name is {girl}")
        opinion = input("Press 1 for yes and 2 for no: ")
        if opinion == '1':
            speak.Speak(f"I knew that I am a good assistant so that's why...")
        else:
            speak.Speak(f"But I know that you are telling a lie... and you feel something about her...")
    elif gender == "f":
        speak.Speak(f"{name} Do you know I am feeling something for you, amm... I love you {name} Do you love me too?")
        opinion = input("Press 1 for yes and 2 for no: ")
        if opinion == '1':
            speak.Speak(f"I know you will not deny my love {name}")
        else:
            girl = random.choice(list)
            speak.Speak(f"I knew that you will deny my love ...so I have already said I love you to someone else and her name is {girl}")


speak.Speak("Enter your name")
name = input("Enter your name.\n")
speak.Speak("Are you a male or female?")
gender = input("For male enter 'm' and for female enter 'f'\n")

truth_teller(name, gender)
