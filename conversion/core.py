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
    elif input[0] == 'F': # no modifiers for an F
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
