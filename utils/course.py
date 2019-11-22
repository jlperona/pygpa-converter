# non-country function imports
import conversion.core
import utils.excel

# country function imports
import conversion.africa
import conversion.america
import conversion.asia
import conversion.europe
import conversion.india
import conversion.oceania

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
        self.units_column = int(column)
        self.grade_column = int(column + 1)

        # attempt conversion of units to float
        try:
            self.units = float(units)

            if self.units < 0:
                raise ValueError
        except ValueError: # invalid unit input
            invalid_units_exception = str('Invalid unit input \'' + units
                + '\' at cell \'' + utils.excel.col_row_to_cell(self.units_column, self.row) + '\'.')
            raise Exception(invalid_units_exception) from None

    # convert given grade to United States letter grade using a conversion function
    def convert_to_letter(self, india_10_dict):
        # first try to see if scale name is in the India 10 dictionary that was passed in
        if self.scale_type in india_10_dict:
            try:
                converted_number = india_10_dict[self.scale_type][self.given_grade.upper()]
                self.letter_grade = conversion.india.convert_india_10(converted_number)
            except KeyError:
                invalid_india_10_grade_exception = str('Invalid grade \'' + self.given_grade
                    + '\' for scale type \'' + self.scale_type + '\' at cell \''
                    + utils.excel.col_row_to_cell(self.grade_column, self.row) + '\'.')
                raise Exception(invalid_india_10_grade_exception) from None
            except ValueError:
                invalid_india_10_letter_grade_exception = str('Converted input grade \''
                    + converted_number + '\' from original input grade \'' + self.given_grade
                    + '\' for grade scale \'' + self.scale_type + '\' at cell \''
                    + utils.excel.col_row_to_cell(self.grade_column, self.row)
                    + '\' caused an internal error.\n'
                    + 'This usually means that the entry for \'' + self.scale_type
                    + '\' in \'data/india10.csv\' has a mistake in it.\n'
                    + 'Please report this on GitHub or via email.')
                raise Exception(invalid_india_10_letter_grade_exception) from None
        else: # otherwise try to see if scale name is in conversion functions
            try:
                ### AFRICA SECTION

                if self.scale_type == 'Nigeria':
                    self.letter_grade = conversion.africa.convert_nigeria(self.given_grade)
                elif self.scale_type == 'South Africa':
                    self.letter_grade = conversion.africa.convert_south_africa(self.given_grade)
                elif self.scale_type == 'Uganda':
                    self.letter_grade = conversion.africa.convert_uganda(self.given_grade)

                ### AMERICA SECTION

                elif self.scale_type == '4':
                    self.letter_grade_points = conversion.america.convert_4(self.given_grade)
                    return
                elif self.scale_type == 'Argentina':
                    self.letter_grade = conversion.america.convert_argentina(self.given_grade)
                elif self.scale_type == 'Brazil':
                    self.letter_grade = conversion.america.convert_brazil(self.given_grade)
                elif self.scale_type == 'Brazil Single':
                    self.letter_grade = conversion.america.convert_brazil_single(self.given_grade)
                elif self.scale_type == 'Brazil Double':
                    self.letter_grade = conversion.america.convert_brazil_double(self.given_grade)
                elif self.scale_type == 'Canada':
                    self.letter_grade = conversion.america.convert_canada(self.given_grade)
                elif self.scale_type == 'Canada British Columbia':
                    self.letter_grade = conversion.america.convert_canada_british_columbia(self.given_grade)
                elif self.scale_type == 'Canada Ontario':
                    self.letter_grade = conversion.america.convert_canada_ontario(self.given_grade)
                elif self.scale_type == 'Mexico':
                    self.letter_grade = conversion.america.convert_mexico(self.given_grade)
                elif self.scale_type == 'Peru':
                    self.letter_grade = conversion.america.convert_peru(self.given_grade)
                elif self.scale_type == 'United States':
                    self.letter_grade = conversion.america.convert_united_states(self.given_grade)

                ### ASIA SECTION

                elif self.scale_type == 'Bangladesh':
                    self.letter_grade = conversion.asia.convert_bangladesh(self.given_grade)
                elif self.scale_type == 'China':
                    self.letter_grade = conversion.asia.convert_china(self.given_grade)
                elif self.scale_type == 'China Modified':
                    self.letter_grade_points = conversion.asia.convert_china_modified(self.given_grade)
                    return
                elif self.scale_type == 'Hong Kong':
                    self.letter_grade = conversion.asia.convert_hong_kong(self.given_grade)
                elif self.scale_type == 'Iran':
                    self.letter_grade = conversion.asia.convert_iran(self.given_grade)
                elif self.scale_type == 'Japan':
                    self.letter_grade = conversion.asia.convert_japan(self.given_grade)
                elif self.scale_type == 'Nepal':
                    self.letter_grade = conversion.asia.convert_nepal(self.given_grade)
                elif self.scale_type == 'Nepal Marks':
                    self.letter_grade = conversion.asia.convert_nepal_marks(self.given_grade, self.units)
                elif self.scale_type == 'Philippines':
                    self.letter_grade = conversion.asia.convert_philippines(self.given_grade)
                elif self.scale_type == 'Russia':
                    self.letter_grade = conversion.asia.convert_russia(self.given_grade)
                elif self.scale_type == 'Saudi Arabia':
                    self.letter_grade = conversion.asia.convert_saudi_arabia(self.given_grade)
                elif self.scale_type == 'Singapore':
                    self.letter_grade = conversion.asia.convert_singapore(self.given_grade)
                elif self.scale_type == 'South Korea':
                    self.letter_grade = conversion.asia.convert_south_korea(self.given_grade)
                elif self.scale_type == 'Taiwan':
                    self.letter_grade = conversion.asia.convert_taiwan(self.given_grade)
                elif self.scale_type == 'Vietnam':
                    self.letter_grade = conversion.asia.convert_vietnam(self.given_grade)

                ### EUROPE SECTION

                elif self.scale_type == 'Austria':
                    self.letter_grade = conversion.europe.convert_austria(self.given_grade)
                elif self.scale_type == 'Belgium':
                    self.letter_grade = conversion.europe.convert_belgium(self.given_grade)
                elif self.scale_type == 'Bulgaria':
                    self.letter_grade = conversion.europe.convert_bulgaria(self.given_grade)
                elif self.scale_type == 'Denmark':
                    self.letter_grade = conversion.europe.convert_denmark(self.given_grade)
                elif self.scale_type == 'ECTS':
                    self.letter_grade = conversion.europe.convert_ects(self.given_grade)
                elif self.scale_type == 'France':
                    self.letter_grade = conversion.europe.convert_france(self.given_grade)
                elif self.scale_type == 'Germany':
                    self.letter_grade = conversion.europe.convert_germany(self.given_grade)
                elif self.scale_type == 'Greece':
                    self.letter_grade = conversion.europe.convert_greece(self.given_grade)
                elif self.scale_type == 'Ireland':
                    self.letter_grade = conversion.europe.convert_ireland(self.given_grade)
                elif self.scale_type == 'Italy':
                    self.letter_grade = conversion.europe.convert_italy(self.given_grade)
                ### INDIA SECTION

                elif self.scale_type == 'India 10':
                    self.letter_grade = conversion.india.convert_india_10(self.given_grade)
                elif self.scale_type == 'India 100':
                    self.letter_grade = conversion.india.convert_india_100(self.given_grade)
                elif self.scale_type == 'India Marks':
                    self.letter_grade = conversion.india.convert_india_marks(self.given_grade, self.units)

                ### OCEANIA SECTION

                elif self.scale_type == 'Australia':
                    self.letter_grade = conversion.oceania.convert_australia(self.given_grade)
                elif self.scale_type == 'Australia New South Wales':
                    self.letter_grade = conversion.oceania.convert_australia_new_south_wales(self.given_grade)

                ### INVALID SECTION

                else: # no such grade scale exists
                    invalid_grade_scale_exception = str('Invalid grade scale \'' + self.scale_type
                        + '\' at cell \'C' + str(self.row) + '\'.')
                    raise Exception(invalid_grade_scale_exception)
            except ValueError: # conversion function raised invalid input
                invalid_grade_exception = str('Invalid grade \'' + self.given_grade
                    + '\' for scale type \'' + self.scale_type + '\' at cell \''
                    + utils.excel.col_row_to_cell(self.grade_column, self.row) + '\'.')
                raise Exception(invalid_grade_exception) from None

        # convert United States letter grade to grade points
        try:
            self.letter_grade_points = float(conversion.core.convert_letter_to_4(self.letter_grade))
        # if this fails then there's a problem with the relevant conversion function
        except ValueError:
            invalid_us_letter_grade_exception = str('Converted input grade \''
                + self.letter_grade + '\' from original input grade \'' + self.given_grade
                + '\' for grade scale \'' + self.scale_type + '\' at cell \''
                + utils.excel.col_row_to_cell(self.grade_column, self.row)
                + '\' caused an internal error.\n'
                + 'This usually means that the conversion function for \'' + self.scale_type
                + '\' has a bug in it.\nPlease report this on GitHub or via email.')
            raise Exception(invalid_us_letter_grade_exception) from None
