# conversion function for United States and other grades already in grade point form
# number grades
# numbers range from 0 - 4.3
def convert_4(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade > 4.3 or grade < 0:
        raise ValueError
    else:
        return min(4.0, grade)

# conversion function for Argentina
# number grades
# numbers range from 0 - 10
def convert_argentina(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 9 and grade <= 10:
        return 'A'
    elif grade >= 8 and grade < 9:
        return 'A-'
    elif grade >= 7 and grade < 8:
        return 'B+'
    elif grade >= 6 and grade < 7:
        return 'B'
    elif grade >= 4 and grade < 6:
        return 'C'
    elif grade >= 0 and grade < 4:
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for Brazil
# number grades
# numbers range from 0 - 100
def convert_brazil(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 90 and grade <= 100:
        return 'A'
    elif grade >= 70 and grade < 90:
        return 'B'
    elif grade >= 50 and grade < 70:
        return 'C'
    elif grade >= 30 and grade < 50:
        return 'D'
    elif grade >= 0 and grade < 30:
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for Brazil single letter grades
# single letter grades
def convert_brazil_single(input):
    grade = input.upper()

    if grade == 'A':
        return 'A'
    elif grade == 'B':
        return 'B'
    elif grade == 'C':
        return 'C'
    elif grade == 'D':
        return 'D'
    elif grade == 'F':
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for Brazil double letter grades
# double letter grades
def convert_brazil_double(input):
    grade = input.upper()

    if grade == 'SS':
        return 'A'
    elif grade == 'MS':
        return 'B'
    elif grade == 'MM':
        return 'C'
    elif grade == 'MI' or grade == 'II':
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for British Columbia, Canada
# number grades
# grades range from 0 - 100
def convert_canada_british_columbia(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 90 and grade <= 100:
        return 'A+'
    elif grade >= 85 and grade < 90:
        return 'A'
    elif grade >= 80 and grade < 85:
        return 'A-'
    elif grade >= 76 and grade < 80:
        return 'B+'
    elif grade >= 72 and grade < 76:
        return 'B'
    elif grade >= 68 and grade < 72:
        return 'B-'
    elif grade >= 64 and grade < 68:
        return 'C+'
    elif grade >= 60 and grade < 64:
        return 'C'
    elif grade >= 55 and grade < 60:
        return 'C-'
    elif grade >= 50 and grade < 55:
        return 'D'
    elif grade >= 0 and grade < 50:
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for Ontario, Canada
# number grades
# grades range from 0 - 100
def convert_canada_ontario(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 90 and grade <= 100:
        return 'A+'
    elif grade >= 80 and grade < 90:
        return 'A'
    elif grade >= 70 and grade < 80:
        return 'B'
    elif grade >= 60 and grade < 70:
        return 'C'
    elif grade >= 50 and grade < 60:
        return 'D'
    elif grade >= 0 and grade < 50:
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for United States
# letter grades
# only verifies validity of the input grade
def convert_united_states(input):
    # length of input should only be one or two characters, example 'A' or 'A-'
    if not (len(input) == 1 or len(input) == 2):
        raise ValueError

    caps_input = input.upper()

    if not (caps_input[0] == 'A' or caps_input[0] == 'B' or caps_input[0] == 'C' or caps_input[0] == 'D' or caps_input[0] == 'F'):
        raise ValueError

    if len(caps_input) == 2:
        if not (caps_input[1] == '+' or caps_input[1] == '-'):
            raise ValueError

    return caps_input

# conversion function for United States letter grades
# transforms letter grades into their numerical equivalents
# note that this is function is only run on outputs from conversion functions
# thus, if an exception occurs in here, there's something wrong with the conversion function originally called
def convert_letter_to_4(input):
    current_points = -1.0

    # handle first character
    if input[0] == 'A':
        current_points = 4
    elif input[0] == 'B':
        current_points = 3
    elif input[0] == 'C':
        current_points = 2
    elif input[0] == 'D':
        current_points = 1
    elif input[0] == 'F':
        return 0
    else:
        raise ValueError

    if len(input) == 1:
        return current_points
    else: # handle second character if it exists
        if len(input) != 2:
            raise ValueError
        elif input[1] == '+':
            return min(4.0, current_points + 0.3)
        elif input[1] == '-':
            return current_points - 0.3
        else:
            raise ValueError
