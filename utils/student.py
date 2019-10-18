# representation of a student defined via each line of the input csv file
class Student:

    def __init__(self, id_primary, id_secondary, scale_type, row):
        # input variables taken from CSV file
        self.id_primary = id_primary
        self.id_secondary = id_secondary
        self.scale_type = scale_type

        # list of courses associated with student
        self.courses = []

        # variables used for calculating final gpa
        self.grade_point_sum = None
        self.unit_sum = None
        self.final_gpa = None

        # debugging
        self.row = row

    # push course into student's list of courses
    def add_course(self, course):
        self.courses.append(course)

    # convert all courses in the student's list to United States equivalent
    def convert_classes(self):
        for current_course in self.courses:
            current_course.convert_to_letter()

    # calculate final gpa from converted courses
    def calculate_gpa(self):
        # gpa formula (c = class)
        # numerator = c1 units * c1 grade points + c2 units * c2 grade points + ...
        # denominator = c1 units + c2 units + ...
        # final gpa = numerator / denominator
        self.grade_point_sum = 0
        self.unit_sum = 0

        for current_course in self.courses:
            self.grade_point_sum += current_course.letter_grade_points * current_course.units
            self.unit_sum += current_course.units

        self.final_gpa = self.grade_point_sum / self.unit_sum

    # string containing final gpa
    def output_gpa(self):
        return str(self.id_primary + ' - ' + self.id_secondary + ' (' + self.scale_type + ') | GPA: ' +
            '{:.3f}'.format(self.final_gpa) + ', Units: ' + str(self.unit_sum) + '\n')
