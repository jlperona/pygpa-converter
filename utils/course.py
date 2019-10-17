import conversion.america as america
import utils.excel

class Course:

    def __init__(self, units, given_grade, scale_type, row, column):
        # input variables taken from CSV file
        self.given_grade = given_grade
        self.scale_type = scale_type

        # variables used for calculating United States equivalent
        self.letter_grade = None
        self.letter_grade_points = None

        # debugging. note that courses take two columns in the input CSV file
        self.row = row
        self.units_column = utils.excel.column_number_to_string(column)
        self.grade_column = utils.excel.column_number_to_string(column + 1)

        try:
            self.units = float(units)
        except ValueError:
            invalid_units_exception = str('Invalid units input at line '
                + str(self.row) + ', column ' + self.units_column + '.')
            raise Exception(invalid_units_exception) from None

    def convert_to_letter(self):
        try:
            if self.scale_type == 'United States':
                self.letter_grade = america.convert_united_states(self.given_grade)
            else:
                invalid_grade_scale_exception = str('Invalid grade scale \'' + self.scale_type
                    + '\' at line ' + str(self.row) + ', column C.')
                raise Exception(invalid_grade_scale_exception)
        except ValueError:
            invalid_grade_exception = str('Invalid grade for scale type \'' + self.scale_type
                + '\' at line ' + str(self.row) + ', column ' + self.grade_column + '.')
            raise Exception(invalid_grade_exception) from None

        # if this fails then there's a problem with the conversion function
        try:
            self.letter_grade_points = float(america.convert_letter_to_4(self.letter_grade))
        except ValueError:
            invalid_us_letter_grade_exception = str('Input grade \'' + self.letter_grade
                + '\' for grade scale \'' + self.scale_type + '\' at line ' + str(self.row)
                + ', column ' + self.grade_column
                + ', caused an internal error.\n'
                + 'This usually means that the conversion function for \'' + self.scale_type
                + '\' has a bug in it.\nPlease report this on GitHub or via email.')
            raise Exception(invalid_us_letter_grade_exception) from None
