# conversion function for Nigeria
# letter grades
def convert_nigeria(input):
    grade = input.upper()

    if grade == 'A' or grade == 'AB':
        return 'A'
    elif grade == 'B' or grade == 'BC':
        return 'B+'
    elif grade == 'C' or grade == 'CD':
        return 'B'
    elif grade == 'D':
        return 'C+'
    elif grade == 'E':
        return 'C'
    elif grade == 'F':
        return 'F'
    else: # invalid
        raise ValueError
