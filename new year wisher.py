from win32com.client import Dispatch

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

if __name__ == '__main__':
    with open("new year in different languages.txt") as f:
        data = f.read()
        diff_language = data.split("\n")
    
    for i in diff_language:
        language = i.split("-")
        speak(f"{language[0]} {language[1]}")