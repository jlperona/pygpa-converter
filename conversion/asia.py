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
