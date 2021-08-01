# base imports
from typing import Dict, List

# relative imports
from utils.course import Course


class Student:
    """Representation of a student.
    Each student defined via each line of the input CSV file.
    """
    def __init__(self, id_primary: str, id_secondary: str,
                 scale_type: str, row: int) -> None:
        """Init a new Student."""
        # input variables taken from CSV file
        self._id_primary = id_primary
        self._id_secondary = id_secondary
        self._scale_type = scale_type

        # list of courses associated with student
        self._courses: List['Course'] = []

        # variables used for calculating final gpa
        self._grade_point_sum = float('-inf')
        self._unit_sum = float('-inf')
        self._final_gpa = float('-inf')

        # debugging
        self._row = row

    def add_course(self, course: 'Course') -> None:
        """Push a course into the student's list of courses."""
        self._courses.append(course)

    def get_number_of_courses(self) -> int:
        """Get the number of courses this student currently has."""
        return len(self._courses)

    def convert_classes(self,
                        india_10_dict: Dict[str, Dict[str, str]]) -> None:
        """Convert all courses in the student's list to the US equivalent."""
        for current_course in self._courses:
            current_course.convert_to_letter(india_10_dict)

    def calculate_gpa(self) -> None:
        """Calculate final GPA from converted courses.

        GPA Formula (c = class)

        numerator = c1 units * c1 grade points + c2 units * c2 points + ...
        denominator = c1 units + c2 units + ...
        final gpa = numerator / denominator
        """
        self._grade_point_sum = 0
        self._unit_sum = 0

        for current_course in self._courses:
            self._grade_point_sum += (current_course.get_letter_grade_points()
                                      * current_course.get_units())
            self._unit_sum += current_course.get_units()

        self._final_gpa = self._grade_point_sum / self._unit_sum

    def output_gpa(self) -> str:
        """Return a string containing this student's final GPA."""
        return str(self._id_primary + ' - ' + self._id_secondary + ' ('
                   + self._scale_type + ') | GPA: '
                   + '{:.3f}'.format(self._final_gpa) + ', Units: '
                   + str(self._unit_sum) + '\n'
                   )
