#Guess The Number Game in Python
import random
logo=''' _______           _______  _______  _______       _________          _______        _                 _______  ______   _______  _______
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \      \__   __/|\     /|(  ____ \      ( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )
| (    \/| )   ( || (    \/| (    \/| (    \/         ) (   | )   ( || (    \/      |  \  ( || )   ( || () () || (   ) )| (    \/| (    )|
| |      | |   | || (__    | (_____ | (_____          | |   | (___) || (__          |   \ | || |   | || || || || (__/ / | (__    | (____)|
| | ____ | |   | ||  __)   (_____  )(_____  )         | |   |  ___  ||  __)         | (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)
| | \_  )| |   | || (            ) |      ) |         | |   | (   ) || (            | | \   || |   | || |   | || (  \ \ | (      | (\ (   
| (___) || (___) || (____/\/\____) |/\____) |         | |   | )   ( || (____/\      | )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__
(_______)(_______)(_______/\_______)\_______)         )_(   |/     \|(_______/      |/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/'''

print(logo)

EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5

def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen=='hard:
        return HARD_LEVEL_ATTEMPTS
   else:
        return

def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low.")
        return attempts-1
    elif guessed_number>answer:
        print("Your guess is too high.")
        return attempts-1
    else:
        print(f"Your guess is right... The answer was {answer}")

def game():
    print("Let me think of a number between 1 to 50.")
    answer=random.randint(1,50)
    level=input("Choose level of difficulty...Type 'easy' or 'hard': ").lower()
    attempts=set_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("You have entered wrong difficulty level...Play again!")
        return

    guessed_number=0
    while guessed_number!=answer:
        print(f"You have {attempts} remaining to guess the number.")
        guessed_number=int(input("Guess a number:"))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("You are out of guesses...You loose!")
            return
        elif guessed_number!=answer:
            print("Guess Again.")

game()
