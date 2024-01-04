# Import libraries
import re

# Initialize vars
digit, upper, special, cons = 0, 0, 0, 0
max_attemp = 5 #Input maximum password attemps

for attemp in range(max_attemp+1):
    # Set maximum password attemps
    if attemp==max_attemp:
        print('Maximum password attemps, please try again later')
        break

    # Input a valid password
    passwd = input('Enter your password')

    # Check if password has at least 8 characters
    if len(passwd) < 8:
        print('Re-enter password (Password must be at least 8 characters)')
        continue

    # Check if password contains number, upper character and special character
    for i in range(len(passwd)):
        if passwd[i].isdigit() == True:
            digit+=1
        if passwd[i].isupper() == True:
            upper+=1
        if passwd[i].isalnum() == False:
            special+=1

    # Check if password contains 3 consecutive numbers
    consecutive_num = re.search(r'\d{3}', passwd)
    if consecutive_num is not None:
        cons+=1

    # Validating all conditions
    if digit>=1 and upper>=1 and special>=1 and cons>=1:
        print('Valid password')
        break
    else:
        print('Re-enter password (Invalid password)')
        continue