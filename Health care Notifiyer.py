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
    speak("Putting your laptop on sleep.., because I cares about your health so much....")
    pyautogui.hotkey('win', 'd')
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    pyautogui.press('left')
    time.sleep(1)
    pyautogui.press("enter")

def water(path):
    time.sleep(60*20)
    speak("It's water time..")
    notification.notify(
                title="** It's water time **",
                message="Drink 1 glass of water from your bottle.... And enjoy programming...",
                app_icon=fr"{path}\Water.ico",
                timeout=12)
    put_on_sleep("First drink 1 glass of water and then come back..")

def eyes(path):
    time.sleep(60*5)
    speak("It's eyes exercise time..")
    notification.notify(
                title="** It's eye's exercise time **",
                message="Look 20 Feet's away for next 20 seconds from now... And enjoy programming...",
                app_icon=fr"{path}\Eye Exersice.ico",
                timeout=12)
    put_on_sleep("First do eyes exercise and then come back..")

def physical(path):
    time.sleep(60*5)
    speak("It's physical exercise time..")
    notification.notify(
                title="** It's exercise time **",
                message="Get up from your chair and do some PT.... And enjoy programming...",
                app_icon=fr"{path}\Exersice.ico",
                timeout=12)
    put_on_sleep("First do some physical activity and then come back..")

if __name__ == '__main__':
    pyautogui.hotkey('win', 'd')
    print("Welcome to Health care management...")
    path = os.getcwd()
    while True:
        water(path)
        eyes(path)
        physical(path)
