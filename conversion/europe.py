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

# conversion function for Belgium
# number grades
# grades range from 0 - 20
def convert_belgium(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade == 20:
        return 'A+'
    elif grade >= 18 and grade < 20:
        return 'A+'
    elif grade >= 16 and grade < 18:
        return 'A'
    elif grade >= 14 and grade < 16:
        return 'B'
    elif grade >= 12 and grade < 14:
        return 'C'
    elif grade >= 10 and grade < 12:
        return 'C-'
    elif grade >= 8 and grade < 10:
        return 'F'
    elif grade >= 0 and grade < 8:
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for Bulgaria
# number grades
# grades range from 2 - 6
def convert_bulgaria(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade == 6:
        return 'A'
    elif grade >= 5 and grade < 6:
        return 'A'
    elif grade >= 4 and grade < 5:
        return 'B'
    elif grade >= 3 and grade < 4:
        return 'C'
    elif grade >= 2 and grade < 3:
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for Denmark
# number grades
# grades range from 0 - 12 or -3
def convert_denmark(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade == 12:
        return 'A+'
    elif grade >= 10 and grade < 12:
        return 'A'
    elif grade >= 7 and grade < 10:
        return 'B'
    elif grade >= 4 and grade < 7:
        return 'C'
    elif grade >= 2 and grade < 4:
        return 'D'
    elif grade >= 0 and grade < 2:
        return 'F'
    elif grade == -3:
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for the European Credit Transfer System
# letter grades
def convert_ects(input):
    grade = input.upper()

    # some of these grades were not in Scholaro's database
    # there were taken from transcripts by the University of New South Wales
    if grade == 'A':
        return 'A'
    elif grade == 'B':
        return 'B+'
    elif grade == 'C':
        return 'B'
    elif grade == 'D':
        return 'C+'
    elif grade == 'E':
        return 'C'
    elif grade == 'F' or grade == 'FX':
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for Germany
# number grades
# grades range from 1 - 6
def convert_germany(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade > 4 and grade <= 6:
        return 'F'
    elif grade > 3.5 and grade <= 4:
        return 'C'
    elif grade > 2.5 and grade <= 3.5:
        return 'B'
    elif grade > 1.5 and grade <= 2.5:
        return 'A'
    elif grade >= 1 and grade <= 1.5:
        return 'A'
    else: # invalid
        raise ValueError
