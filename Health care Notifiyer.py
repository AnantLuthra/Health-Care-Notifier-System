import time
from playsound import playsound
from plyer import notification


def water():
    time.sleep(60*30)
    print("It's water time..")
    playsound('D:\\game sounds\\water.mp3')
    notification.notify(
                title="** It's water time **",
                message="Drink 1 glass of water from your bottle.... And enjoy programming...",
                app_icon="C:\\Users\\star\\PycharmProjects\\practicepython\\Water.ico",
                timeout=12)


def eyes():
    time.sleep(60*5)
    print("It's eyes exercise time..")
    playsound('D:\\game sounds\\eyes.mp3')
    notification.notify(
                title="** It's eye's exercise time **",
                message="Look 20 Feet's away for next 20 seconds from now... And enjoy programming...",
                app_icon="C:\\Users\\star\\PycharmProjects\\practicepython\\Eye Exersice.ico",
                timeout=12)


def physical():
    time.sleep(60*3)
    print("It's physical exercise time..")
    playsound('D:\\game sounds\\physical.mp3')
    notification.notify(
                title="** It's exercise time **",
                message="Get up from your chair and do some PT.... And enjoy programming...",
                app_icon="C:\\Users\\star\\PycharmProjects\\practicepython\\Exersice.ico",
                timeout=12)


if __name__ == '__main__':
    print("Welcome to Health care management...")
    while True:
        water()
        eyes()
        physical()
