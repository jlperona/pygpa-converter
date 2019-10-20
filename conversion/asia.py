# conversion function for China
# number grades
# grades range from 0 - 100
def convert_china(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 90 and grade <= 100:
        return 'A'
    elif grade >= 80 and grade < 90:
        return 'B'
    elif grade >= 70 and grade < 80:
        return 'C'
    elif grade >= 60 and grade < 70:
        return 'D'
    elif grade >= 0 and grade < 60:
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for China, modified for the scale in use at UC Davis
# number grades
# grades range from 0 - 100
def convert_china_modified(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    # handle easy cases first
    if grade >= 91 and grade <= 100:
        return 4.0
    elif grade >= 0 and grade <= 51:
        return 0.0
    elif grade < 0 or grade > 100:
        raise ValueError

    # truncate to do easy math
    truncated_grade = int(grade)
    return (truncated_grade / 10.0) - 5.1

# conversion function for Taiwan
# number grades
# grades range from 0 - 100
def convert_taiwan(input):
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
    elif grade >= 0 and grade < 60:
        return 'F'
    else: # invalid
        raise ValueError