import time
import keyboard

while True:
    duration = int(input("combien de temps en minutes? :"))
    while duration >= 0:
        duration -= 1
        keyboard.press_and_release("a")
        keyboard.press_and_release("enter")
        time.sleep(60)