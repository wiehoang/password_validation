# Given a positive integer 'n' less than or equal to 26, you are required to print the below pattern
# Sample
# Input: 4
# Output:
# ------d------
# ----d-c-d----
# --d-c-b-c-d--
# d-c-b-a-b-c-d
# --d-c-b-c-d--
# ----d-c-d----
# ------d------

def print_pattern(n):
    for row in range(1, 2 * n):

        # Calculate a number of half-side dashes on each row
        num_of_dashes: int
        if row <= n:
            num_of_dashes = (n - row) * 2
        else:
            num_of_dashes = (row - n) * 2

        # Calculate a number of half-left chars on each row
        num_of_hl_chars: int
        if row <= n:
            num_of_hl_chars = row
        else:
            num_of_hl_chars = row - num_of_dashes

        # Assign an ASCII value of character
        char_val: int = 97 + n - 1  # 97 is an ASCII code of starting letter 'a'

        # Print half-left dashes
        for hld in range(num_of_dashes):
            print('-', end = '')

        # Print half-left chars
        for hlc in range(num_of_hl_chars):
            print(chr(char_val), end = '-')
            char_val -= 1

        # Print half-right chars
        upd_char_val = char_val + 2  # Assign a new char_val to print symmetrically with the half-left chars
        for hrc in range(num_of_hl_chars - 1):
            if row == n and hrc == (num_of_hl_chars - 2): # Avoid printing a last dash on a middle row
                print(chr(upd_char_val), end='')
            else:
                print(chr(upd_char_val), end = '-')
            upd_char_val += 1

        # Print half-right dashes
        for hrd in range(num_of_dashes - 1):
            print('-', end = '')

        # Add a new line after printed a row
        print()


def alphabetic_pattern():
    n = int(input('Enter a number of row: '))
    while n < 2 or n > 26:
        print('Please choose a number from 2 to 26')
        n = int(input('Enter a number of row: '))
    print_pattern(n)


alphabetic_pattern()
