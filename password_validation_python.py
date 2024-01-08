# Import libraries
import re

# Initialize vars
max_attemp = 5  # Input maximum password attemps

for attemp in range(max_attemp + 1):
    # Initialize password requirements
    passwd_reqs = {'digit': 0, 'upper': 0, 'special': 0, 'cons': 0}
    invalid_passwd_mess = {'digit': 'one number', 'upper': 'one uppercase', 'special': 'one special character',
                           'cons': 'only 2 consecutive numbers'}

    # Set maximum password attemps
    if attemp == max_attemp:
        print('Maximum password attemps, please try again later!')
        break

    # Input a valid password
    passwd = input('Enter your password: ')

    # Check if password has at least 8 characters
    if len(passwd) < 8:
        print('Re-enter password (Password must contains at least 8 characters)')
        continue

    # Check if password contains number, upper character and special character
    for i in range(len(passwd)):
        if passwd[i].isdigit() is True:
            passwd_reqs['digit'] += 1
        if passwd[i].isupper() is True:
            passwd_reqs['upper'] += 1
        if passwd[i].isalnum() is False:
            passwd_reqs['special'] += 1

    # Check if password contains 3 consecutive numbers
    consecutive_num = re.search(r'\d{3}', passwd)
    if consecutive_num is None:
        passwd_reqs['cons'] += 1

    # Validating all conditions
    if passwd_reqs['digit'] >= 1 and passwd_reqs['upper'] >= 1 and passwd_reqs['special'] >= 1 and passwd_reqs['cons'] >= 1:
        print('Valid password')
        break
    for req in passwd_reqs.keys():
        if passwd_reqs[req] == 0:
            print(f'Re-enter password (Invalid password - Password must contains {invalid_passwd_mess[req]})')
