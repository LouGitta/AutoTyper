import time
import keyboard
from Waiting import wait
def main():

    print(f"What do you want to do ?\n")
    print("1. Spelling out a sentence (letter by letter)")
    print("2. Write a sentence in one time")

    choice = int(input(f"Please choose one of the next proposition !\n"))

    match choice:

        case 1:

            print(f"Do you need to use a duration ?\n")
            print("1. Yes")
            print("2. No")

            choice = int(input(f"Please choose one of the proposition !\n"))

            if choice == 1 :

                print(f"What do you want ?\n")
                print("1. Wait beetween each letter")
                print("2. Write in a limited time")

                choice = int(input(f"Please choose one of the proposition !\n"))

                match choice :

                    case 1: 

                        wait = int(input("How many time i have to write everything ?\nPlease enter the duration in seconds\n"))
                        sentence = str(input(f"Can you give me you're sentence please\n"))

                        wait
                        for letter in sentence :
                            keyboard.press_and_release(letter)
                            time.sleep(wait)

                    case 2:

                        duration = int(input("How many time should i wait between each letter ?\nPlease enter the duration in seconds\n"))
                        sentence = str(input(f"Can you give me you're sentence please\n"))

                        timing = duration/len(sentence)

                        for letter in sentence :
                            keyboard.press_and_release(letter)
                            time.sleep(timing)

            elif choice == 2 :
                sentence = str(input(f"Can you give me you're sentence please\n"))
                for letter in sentence :
                    keyboard.press_and_release(letter)
        case 2:
            sentence = str(input(f"Can you give me you're sentence please\n"))
            keyboard.write(sentence)


if __name__ == '__main__':
    main()