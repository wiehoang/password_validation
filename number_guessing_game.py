# Import libraries
import random

def start_game():
    # Initialize vars
    min_guess, max_guess = 1, 100
    attemp = 0
    last_guess, sec_last_guess = 0, 0

    # Generate random number
    randnum = random.randint(min_guess, max_guess+1)

    # Welcome message
    print('Welcome to the Number Guessing Game! \nI have selected a random number between 1 and 100. \nTry to guess what it is!')

    guess = int(input('Enter your guess: '))
    while guess != randnum:
        # Determine an approriate range for hints by calculating the difference between a random number and other variables
        diff_num = {sec_last_guess: abs(randnum - sec_last_guess),last_guess: abs(randnum - last_guess),
                    min_guess: abs(randnum - min_guess), max_guess: abs(randnum - max_guess)}
        for key, value in diff_num.items():
            if value == min(diff_num.values()):
                range_num = key
        # Determine a message for each condition
        if guess < randnum:
            if guess < range_num:
                print(f'Your number is lower than the number I picked. It ranges between {guess} and {range_num}.')
            elif guess > range_num:
                print(f'Your number is lower than the number I picked. It ranges between {range_num} and {guess}.')
        elif guess > randnum:
            if guess < range_num:
                print(f'Your number is higher than the number I picked. It ranges between {guess} and {range_num}.')
            elif guess > range_num:
                print(f'Your number is higher than the number I picked. It ranges between {range_num} and {guess}.')
        sec_last_guess = last_guess
        last_guess = guess
        attemp += 1
        guess = int(input('Enter your guess: '))
    print(f'Correct! You guessed the number {randnum} in {attemp} tries.')

    # Restart game option
    restart = input('Do you want to play again? (yes/no): ')
    if restart == 'yes' or restart == 'y':
        start_game()
    elif restart == 'no' or restart == 'n':
        print('Thanks for playing!')

start_game()
