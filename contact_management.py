# Create a simple application to manage a contact. You can add, delete, and display contacts.
# Each contact can contain information such as name, phone number.
# Require input validation, name only enter string, phone number enter required int of 10 characters and start with 0,
# cannot have 2 identical phone numbers

# Import libraries
import re
import pandas as pd

def validate_contact(info, contact_db):
    for key in info.keys():
        valid = 0 # Var to break out while loop
        while valid == 0:
            value = input(f'{key}: ')
            match key:
                case 'Name':
                    if re.search('[^A-Za-z]', value) == None:
                        valid += 1
                        info[key] = value.title()
                    else:
                        print('Invalid input, please only enter alphabetical characters')
                case 'Phone number':
                    if re.search('[^0-9]', value):
                        print('Please only enter numeric characters')
                    elif re.search('^0', value) == None or len(value) != 10:
                        print('Phone number must contains 10-digit and starts with 0')
                    num_exist = ''
                    for dict in contact_db:
                        if value in dict['Phone number']:
                            print('Phone number exists already, please enter another one!')
                            num_exist = '1'
                        else: num_exist = '0'
                    if num_exist == '0':
                        valid += 1
                        info[key] = value
    return info


def create_contact(contact_db):
    contact_info = {
        'Name': '',
        'Phone number': ''
    }
    validate_contact(contact_info, contact_db)
    contact_db.append(contact_info)
    print('Contact added successfully!')
    return contact_db

def view_contact(contact_db):
    if contact_db == []:
        return print('No contacts found!')
    else:
        contact_df = pd.DataFrame(contact_db)
        return print(contact_df)

def delete_contact():
    pass

def contact_management():
    # Initialize vars
    contact_db = []

    # Welcome message
    print('''
        ==================================
		WELCOME TO CONTACT MANAGEMENT
		==================================
		1. Create Contact
		2. View Contact
		3. Exit
		(Choose 1 to create contact, 2 to view contact, 3 to exit program) : 
		''')

    action = '0'
    while action != '3':
        curr_action = input('Enter 1 to create contact, 2 to view contact, 3 to exit program: ')
        match curr_action:
            case '1':
                create_contact(contact_db)
            case '2':
                view_contact(contact_db)
            case '3':
                break
            case _:
                print('Invalid input, please only enter numbers from 1 to 3')

contact_management()

