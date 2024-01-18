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
    global booking_lst
    booking_lst = []
    # Validating guest's name
    while True:
        temp_booking = []
        guest_name = input('Name: ')
        if re.search('[^A-Za-z]', guest_name) == None:
            valid_guess_name = guest_name.title()
            temp_booking.append(valid_guess_name)
            break
        else:
            print('Please input a valid name format')

    # Validating guest's check-in time
    while True:
        guest_checkin = input('Check-in time (dd/mm/yyyy): ')
        try:
            if datetime.strptime(guest_checkin, '%d/%m/%Y'):
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

    booking_lst.append(temp_booking)
    # Return error if name is obscene (Fuck, Damn, Dog...)
    # Return error if check-in/check-out time < today
    # Return error if check-out <= check-in time

def view_booking():
    for i in range(len(booking_lst)):
        for j in booking_lst[i]:
            print(j)
create_booking()
view_booking()

def room_required():
    pass

def hotel_room_booking_management():
    # Welcome message
    print('''
    	========================================
		WELCOME TO HOTEL ROOM BOOKING MANAGEMENT
		========================================
		1. Create Booking
		2. View Booking
		3. Room Required Calculator
		''')

    # User input
    user_input = int(input('Choose 1 to create contact, 2 to view contact, 3 to use room required calculator: '))
    while user_input not in range(1,4):
        if user_input == 1:
            create_booking()
        elif user_input == 2:
            view_booking()
        elif user_input == 3:
            room_required()
        else:
            print('Please only choose numbers from 1 to 3')
            user_input = int(input('Choose 1 to create contact, 2 to view contact, 3 to use room required calculator: '))

#hotel_room_booking_management()