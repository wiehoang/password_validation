# Import libraries
import random

def user_guess():
    global guess
    guess = int(input('Enter your guess: '))
    if guess not in range(min_guess, max_guess):
        print('Please only guess numbers are between 1 to 100')
        user_guess()

def restart_game():
    restart = input('Do you want to play again? (yes/no): ')
    if restart == 'yes' or restart == 'y':
        start_game()
    elif restart == 'no' or restart == 'n':
        print('Thanks for playing!')
    else:
        print('Please only choose yes(y) or no(n)')
        restart_game()
def start_game():
    # Initialize vars
    global min_guess, max_guess
    min_guess, max_guess = 1, 100
    last_guess, sec_last_guess = 1, 1 # min_guess is 1 so 1 is default number
    range_num = 0
    attemp = 0

    # Generate random number
    randnum = random.randint(min_guess, max_guess + 1)
    print('randnum: ',randnum)

    # Welcome message
    print('Welcome to the Number Guessing Game! \nI have selected a random number between 1 and 100. \nTry to guess what it is!')

    # User guess
    user_guess()

    while guess != randnum:
        # Determine an appropriate range for hints by calculating the difference between a random number and other variables
        diff_num = {sec_last_guess: abs(randnum - sec_last_guess), last_guess: abs(randnum - last_guess),
                    min_guess: abs(randnum - min_guess), max_guess: abs(randnum - max_guess)}
        sorted_diff_num = dict(sorted(diff_num.items(), key=lambda x: x[1]))
        for key, value in sorted_diff_num.items():
            if randnum in range(*sorted((guess, key))):
                range_num = key
                break

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
        user_guess()
    print(f'Correct! You guessed the number {randnum} in {attemp} tries.')

    # Restart game option
    restart_game()

start_game()
