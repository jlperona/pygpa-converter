# conversion function for 10 point scale in India
# number grades
# grades range from 0 - 10
def convert_india_10(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 9 and grade <= 10:
        return 'A'
    elif grade >= 8 and grade < 9:
        return 'B+'
    elif grade >= 7 and grade < 8:
        return 'B'
    elif grade >= 6 and grade < 7:
        return 'B-'
    elif grade >= 4 and grade < 6:
        return 'C'
    elif grade >= 0 and grade < 4:
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for 100 point scale in India
# number grades
# grades range from 0 - 100
def convert_india_100(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 60 and grade <= 100:
        return 'A'
    elif grade >= 50 and grade < 60:
        return 'B'
    elif grade >= 40 and grade < 50:
        return 'C'
    elif grade >= 0 and grade < 40:
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for Indian universities that only report marks
# number grades
# grades range from 0 - number of marks
def convert_india_marks(input, marks):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade < 0 or grade > marks:
        raise ValueError

    scaled_grade = grade * 100.0 / marks
    return convert_india_100(scaled_grade)
