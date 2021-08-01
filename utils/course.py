# base imports
from typing import Dict

# relative non-country function imports
import conversion.core
import utils.excel

# relative country function imports
import conversion.africa
import conversion.america
import conversion.asia
import conversion.europe
import conversion.india
import conversion.oceania


class Course:
    """Representation of a course defined via each line of the input CSV file.
    Also contains helper functions to convert the course
    to the United States grade scale.
    """
    def __init__(self, units: str, given_grade: str, scale_type: str,
                 row: int, column: int) -> None:
        """Init a new Course."""
        # input variables taken from CSV file
        self._given_grade = given_grade
        self._scale_type = scale_type

        # variables used for calculating United States equivalent
        self._letter_grade = ""
        self._letter_grade_points = float('-inf')

        # debugging, note that courses take two columns in the input CSV file
        self._row = row
        self._units_column = column
        self._grade_column = column + 1

        # attempt conversion of units to float
        try:
            self._units = float(units)

            if self._units < 0:
                raise ValueError
        except ValueError:  # invalid unit input
            msg = str(
                'Invalid unit input \'' + units + '\' at cell \''
                + utils.excel.col_row_to_cell(self._units_column, self._row)
                + '\'.'
            )
            raise Exception(msg)

    def get_letter_grade_points(self) -> float:
        return self._letter_grade_points

    def get_units(self) -> float:
        return self._units

    def convert_to_letter(self, india_10_dict: Dict[str, Dict[str, str]]
                          ) -> None:
        """Convert given grade to United States letter grade
        using one of the conversion functions defined.
        """
        if self.convert_region_africa():
            pass
        elif self.convert_region_america():
            pass
        elif self.convert_region_asia():
            pass
        elif self.convert_region_europe():
            pass
        elif self.convert_region_india_10(india_10_dict):
            pass
        elif self.convert_region_india():
            pass
        elif self.convert_region_oceania():
            pass
        else:  # no such grade scale exists
            msg = str(
                'Invalid grade scale \'' + self._scale_type
                + '\' at cell \'C' + str(self._row) + '\'.'
            )
            raise Exception(msg)

        # certain scales will have set the grade points already
        if self._letter_grade_points < 0:
            self.convert_letter_grade_to_grade_points()

    def convert_region_africa(self) -> bool:
        """Convert course if the grade is using an African grade scale."""
        try:
            if self._scale_type == 'Nigeria':
                self._letter_grade = conversion.africa.convert_nigeria(
                    self._given_grade
                )
            elif self._scale_type == 'South Africa':
                self._letter_grade = conversion.africa.convert_south_africa(
                    self._given_grade
                )
            elif self._scale_type == 'Uganda':
                self._letter_grade = conversion.africa.convert_uganda(
                    self._given_grade
                )
        except ValueError:  # conversion function raised invalid input
            msg = str(
                'Invalid grade \'' + self._given_grade
                + '\' for scale type \'' + self._scale_type
                + '\' at cell \''
                + utils.excel.col_row_to_cell(self._grade_column, self._row)
                + '\'.'
            )
            raise Exception(msg)

        return True if self._letter_grade != "" else False

    def convert_region_america(self) -> bool:
        """Convert course if the grade is using an American grade scale."""
        try:
            if self._scale_type == '4':
                self._letter_grade_points = conversion.america.convert_4(
                    self._given_grade
                )
                return True
            elif self._scale_type == 'Argentina':
                self._letter_grade = conversion.america.convert_argentina(
                    self._given_grade
                )
            elif self._scale_type == 'Brazil':
                self._letter_grade = conversion.america.convert_brazil(
                    self._given_grade
                )
            elif self._scale_type == 'Brazil Single':
                self._letter_grade = conversion.america.convert_brazil_single(
                    self._given_grade
                )
            elif self._scale_type == 'Brazil Double':
                self._letter_grade = conversion.america.convert_brazil_double(
                    self._given_grade
                )
            elif self._scale_type == 'Canada':
                self._letter_grade = conversion.america.convert_canada(
                    self._given_grade
                )
            elif self._scale_type == 'Canada British Columbia':
                self._letter_grade = (
                    conversion.america.convert_canada_british_columbia(
                        self._given_grade
                    )
                )
            elif self._scale_type == 'Canada Ontario':
                self._letter_grade = conversion.america.convert_canada_ontario(
                    self._given_grade
                )
            elif self._scale_type == 'Mexico':
                self._letter_grade = conversion.america.convert_mexico(
                    self._given_grade
                )
            elif self._scale_type == 'Peru':
                self._letter_grade = conversion.america.convert_peru(
                    self._given_grade
                )
            elif self._scale_type == 'United States':
                self._letter_grade = conversion.america.convert_united_states(
                    self._given_grade
                )
        except ValueError:  # conversion function raised invalid input
            msg = str(
                'Invalid grade \'' + self._given_grade
                + '\' for scale type \'' + self._scale_type
                + '\' at cell \''
                + utils.excel.col_row_to_cell(self._grade_column, self._row)
                + '\'.'
            )
            raise Exception(msg)

        return True if self._letter_grade != "" else False

    def convert_region_asia(self) -> bool:
        """Convert course if the grade is using an Asian grade scale."""
        try:
            if self._scale_type == 'Bangladesh':
                self._letter_grade = conversion.asia.convert_bangladesh(
                    self._given_grade)
            elif self._scale_type == 'China':
                self._letter_grade = conversion.asia.convert_china(
                    self._given_grade)
            elif self._scale_type == 'China Modified':
                self._letter_grade_points = (
                    conversion.asia.convert_china_modified(self._given_grade)
                )
                return True
            elif self._scale_type == 'Hong Kong':
                self._letter_grade = conversion.asia.convert_hong_kong(
                    self._given_grade
                )
            elif self._scale_type == 'Iran':
                self._letter_grade = conversion.asia.convert_iran(
                    self._given_grade
                )
            elif self._scale_type == 'Israel':
                self._letter_grade = conversion.asia.convert_israel(
                    self._given_grade
                )
            elif self._scale_type == 'Japan':
                self._letter_grade = conversion.asia.convert_japan(
                    self._given_grade
                )
            elif self._scale_type == 'Lebanon':
                self._letter_grade = conversion.asia.convert_lebanon(
                    self._given_grade
                )
            elif self._scale_type == 'Nepal':
                self._letter_grade = conversion.asia.convert_nepal(
                    self._given_grade
                )
            elif self._scale_type == 'Nepal Marks':
                self._letter_grade = conversion.asia.convert_nepal_marks(
                    self._given_grade, self._units
                )
            elif self._scale_type == 'Philippines':
                self._letter_grade = conversion.asia.convert_philippines(
                    self._given_grade
                )
            elif self._scale_type == 'Russia':
                self._letter_grade = conversion.asia.convert_russia(
                    self._given_grade
                )
            elif self._scale_type == 'Saudi Arabia':
                self._letter_grade = conversion.asia.convert_saudi_arabia(
                    self._given_grade
                )
            elif self._scale_type == 'Singapore':
                self._letter_grade = conversion.asia.convert_singapore(
                    self._given_grade
                )
            elif self._scale_type == 'South Korea':
                self._letter_grade = conversion.asia.convert_south_korea(
                    self._given_grade
                )
            elif self._scale_type == 'Taiwan':
                self._letter_grade = conversion.asia.convert_taiwan(
                    self._given_grade
                )
            elif self._scale_type == 'Vietnam':
                self._letter_grade = conversion.asia.convert_vietnam(
                    self._given_grade
                )
        except ValueError:  # conversion function raised invalid input
            msg = str(
                'Invalid grade \'' + self._given_grade
                + '\' for scale type \'' + self._scale_type
                + '\' at cell \''
                + utils.excel.col_row_to_cell(self._grade_column, self._row)
                + '\'.'
            )
            raise Exception(msg)

        return True if self._letter_grade != "" else False

    def convert_region_europe(self) -> bool:
        """Convert course if the grade is using an European grade scale."""
        try:
            if self._scale_type == 'Austria':
                self._letter_grade = conversion.europe.convert_austria(
                    self._given_grade
                )
            elif self._scale_type == 'Belgium':
                self._letter_grade = conversion.europe.convert_belgium(
                    self._given_grade
                )
            elif self._scale_type == 'Bulgaria':
                self._letter_grade = conversion.europe.convert_bulgaria(
                    self._given_grade
                )
            elif self._scale_type == 'Denmark':
                self._letter_grade = conversion.europe.convert_denmark(
                    self._given_grade
                )
            elif self._scale_type == 'ECTS':
                self._letter_grade = conversion.europe.convert_ects(
                    self._given_grade
                )
            elif self._scale_type == 'France':
                self._letter_grade = conversion.europe.convert_france(
                    self._given_grade
                )
            elif self._scale_type == 'Germany':
                self._letter_grade = conversion.europe.convert_germany(
                    self._given_grade
                )
            elif self._scale_type == 'Greece':
                self._letter_grade = conversion.europe.convert_greece(
                    self._given_grade
                )
            elif self._scale_type == 'Ireland':
                self._letter_grade = conversion.europe.convert_ireland(
                    self._given_grade
                )
            elif self._scale_type == 'Italy':
                self._letter_grade = conversion.europe.convert_italy(
                    self._given_grade
                )
            elif self._scale_type == 'Netherlands':
                self._letter_grade = conversion.europe.convert_netherlands(
                    self._given_grade
                )
            elif self._scale_type == 'Romania':
                self._letter_grade = conversion.europe.convert_romania(
                    self._given_grade
                )
            elif self._scale_type == 'Spain':
                self._letter_grade = conversion.europe.convert_spain(
                    self._given_grade
                )
            elif self._scale_type == 'Sweden':
                self._letter_grade = conversion.europe.convert_sweden(
                    self._given_grade
                )
            elif self._scale_type == 'Sweden 5':
                self._letter_grade = conversion.europe.convert_sweden_5(
                    self._given_grade
                )
            elif self._scale_type == 'Switzerland':
                self._letter_grade = conversion.europe.convert_switzerland(
                    self._given_grade
                )
            elif self._scale_type == 'United Kingdom':
                self._letter_grade = conversion.europe.convert_united_kingdom(
                    self._given_grade
                )
            elif self._scale_type == 'University of Glasgow':
                self._letter_grade = (
                    conversion.europe.convert_university_of_glasgow(
                        self._given_grade
                    )
                )
        except ValueError:  # conversion function raised invalid input
            msg = str(
                'Invalid grade \'' + self._given_grade
                + '\' for scale type \'' + self._scale_type
                + '\' at cell \''
                + utils.excel.col_row_to_cell(self._grade_column, self._row)
                + '\'.'
            )
            raise Exception(msg)

        return True if self._letter_grade != "" else False

    def convert_region_india(self) -> bool:
        """Convert course if the grade is using an Indian grade scale."""
        try:
            if self._scale_type == 'India 10':
                self._letter_grade = conversion.india.convert_india_10(
                    self._given_grade
                )
            elif self._scale_type == 'India 100':
                self._letter_grade = conversion.india.convert_india_100(
                    self._given_grade
                )
            elif self._scale_type == 'India Marks':
                self._letter_grade = conversion.india.convert_india_marks(
                    self._given_grade, self._units
                )
        except ValueError:  # conversion function raised invalid input
            msg = str(
                'Invalid grade \'' + self._given_grade
                + '\' for scale type \'' + self._scale_type
                + '\' at cell \''
                + utils.excel.col_row_to_cell(self._grade_column, self._row)
                + '\'.'
            )
            raise Exception(msg)

        return True if self._letter_grade != "" else False

    def convert_region_india_10(self, india_10_dict: Dict[str, Dict[str, str]]
                                ) -> bool:
        """Convert course if the grade is using an Indian 10 grade scale."""
        # see if the scale name is in the India 10 dictionary
        if self._scale_type in india_10_dict:
            try:
                converted_number = (india_10_dict[self._scale_type]
                                    [self._given_grade.upper()])
                self._letter_grade = conversion.india.convert_india_10(
                    converted_number
                )
            except KeyError:
                msg = str(
                    'Invalid grade \'' + self._given_grade
                    + '\' for scale type \'' + self._scale_type
                    + '\' at cell \''
                    + utils.excel.col_row_to_cell(self._grade_column,
                                                  self._row) + '\'.'
                )
                raise Exception(msg)
            except ValueError:
                msg = str(
                    'Converted input grade \'' + converted_number
                    + '\' from original input grade \'' + self._given_grade
                    + '\' for grade scale \'' + self._scale_type
                    + '\' at cell \''
                    + utils.excel.col_row_to_cell(self._grade_column,
                                                  self._row)
                    + '\' caused an internal error.\n'
                    + 'This usually means that the entry for \''
                    + self._scale_type
                    + '\' in \'data/india10.csv\' has a mistake in it.\n'
                    + 'Please report this on GitHub or via email.'
                )
                raise Exception(msg)

            return True
        else:
            return False

    def convert_region_oceania(self) -> bool:
        """Convert course if the grade is using an Oceanian grade scale."""
        try:
            if self._scale_type == 'Australia':
                self._letter_grade = conversion.oceania.convert_australia(
                    self._given_grade
                )
            elif self._scale_type == 'Australia New South Wales':
                self._letter_grade = (
                    conversion.oceania.convert_australia_new_south_wales(
                        self._given_grade
                    )
                )
            elif self._scale_type == 'New Zealand':
                self._letter_grade = conversion.oceania.convert_new_zealand(
                    self._given_grade
                )
        except ValueError:  # conversion function raised invalid input
            msg = str(
                'Invalid grade \'' + self._given_grade
                + '\' for scale type \'' + self._scale_type
                + '\' at cell \''
                + utils.excel.col_row_to_cell(self._grade_column, self._row)
                + '\'.'
            )
            raise Exception(msg)

        return True if self._letter_grade != "" else False

    def convert_letter_grade_to_grade_points(self) -> None:
        """Convert an United States letter grade to grade points."""
        try:
            self._letter_grade_points = float(
                conversion.core.convert_letter_to_4(self._letter_grade))
        # if this fails then there's a problem with that conversion function
        except ValueError:
            msg = str(
                'Converted input grade \'' + self._letter_grade
                + '\' from original input grade \'' + self._given_grade
                + '\' for grade scale \'' + self._scale_type + '\' at cell \''
                + utils.excel.col_row_to_cell(self._grade_column, self._row)
                + '\' caused an internal error.\n'
                + 'This usually means that the conversion function for \''
                + self._scale_type
                + '\' has a bug in it.\nPlease report this on GitHub.'
            )
            raise Exception(msg)
