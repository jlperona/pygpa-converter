import conversion.america as america
import utils.excel

# representation of a course defined via each line of the input csv file
# also contains helper functions to convert the course to the United States grade scale
class Course:

    def __init__(self, units, given_grade, scale_type, row, column):
        # input variables taken from CSV file
        self.given_grade = given_grade
        self.scale_type = scale_type

        # variables used for calculating United States equivalent
        self.letter_grade = None
        self.letter_grade_points = None

        # debugging, note that courses take two columns in the input CSV file
        self.row = row
        self.units_column = utils.excel.column_number_to_string(column)
        self.grade_column = utils.excel.column_number_to_string(column + 1)

        # attempt conversion of units to float
        try:
            self.units = float(units)

            if self.units < 0:
                raise ValueError
        except ValueError: # invalid unit input
            invalid_units_exception = str('Invalid unit input \'' + units
                + '\' at cell \'' + self.units_column + str(self.row) + '\'.')
            raise Exception(invalid_units_exception) from None

    # convert given grade to United States letter grade using a conversion function
    def convert_to_letter(self):
        try:
            if self.scale_type == '4':
                self.letter_grade_points = america.convert_4(self.given_grade)
                return
            elif self.scale_type == 'Argentina':
                self.letter_grade = america.convert_argentina(self.given_grade)
            elif self.scale_type == 'Brazil':
                self.letter_grade = america.convert_brazil(self.given_grade)
            elif self.scale_type == 'Brazil Single':
                self.letter_grade = america.convert_brazil_single(self.given_grade)
            elif self.scale_type == 'United States':
                self.letter_grade = america.convert_united_states(self.given_grade)
            else: # no such grade scale exists
                invalid_grade_scale_exception = str('Invalid grade scale \'' + self.scale_type
                    + '\' at cell \'C' + str(self.row) + '\'.')
                raise Exception(invalid_grade_scale_exception)
        except ValueError: # conversion function raised invalid input
            invalid_grade_exception = str('Invalid grade \'' + self.given_grade + '\' for scale type \'' + self.scale_type
                + '\' at cell \'' + self.grade_column + str(self.row) + '\'.')
            raise Exception(invalid_grade_exception) from None

        # convert United States letter grade to grade points
        try:
            self.letter_grade_points = float(america.convert_letter_to_4(self.letter_grade))
        # if this fails then there's a problem with the relevant conversion function
        except ValueError:
            invalid_us_letter_grade_exception = str('Input grade \'' + self.letter_grade
                + '\' for grade scale \'' + self.scale_type + '\' at cell \'' + self.grade_column
                + str(self.row) + '\' caused an internal error.\n'
                + 'This usually means that the conversion function for \'' + self.scale_type
                + '\' has a bug in it.\nPlease report this on GitHub or via email.')
            raise Exception(invalid_us_letter_grade_exception) from None
