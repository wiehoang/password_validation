# In the context of a major sporting event upcoming in Hanoi city, attracting numerous visitors, you - as the manager of a hotel
# need to develop a program to manage room bookings.
# This program should include the following functionalities:
# Room Booking Entry: This feature should allow users to input booking requests, including the guest's name, check-in time, and check-out time.
# Note that these booking times may overlap with other requests.
# Display Booking List: This function will show a list of all booking requests that have been entered, including guest names, check-in and check-out times.
# Calculate Minimum Number of Rooms Required: Based on the list of booking requests, the program should calculate
# and return the minimum number of rooms required to accommodate all the requests without having to deny any guests due to a shortage of rooms.

# Import libraries
import re
import pandas as pd
from datetime import datetime

def validate_form(form):
    for key in form.keys():
        valid = 0 # Var to break out while loop
        while valid == 0: # Loop through each inputted info, add that info into booking form if it is valid
            value = input(f'{key}: ')
            match key:
                case 'guest_name':
                    if re.search('[^A-Za-z]', value) == None: # Name can only contains alphabetic character
                        form['guest_name'] = value.title()
                        valid += 1
                    else:
                        print('Please input a valid name format')
                case 'guest_checkin':
                    try:
                        if datetime.strptime(value, '%d-%m-%Y') >= datetime.today(): # Validate date format & check-in time must be after today
                            form['guest_checkin'] = value
                            valid += 1
                        else:
                            print('Check-in time must be after today date!')
                    except ValueError:
                        print('Please input a valid check-in time format (dd-mm-yyyy)')
                case 'guest_checkout':
                    try:
                        if datetime.strptime(value, '%d-%m-%Y') > datetime.strptime(form['guest_checkin'], '%d-%m-%Y'): # Validate date format & check-out time must be after check-in time
                            form['guest_checkout'] = value
                            valid += 1
                        else:
                            print('Check-out time must be after check-in time!')
                    except ValueError:
                        print('Please input a valid check-out time format (dd-mm-yyyy)')

def create_new_booking(booking_lst):
    form = {
        'guest_name': '',
        'guest_checkin': '',
        'guest_checkout': ''
        } # Create a form template
    validate_form(form) # Validate guess infos
    booking_lst.append(form) # Add a new booking to booking database
    print('Booking added successfully!')
    return booking_lst

def create_other_booking(booking_lst): # Ask if user want to create other bookings
    create_other_booking = ''
    while create_other_booking != '0' or create_other_booking != '1':
        create_other_booking = input('Do you want to add another booking? (Type 1 to add another booking, type 0 to go back to main menu): ')
        match create_other_booking:
            case '1':
                create_new_booking(booking_lst)
            case '0':
                break
            case _:
                print('Invalid input. Please try again.')

def view_booking(booking_lst):
    if booking_lst == []: # If no booking exists
        print('No booking exists')
        create_booking = ''
        while create_booking != '0' or create_booking != '1':
            create_booking = input('Do you want to create a booking? (Type 1 to create a booking, type 0 to go back to main menu): ')
            match create_booking:
                case '1':
                    create_new_booking(booking_lst)
                case '0':
                    break
                case _:
                    print('Invalid input. Please try again.')
    else: # View all bookings if exist
        print(pd.DataFrame(booking_lst))
        back_to_main_menu = '' # Back to the main menu option
        while back_to_main_menu != '0':
            back_to_main_menu = input('Type 0 to go back to main menu: ')
            if back_to_main_menu == '0':
                break
            else:
                print('Invalid input. Please try again.')

def min_room_required(booking_lst):
    checkin_times, checkout_times = [], []
    room = 1 # Need at least 2 bookings to use this calculator, so 1 is default
    j = 0 # Var for iterating check-out time
    in_less_than_out = 0 # Number of times check-in time < check-out time

    # Add check-in & check-out times into each check-in & check-out lists
    for dict in range(len(booking_lst)):
        checkin_times.append(booking_lst[dict]['guest_checkin'])
        checkout_times.append(booking_lst[dict]['guest_checkout'])

    # Calculating number of rooms
    for i in range(len(checkin_times)):
        if checkin_times[i] < checkout_times[j]: # Iterate to a next check-in time if current check-in time < current check-out time
            in_less_than_out += 1
            if in_less_than_out >= 2: # Need 1 more room if check-time time < check-out time happens 2 consecutive times
                room += 1             # Every booking has check-in & check-out time, 1st time will compare its own current check-in & check-out time, 2nd time will compare next check-in with current check-out time
        else:
            j += 1 # Iterate to a next check-out time if current check-in time > current check-out time
            in_less_than_out = 0 # Reset number of times check-in time < check-out time
            if checkin_times[i] < checkout_times[j]: # Compare current check-in time with next check-out time
                in_less_than_out += 1
    return print(f'Minimum number of rooms required to accommodate all the requests is {room}')

def hotel_room_booking_management():
    # Initialize vars
    booking_lst = []

    # Welcome message
    print('''
    ========================================
	WELCOME TO HOTEL ROOM BOOKING MANAGEMENT
	========================================
	1. Create Booking
	2. View Booking
	3. Minimum Room Required Calculator
	4. Exit
	''')

    # User input
    action = '0'
    while action != '4':
        action = input('Choose 1 to create contact, 2 to view contact, 3 to use minimum room required calculator, 4 to exit: ')
        match action:
            case '1':
                create_new_booking(booking_lst)
                create_other_booking(booking_lst)
            case '2':
                view_booking(booking_lst)
            case '3':
                if len(booking_lst) >= 2:  # Check if hotel has more than 2 bookings
                    min_room_required(booking_lst)
                else:
                    print('Hotel needs at least 2 bookings to use this calculator!')
            case _:
                print('Please only choose numbers from 1 to 4')
    print('Thanks for using!')

hotel_room_booking_management()
