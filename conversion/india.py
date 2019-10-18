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
