import time
from functools import lru_cache
from plyer import notification
from playsound import playsound


@lru_cache(maxsize=5)
def nacho(n):
    time.sleep(n)
    return n


# if __name__ == '__main__':
#     print("Ek run ho hai")
#     print(nacho(3))

def water_drinker():
    print("This Water notification system.")
    while True:
        time.sleep(15)
        notification.notify(
                title="** It's water time **",
                message="Drink 1 glass of water from your bottle.... And enjoy programming...",
                app_icon="C:\\Users\\star\\PycharmProjects\\practicepython\\Iconsmind-Outline-Glass-Water.ico",
                timeout=10)


def physical():
    time.sleep(4)
    print("It's physical exercise time..")
    playsound('D:\\game sounds\\physical.mp3')
    notification.notify(
                title="** It's exercise time **",
                message="Get up from your chair and do some PT.... And enjoy programming...",
                app_icon="C:\\Users\\star\\PycharmProjects\\practicepython\\Icons8-Ios7-Sports-Running.ico",
                timeout=12)


