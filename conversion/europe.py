# conversion function for Austria
# number grades
# grades range from 1 - 5
def convert_austria(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade == 5:
        return 'F'
    elif grade >= 4 and grade < 5:
        return 'C'
    elif grade >= 3 and grade < 4:
        return 'B'
    elif grade >= 2 and grade < 3:
        return 'A-'
    elif grade >= 1 and grade < 2:
        return 'A'
    else: # invalid
        raise ValueError
