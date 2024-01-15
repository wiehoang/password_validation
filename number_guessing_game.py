# Import libraries
import random

def user_input():
    global guess
    guess = int(input('Enter your guess: '))
    # Handle invalid inputs
    if guess not in range(min_guess, max_guess): # Out of min-max range
        print('Please only guess numbers are between 1 to 100')
        user_input()
    elif guess in guess_history.keys(): # Duplicated guess
        print('You already guessed this number. Try guessing a new number in suggested range')
        user_input()
    elif guess not in range(*sorted((last_guess, range_num))): # Out of suggested range
        if last_guess == 0 or range_num == 0: pass
        else:
            print('Please only guess numbers that in suggested range')
            user_input()

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
    global randnum, min_guess, max_guess, last_guess, guess_history, range_num
    min_guess, max_guess = 1, 100 # Min and max number for guessing
    last_guess = 0 # Var for "Out of suggested range" condition in user_input function
    guess_history = {} # Store all of previous guesses by pair template: key (guesse number), value (absolute difference between guesse and random number)
    range_num = 0 # A number for range suggested
    attemp = 0 # Guessing times, increase 1 everytime guess number != random number

    # Generate random number
    randnum = random.randint(min_guess, max_guess)
    print('randnum:', randnum)

    # Welcome message
    print('Welcome to the Number Guessing Game! \nI have selected a random number between 1 and 100. \nTry to guess what it is!')

    # User guess
    user_input()

    while guess != randnum:
    # Determine an appropriate range
        sorted_guess_history = dict(sorted(guess_history.items(), key=lambda x: x[1]))
        for key, value in sorted_guess_history.items(): # Loop from the smallest abs value
            if randnum in range(*sorted((guess, key))):
                range_num = key
                break
        if range_num == 0: # Handle when guess_history is blank or no value meets the loop condition above
            range_num = min_guess if randnum in range(*sorted((guess, min_guess))) else max_guess

    # Determine a message for each ranges
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
        last_guess = guess
        guess_history[guess] = abs(randnum - guess) # Create a new pair {key:value} in guess_history
        attemp += 1
        user_input() # Guess again if guess != random number
    print(f'Correct! You guessed the number {randnum} in {attemp + 1} tries.') # Correct guess message

    # Restart game option
    restart_game()

start_game()
