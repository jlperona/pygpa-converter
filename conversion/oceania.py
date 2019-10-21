# conversion function for Australian letter grades
# letter grades
def convert_australia(input):
    grade = input.upper()

    # some of these grades were not in Scholaro's database
    # there were taken from transcripts by the University of New South Wales
    if grade == 'HD':
        return 'A+'
    elif grade == 'D' or grade == 'DN':
        return 'A'
    elif grade == 'CR':
        return 'B'
    elif grade == 'P' or grade == 'PS':
        return 'C'
    elif grade == 'PC':
        return 'D'
    elif grade == 'N' or grade == 'F' or grade == 'FL':
        return 'F'
    else: # invalid
        raise ValueError

# conversion function for New South Wales, Australia
# number grades
# grades range from 0 - 100
def convert_australia_new_south_wales(input):
    try:
        grade = float(input)
    except ValueError: # invalid conversion
        raise

    if grade >= 85 and grade <= 100:
        return 'A+'
    elif grade >= 75 and grade < 85:
        return 'A'
    elif grade >= 65 and grade < 75:
        return 'B'
    elif grade >= 50 and grade < 65:
        return 'C'
    elif grade >= 0 and grade < 50:
        return 'F'
    else: # invalid
        raise ValueError
