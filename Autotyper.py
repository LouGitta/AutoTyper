import time
import keyboard

while True:
    duration = int(input("How many time should i wait (minutes) ? : "))
    while duration >= 0:
        duration -= 1
        keyboard.press_and_release("a")
        keyboard.press_and_release("enter")
        time.sleep(60)





