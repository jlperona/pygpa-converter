# conversion function for grades that are already in grade point form
def convert_4(input):
    try:
        grade = float(input)
    except ValueError:
        raise

    if grade > 4.3 or grade < 0:
        raise ValueError
    else:
        return min(4.0, grade)

# conversion function for United States letter grades
# only verifies validity of the input grade
def convert_united_states(input):
    # length of input should only be one or two characters, example "A" or "A-"
    if not (len(input) == 1 or len(input) == 2):
        raise ValueError

    caps_input = input.upper()

    if not (caps_input[0] == 'A' or caps_input[0] == 'B' or caps_input[0] == 'C' or caps_input[0] == 'D' or caps_input[0] == 'F'):
        raise ValueError

    if len(caps_input) == 2:
        if not (caps_input[1] == '+' or caps_input[1] == '-'):
            raise ValueError

    return caps_input

# conversion function for United States letter grades
# transforms letter grades into their numerical equivalents
# note that this is function is only run on outputs from conversion functions
# thus, if an exception occurs in here, there's something wrong with that conversion function
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
    elif input[0] == 'F':
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
