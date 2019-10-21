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
