import conversion.america as america
import utils.excel

class Course:

    def __init__(self, units, given_grade, scale_type, row, first_column):
        # input variables taken from CSV file
        self.units = float(units)
        self.given_grade = given_grade
        self.scale_type = scale_type

        # variables used for calculating United States equivalent
        self.letter_grade = None
        self.letter_grade_points = None

        # debugging. note that courses take two columns in the input CSV file
        self.row = row
        self.first_column = utils.excel.column_number_to_string(first_column)

    def convert_to_letter(self):
        if self.scale_type == 'United States':
            self.letter_grade = america.convert_united_states(self.given_grade)

        self.letter_grade_points = float(america.convert_letter_to_4(self.letter_grade))
