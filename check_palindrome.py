# Given a positive integer, write a function that returns
# true if the given number is a palindrome, else false.
# For example, 12321 is a palindrome, but 1451 is not a palindrome.


def pal_rec(num, f_idx, l_idx):
    # Base case, return True if already checked the middles of integer
    if f_idx >= l_idx:
        return print('True')
    # Check first idx digit and last idx digit recursively
    elif f_idx < l_idx:
        if num[f_idx] == num[l_idx]:
            return pal_rec(num, f_idx + 1, l_idx - 1) # Check "the next" first idx digit and last idx digit
        elif num[f_idx] != num[l_idx]:
            return print('False')


def check_pal(num):
    n = len(num)
    # Return True if there is only 1 digit
    if n == 1:
        return print('True')
    # If there are over 2 digits, check first idx digit and last idx digit
    else:
        pal_rec(num, 0, n - 1)


# Test cases
if __name__ == "__main__":
    check_pal('12321')
    check_pal('1451')
    check_pal('35799753')