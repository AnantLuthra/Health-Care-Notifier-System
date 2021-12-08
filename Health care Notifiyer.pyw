import time
from plyer import notification
import pyautogui
import os

def speak(str):
    '''
    Function for speaking of program.
    '''
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

def put_on_sleep(str):
    speak(str)
    pyautogui.hotkey('win', 'd')

def water(path):
    time.sleep(60*20)
    speak("It's water time..")
    put_on_sleep("Drink 1 glass of water..")
    notification.notify(
                title="** It's water time **",
                message="Drink 1 glass of water from your bottle.... And enjoy programming...",
                app_icon=fr"{path}\Water.ico",
                timeout=12)

def eyes(path):
    time.sleep(60*8)
    put_on_sleep("Do eyes exercise.")
    notification.notify(
                title="** It's eye's exercise time **",
                message="Look 20 Feet's away for next 20 seconds from now... And enjoy programming...",
                app_icon=fr"{path}\Eye Exersice.ico",
                timeout=12)

def physical(path):
    time.sleep(60*8)
    speak("Get up from you chair and go for a walk.")
    notification.notify(
                title="** It's exercise time **",
                message="Get up from your chair and do some PT.... And enjoy programming...",
                app_icon=fr"{path}\Exersice.ico",
                timeout=12)

if __name__ == '__main__':
    print("Welcome to Health care management...")
    path = os.getcwd()
    while True:
        water(path)
        eyes(path)
        physical(path)
