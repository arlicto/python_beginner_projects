print(r'''
 _____ _     _____ ____  ____    _____ _     _____   _      _     _      ____  _____ ____ 
/  __// \ /\/  __// ___\/ ___\  /__ __Y \ /|/  __/  / \  /|/ \ /\/ \__/|/  __\/  __//  __\
| |  _| | |||  \  |    \|    \    / \ | |_|||  \    | |\ ||| | ||| |\/||| | //|  \  |  \/|
| |_//| \_/||  /_ \___ |\___ |    | | | | |||  /_   | | \||| \_/|| |  ||| |_\\|  /_ |    /
\____\\____/\____\\____/\____/    \_/ \_/ \|\____\  \_/  \|\____/\_/  \|\____/\____\\_/\_\
                                                                                          ''')
print("\nWelcome to the Number guessing game. Are you ready to test your intuition?")

import random

# random number





#guessing logic easy
def easy():
    print("You have 10 guesses.")
    guess = int(input("Make a guess: "))
    lives = 10
    while lives > 1:
        if guess < rd_number:
            lives -= 1
            print(f"Too low. You have {lives} guess left.")        
            guess = int(input("Guess again: "))
        elif guess > rd_number:
            lives -= 1
            print(f"Too high. You have {lives} guess left.")
            guess = int(input("Guess again: "))
        else:
            print(f"You got it. {rd_number} was the number.")
            break

    if lives == 1:
        print(f"You lost. It was {rd_number}")


# hard logic 
def hard():
    print("You have 5 guesses.")
    guess = int(input("Make a guess: "))
    lives = 5
    while lives > 1:
        if guess < rd_number:
            lives -= 1
            print(f"Too low. You have {lives} guess left.")        
            guess = int(input("Guess again: "))
        elif guess > rd_number:
            lives -= 1
            print(f"Too high. You have {lives} guess left.")
            guess = int(input("Guess again: "))
        else:
            print(f"You got it. {rd_number} was the number.")
            break

    if lives == 1:
        print(f"You lost. It was {rd_number}")




rd_number = random.randint(2, 99)

print("\nYou have 10 attempts to guess the number.\nIt's between 1 and 100.")
easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if easy_or_hard == "easy":
    easy()
else:
    hard()