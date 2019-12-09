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

# conversion function for Lebanon
# number grades
# grades range from 0 - 100
def convert_lebanon(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 80 and grade <= 100:
        return 'A'
    elif grade >= 70 and grade < 80:
        return 'B'
    elif grade >= 60 and grade < 70:
        return 'C'
    elif grade >= 50 and grade < 60:
        return 'C-'
    elif grade >= 40 and grade < 50:
        return 'D'
    elif grade >= 0 and grade < 40:
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

# conversion function for Nepalese universities that only report marks
# number grades
# grades range from 0 - number of marks
def convert_nepal_marks(input, marks):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade < 0 or grade > marks:
        raise ValueError

    scaled_grade = grade * 100.0 / marks
    return convert_nepal(scaled_grade)

# conversion function for the Philippines
# number grades
# grades range from 1 - 5
def convert_philippines(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade == 5:
        return 'F'
    elif grade >= 4 and grade < 5:
        return 'D'
    elif grade >= 3 and grade < 4:
        return 'C-'
    elif grade >= 2.75 and grade < 3:
        return 'C'
    elif grade >= 2.5 and grade < 2.75:
        return 'C+'
    elif grade >= 2.25 and grade < 2.5:
        return 'B-'
    elif grade >= 2 and grade < 2.25:
        return 'B'
    elif grade >= 1.75 and grade < 2:
        return 'B+'
    elif grade >= 1.5 and grade < 1.75:
        return 'A-'
    elif grade >= 1.25 and grade < 1.5:
        return 'A'
    elif grade >= 1 and grade < 1.25:
        return 'A+'
    else: # invalid
        raise ValueError

# conversion function for Russia
# letter grades
def convert_russia(input):
    grade = input.upper()

    if grade == 'EXCELLENT' or grade == 'E':
        return 'A'
    elif grade == 'GOOD' or grade == 'G':
        return 'B'
    elif grade == 'SATISFACTORY' or grade == 'S':
        return 'C'
    elif grade == 'UNSATISFACTORY' or grade == 'U':
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for Saudi Arabia
# letter grades
def convert_saudi_arabia(input):
    grade = input.upper()

    if grade == 'A+':
        return 'A+'
    elif grade == 'A':
        return 'A'
    elif grade == 'B+':
        return 'A-'
    elif grade == 'B':
        return 'B+'
    elif grade == 'C+':
        return 'B'
    elif grade == 'C':
        return 'B-'
    elif grade == 'D+':
        return 'C+'
    elif grade == 'D':
        return 'C'
    elif grade == 'F' or grade == 'NF' or grade == 'DN':
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for Singapore
# letter grades
def convert_singapore(input):
    grade = input.upper()

    if grade == 'A+' or grade == 'AD':
        return 'A+'
    elif grade == 'A':
        return 'A'
    elif grade == 'A-':
        return 'A-'
    elif grade == 'B+':
        return 'B+'
    elif grade == 'B':
        return 'B'
    # Scholaro doesn't have this grade listed on their website
    # however, National University of Singapore uses it
    elif grade == 'B-':
        return 'B-'
    elif grade == 'C+':
        return 'C+'
    elif grade == 'C':
        return 'C'
    elif grade == 'C-':
        return 'C-'
    elif grade == 'D+':
        return 'D+'
    elif grade == 'D':
        return 'D'
    # Scholaro doesn't have this grade listed on their website
    # however, National University of Singapore uses it
    elif grade == 'D-':
        return 'D-'
    elif grade == 'F':
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for South Korea
# letter grades
def convert_south_korea(input):
    grade = input.upper()

    if grade == 'A+':
        return 'A+'
    elif grade == 'A' or grade == 'A0' or grade == 'AO':
        return 'A'
    elif grade == 'A-':
        return 'A-'
    elif grade == 'B+':
        return 'B+'
    elif grade == 'B' or grade == 'B0' or grade == 'BO':
        return 'B'
    elif grade == 'B-':
        return 'B-'
    elif grade == 'C+':
        return 'C+'
    elif grade == 'C' or grade == 'C0' or grade == 'CO':
        return 'C'
    elif grade == 'C-':
        return 'C-'
    elif grade == 'D+':
        return 'D+'
    elif grade == 'D' or grade == 'D0' or grade == 'DO':
        return 'D'
    elif grade == 'D-':
        return 'D-'
    elif grade == 'F':
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

# conversion function for Vietnam
# number grades
# grades range from 0 - 10
def convert_vietnam(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 9 and grade <= 10:
        return 'A+'
    elif grade >= 8 and grade < 9:
        return 'A'
    elif grade >= 7 and grade < 8:
        return 'B+'
    elif grade >= 6 and grade < 7:
        return 'B'
    elif grade >= 5 and grade < 6:
        return 'C'
    # note that there's a carve-out for a D here, but exactly when this applies is unclear
    # Scholaro says "with an overall average grade of at least 5.0"
    # how this applies to one course is unclear, so assigning an F is safer
    elif grade >= 0 and grade < 5:
        return 'F'
    else: # invalid
        raise ValueError
