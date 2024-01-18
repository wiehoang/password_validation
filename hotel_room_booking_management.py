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
from datetime import datetime

def create_booking():
    # Validating guest's name
    while True:
        temp_booking = []
        guest_name = input('Name: ')
        if re.search('[^A-Za-z]', guest_name) == None: # Name can only contains alphabetic character
            valid_guess_name = guest_name.title()
            temp_booking.append(valid_guess_name)
            break
        else:
            print('Please input a valid name format')

    # Validating guest's check-in time
    while True:
        guest_checkin = input('Check-in time (dd/mm/yyyy): ')
        try:
            if datetime.strptime(guest_checkin, '%d/%m/%Y'): # Check date format
                temp_booking.append(guest_checkin)
                break
        except ValueError:
            print('Please input a valid check-in time format (dd/mm/yyyy)')

    # Validating guest's check-out time
    while True:
        guest_checkout = input('Check-out time (dd/mm/yyyy): ')
        try:
            if datetime.strptime(guest_checkout, '%d/%m/%Y'):
                temp_booking.append(guest_checkout)
                break
        except ValueError:
            print('Please input a valid check-out time format (dd/mm/yyyy)')

    booking_lst.append(temp_booking) # Add new booking to booking database
    print('Booking added successfully!')

    # Ask if user want to create other bookings
    create_other_booking = input('Do you want to add another booking? (Type 1 to add another booking, type 0 to go back to main menu): ')
    while True:
        if create_other_booking == '1':
            create_booking()
            break
        elif create_other_booking == '0':
            hotel_room_booking_management()
            break
        print('Invalid input. Please try again.')
        create_other_booking = input('Do you want to add another booking? (Type 1 to add another booking, type 0 to go back to main menu): ')
    # Return error if check-in/check-out time < today
    # Return error if check-out <= check-in time

def view_booking():
    # If no booking exists
    if booking_lst == []:
        print('No booking exists')
        create_new_booking = input('Do you want to create a booking? (Type 1 to create a booking, type 0 to go back to main menu): ')
        while True:
            if create_new_booking == '1':
                create_booking()
                break
            elif create_new_booking == '0':
                hotel_room_booking_management()
                break
            print('Invalid input. Please try again.')
            create_new_booking = input('Do you want to create a booking? (Type 1 to create a booking, type 0 to go back to main menu): ')

    # View all bookings
    for i in range(len(booking_lst)):
        print(f'Name: {booking_lst[i][0]}\n'
              f'Check-in time: {booking_lst[i][1]}\n'
              f'Check-out time: {booking_lst[i][2]}\n'
              f'=========================')

    # Back to the main menu option
    back_to_main_menu = input('Type 0 to go back to main menu: ')
    while True:
        if back_to_main_menu == '0':
            hotel_room_booking_management()
            break
        print('Invalid input. Please try again.')
        back_to_main_menu = input('Type 0 to go back to main menu: ')

def min_room_required():
    checkin_times, checkout_times = [], []
    room = 1 # Need at least 2 bookings to use this calculator, so 1 is default
    j = 0 # Var for iterating check-out time
    in_less_than_out = 0 # Number of times check-in time is less than check-out time

    # Add checkin & checkout index into checkin & checkout lists
    for [name, checkin, checkout] in range(len(booking_lst)):
        checkin_times.append(checkin)
        checkout_times.append(checkout)

    # Calculating number of rooms (Explain in detail at the end of program)
    for i in range(len(checkin_times)):
        if checkin_times[i] < checkout_times[j]:
            in_less_than_out += 1
            if in_less_than_out >= 2:
                room += 1
        else:
            j += 1
            in_less_than_out = 0
            if checkin_times[i] < checkout_times[j]:
                in_less_than_out += 1
    return print(f'Minimum number of rooms required to accommodate all the requests is {room}')

def hotel_room_booking_management():
    # Initialize vars
    global booking_lst
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
    num = input('Choose 1 to create contact, 2 to view contact, 3 to use minimum room required calculator, 4 to exit: ')
    while True:
        if num == '1':
            create_booking()
            break
        elif num == '2':
            view_booking()
            break
        elif num == '3':
            if len(booking_lst) >= 2:  # Check if hotel has more than 2 bookings
                min_room_required()
                break
            else:
                print('Hotel need at least 2 bookings to use this calculator!')
                hotel_room_booking_management()  # Back to the main menu if hotel doesn't have any bookings
        elif num == '4':
            break
        print('Please only choose numbers from 1 to 4')
        num = input('Choose 1 to create contact, 2 to view contact, 3 to use minimum room required calculator, 4 to exit: ')

hotel_room_booking_management()

# ============================================================
# 3rd function example:
# Booking with check-in & check-out time
# bookings = [[7, 9], [1, 3], [5, 7], [4, 8], [9, 10]]
# sort_bookings = [[1, 3], [4, 8], [5, 7], [7, 9], [9, 10]]

# Looping start & end into 2 lists
# start_time = [1, 4, 5, 7, 9]
# end_time = [3, 8, 7, 9, 10]

# Visualize by timeline
# 1   2   3   4   5   6   7   8   9   10
# ---------
#             -----------------
#                 ---------
#                         ---------
#                                 ------

# Looping flow explanation:
# If start < end, we iterate start_time
# If start < end more than 2 time, room will increase 1
# If start still < end (3 times, 4 times...), room will keep increase 1 each time
# Until start > end, we iterate end_time
# Keep comparing 2 values until the end of 2 lists

# Step-by-step looping flow:
# 1 < 3
# 4 > 3
# 4 < 8
# 5 < 8 => room = 2
# 7 > 8 => room = 3
# 9 > 8
# 9 > 7
# 9 = 9
# 9 < 10
