'''MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written.
They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor, they should receive more money.
Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.
For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].'''

def compute_bonus(ees_loc):
    for i in range(1, len(ees_loc)):
        if ees_loc[i] > ees_loc[i-1]:
            ees_b[i] = ees_b[i-1] + 1
        elif ees_loc[i] < ees_loc[i-1]:
            for j in range(i,0,-1):
                if ees_b[j] == ees_b[j-1]:
                    ees_b[j-1] +=1
    return print(f'Employees lines of code: {ees_loc} \nEmployees bonus: {ees_b}')

ees_ls = list(input('Enter lines of codes for each employee (seperated by comma): ').split(','))
ees_loc = [int(ee) for ee in ees_ls]
ees_b = [1] * len(ees_loc) #Everyone has bonus even they write only 1 line of code, so all employees will have "1-bonus" by default
compute_bonus(ees_loc)
