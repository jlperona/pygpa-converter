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

# conversion function for South Africa
# number grades
# grades range from 0 - 100
def convert_south_africa(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 75 and grade <= 100:
        return 'A'
    elif grade >= 70 and grade < 75:
        return 'B+'
    elif grade >= 60 and grade < 70:
        return 'B'
    elif grade >= 50 and grade < 60:
        return 'C'
    elif grade >= 0 and grade < 50:
        return 'F'
    else: # invalid
        raise ValueError
