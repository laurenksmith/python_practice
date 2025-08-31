# Number Guessing Game

import random


"""
1. Random number in a range
2. Capture guess
3. Evaluate user guess

command line game prodice user messages
Linear
while loop - boolean argument of true

"""

game_random_number = random.randint(1, 100)
game_active = True

while game_active:
    print("Guess a number between 1 - 100.")
    user_guess = int(input())  # Expected a string - add int before input so that it casts string to integer
    if user_guess == game_random_number:
        print("Woohoo! You guessed correctly!")
        game_active = False
    elif user_guess < game_random_number:
        print("Too low, guess again.")
    else:
        print("Too high, guess again.")

