# In a certain encrypted message which has information about the location(area, city),
# the characters are jumbled such that first character of the first word is followed by the first character of the second word,
# then it is followed by second character of the first word and so on In other words, let’s say the location is bandra,mumbai
# The encrypted message says ‘bmaunmdbraai’.

# Import libraries
import re


def validate_location(location):
    while re.search(',', location) == None: # Input must contain ',' between area & city
        location = input('Enter location by area, city: ')
    return location


def jumbled_location():
    jumbled_lst = [] # A list of jumbled characters
    location = input('Enter location by area, city: ')
    validate_location(location)

    # Format validated location
    val_location = location.lower()
    area = val_location.split(',')[0].replace(' ', '')
    city = val_location.split(',')[1].replace(' ', '')

    # Jumble validated location
    if len(area) == len(city):
        for char in range(len(area)): # Add chars of area & city into 1 list respectively
            jumbled_lst.append(area[char])
            jumbled_lst.append(city[char])
        print(''.join(jumbled_lst))
    else: # If num of chars in area != city, jumble chars equally then add remain chars
        shorter_word = area if len(area) < len(city) else city
        longer_word = area if len(area) > len(city) else city
        for char in range(len(shorter_word)):
            jumbled_lst.append(area[char])
            jumbled_lst.append(city[char])
        print(''.join(jumbled_lst) + longer_word[len(shorter_word):])


jumbled_location()
