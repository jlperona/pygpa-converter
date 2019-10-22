import conversion.america

# conversion function for Bangladesh
# number grades
# grades range from 0 - 100
def convert_bangladesh(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 60 and grade <= 100:
        return 'A'
    elif grade >= 55 and grade < 60:
        return 'B+'
    elif grade >= 50 and grade < 55:
        return 'B'
    elif grade >= 43 and grade < 50:
        return 'C+'
    elif grade >= 35 and grade < 43:
        return 'C'
    elif grade >= 0 and grade < 35:
        return 'F'
    else: # invalid
        raise ValueError

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

# conversion function for Hong Kong
# alias of United States
# single letter grades
def convert_hong_kong(input):
    return conversion.america.convert_united_states(input)

# conversion function for Iran
# number grades
# grades range from 0 - 20
def convert_iran(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 18 and grade <= 20:
        return 'A+'
    elif grade >= 16 and grade < 18:
        return 'A'
    elif grade >= 14 and grade < 16:
        return 'B'
    elif grade >= 12 and grade < 14:
        return 'C'
    elif grade >= 10 and grade < 12:
        return 'D'
    elif grade >= 0 and grade < 10:
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for Japan
# number grades
# grades range from 0 - 100
def convert_japan(input):
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

# conversion function for Nepal
# number grades
# grades range from 0 - 100
def convert_nepal(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 80 and grade <= 100:
        return 'A+'
    elif grade >= 60 and grade < 80:
        return 'A'
    elif grade >= 46 and grade < 60:
        return 'B'
    elif grade >= 32 and grade < 46:
        return 'C'
    elif grade >= 0 and grade < 32:
        return 'F'
    else: # invalid
        raise ValueError

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
