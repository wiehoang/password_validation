# Write an algorithm to justify text. Given a sequence of words
# and an integer line length k, return a list of strings which represents each line, fully justified.
#
# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k.
# Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
#
# If you can only fit one word on a line, then you should pad the right-hand side with spaces.
# Each word is guaranteed not to be longer than k.
#
# For example, given the list of words ["the", "quick", "brown", "fox",
# "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly


#Import libraries
from collections import deque
import re


def justify_word(list_of_words, line_len, word_in_lines, char_in_lines, space_def):
    while len(list_of_words) > 0:
        char_count = 0 # Count a number of characters in one line
        over_char = 0 # Break out while loop, in case number of characters in one line are over line length after looping
        word_in_one_line = []
        while over_char < line_len: # Add word into a list if number of characters in list still smaller than line length
            try:
                char_count += len(list_of_words[0]) + space_def # Increase incrementally, add number of characters of word and 1 default space
                word_in_one_line.append(list_of_words[0])
                list_of_words.popleft() # Remove the word that added into a word_in_one_line list
                over_char = char_count + len(list_of_words[0])
            except IndexError: break # Error happens when popping an element in a blank list_of_words
        char_in_lines.append(char_count - space_def)
        word_in_lines.append(word_in_one_line)
    return char_in_lines, word_in_lines


def justify_space(word_in_lines, char_in_lines, space_def, extra_space, extra_space_remain, line_len):
    for line in range(len(char_in_lines)): # Looping each line in a list of lines
        justify_line = ''
        if char_in_lines[line] != line_len:
            extra_space = space_def + ((line_len - char_in_lines[line]) // (len(word_in_lines[line]) - 1)) # Calculate spaces needed to distribute equally
            extra_space_remain += ((line_len - char_in_lines[line]) % (len(word_in_lines[line]) - 1)) # Calculate leftover spaces after distributing equally
            temp_extra_space_remain = 0 # Duplicated version of extra_space_remain, used for printing result
            for word in range(len(word_in_lines[line]) -1): # Looping each word in one line
                if extra_space_remain > 0: # If a line has leftover spaces
                    word_in_lines[line][word] += ' '*extra_space + ' ' # Distribute both equally and non-equally spaces
                    extra_space_remain -= 1 # Distribute 1 non-equally space in each loop, until this var reach 0
                    temp_extra_space_remain += 1
                else:
                    word_in_lines[line][word] += ' '*extra_space # Distribute only equally spaces

            # Print final justify result
            justify_line = ''.join(word_in_lines[line]) # Merge into string
            if extra_space > 0 and temp_extra_space_remain > 0:
                print(f'{justify_line}, # {extra_space} extra {'space' if extra_space == 1 else 'spaces'} distributed evenly'
                      f' and {temp_extra_space_remain} extra {'space' if temp_extra_space_remain == 1 else 'spaces'} on the left')
            elif extra_space > 0 and temp_extra_space_remain == 0:
                print(f'{justify_line}, # {extra_space} extra {'space' if extra_space == 1 else 'spaces'} distributed evenly')
            elif extra_space == 0 and temp_extra_space_remain > 0:
                print(f'{justify_line}, # {temp_extra_space_remain} extra {'space' if temp_extra_space_remain == 1 else 'spaces'} on the left')
            else:
                print(f'{justify_line}, No extra spaces needed')
    return word_in_lines


def justify_text():
    # Initialize vars
    word_in_lines = [] # Store a list of lines, each line stores a list of words
    char_in_lines = [] # Store a list of characters count in each line (space default included)
    space_def = 1 # Default number of space between 2 words (1 is normally in real life)
    extra_space = 0 # Spaces that can distributed equally
    extra_space_remain = 0 # Spaces remain after distributing equally

    # Input & validate line length
    line_len = input('Enter length for each line: ') # Length for each line
    while re.search('[^0-9]', line_len): # Print error and input again if it is not an integer
        print('Please only enter an integer')
        line_len = input('Enter length for each line: ')
    line_len = int(line_len) # Convert into an integer

    # Input & validate words
    word_valid = 0
    while word_valid == 0: # Loop until len of all words inputted are shorter than line length
        words = input('Enter words seperated by space: ')  # String of words
        if all(len(word) < line_len for word in words):
            word_valid += 1

    # Convert into a queue
    list_of_words = deque(words.split(' '))

    # Justify word
    justify_word(list_of_words, line_len, word_in_lines, char_in_lines, space_def)

    # Justify space
    justify_space(word_in_lines, char_in_lines, space_def, extra_space, extra_space_remain, line_len)

justify_text()
