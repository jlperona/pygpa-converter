def convert_nigeria(input: str) -> str:
    """Conversion function for Nigeria.
    Letter grades.
    """
    grade = input.upper()

    if grade == 'A' or grade == 'AB':
        return 'A'
    elif grade == 'B' or grade == 'BC':
        return 'B+'
    elif grade == 'C' or grade == 'CD':
        return 'B'
    elif grade == 'D':
        return 'C+'
    elif grade == 'E':
        return 'C'
    elif grade == 'F':
        return 'F'
    else:  # invalid
        raise ValueError


def convert_south_africa(input: str) -> str:
    """Conversion function for South Africa.
    Number grades.
    Grades range from 0 - 100.
    """
    try:
        grade = float(input)
    except ValueError:  # invalid conversion
        raise

    if grade >= 75 and grade <= 100:
        return 'A'
    elif grade >= 70 and grade < 75:
        return 'B+'
    elif grade >= 60 and grade < 70:
        return 'B'
    elif grade >= 50 and grade < 60:
        return 'C'
    elif grade >= 0 and grade < 50:
        return 'F'
    else:  # invalid
        raise ValueError


def convert_uganda(input: str) -> str:
    """Conversion function for Uganda.
    Number grades.
    Grades range from 1 - 9.
    """
    try:
        grade = float(input)
    except ValueError:  # invalid conversion
        raise

    if grade == 9:
        return 'F'
    elif grade >= 8 and grade < 9:
        return 'C'
    elif grade >= 7 and grade < 8:
        return 'C'
    elif grade >= 5 and grade < 7:
        return 'B'
    elif grade >= 3 and grade < 5:
        return 'B'
    elif grade >= 1 and grade < 3:
        return 'A'
    else:  # invalid
        raise ValueError
