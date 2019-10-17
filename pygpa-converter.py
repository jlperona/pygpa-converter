import argparse
import csv
import sys

from scales import america

class Student:

    def __init__(self, id_primary, id_secondary, scale_type):
        # primary identifier, usually student id
        self.id_primary = id_primary
        # secondary identifier, such as transcript type
        self.id_secondary = id_secondary
        # which grade scale to use for
        self.scale_type = scale_type
        self.courses = []
        self.grade_point_sum = 0
        self.unit_sum = 0
        self.final_gpa = 0

    def add_course(self, course):
        self.courses.append(course)

    def convert_classes(self):
        for current_course in self.courses:
            current_course.convert_to_letter()

    def calculate_gpa(self):
        self.grade_point_sum = 0
        self.unit_sum = 0

        for current_course in self.courses:
            self.grade_point_sum += current_course.letter_grade_points * current_course.units
            self.unit_sum += current_course.units

        self.final_gpa = self.grade_point_sum / self.unit_sum

class Course:

    def __init__(self, units, given_grade, scale_type):
        self.units = float(units)
        self.given_grade = given_grade
        self.scale_type = scale_type
        self.letter_grade = None
        self.letter_grade_points = None

    def convert_to_letter(self):
        if self.scale_type == 'United States':
            self.letter_grade = america.convert_united_states(self.given_grade)

        self.letter_grade_points = float(america.convert_letter_to_4(self.letter_grade))

parser = argparse.ArgumentParser(
    description = 'Take in a CSV file with student transcript data. '
        'Output GPAs on the 4.0 scale for each student.'
)

# mandatory input file
parser.add_argument('infile',
    metavar = 'input.csv',
    help = 'Input CSV file with valid student transcript data.'
)

# optional output file
parser.add_argument('outfile',
    nargs = '?',
    help = 'If specified, write to an output file instead of the console. '
        'Output file will be overwritten.'
)

# no header flag
parser.add_argument('-n',
    '--noheader',
    action = 'store_true',
    help = 'Treat the first line of the file as data rather than skipping it.'
)

args = parser.parse_args()
all_students = []

# open file and begin reading data
with open(args.infile) as infile:
    csvreader = csv.reader(infile)

    # skip header line depending on command line arguments
    if args.noheader == False:
        next(csvreader)

    # for every line in the csv file
    for row in csvreader:
        line_number = csvreader.line_num
        row_it = iter(row)

        # process first three columns with non-course data
        id_primary = next(row_it)
        id_secondary = next(row_it)
        scale_type = next(row_it)

        # create new student
        current_student = Student(id_primary, id_secondary, scale_type)
        all_students.append(current_student)

        # parse remaining columns in sets of two
        while True:
            # read first column of two
            try:
                current_units = next(row_it)

                # if string is empty, then we're at the end of the courses
                if not current_units:
                    break
            # if iterator stops, then we're at the end of the courses
            except StopIteration:
                break

            # read second column of two
            try:
                current_grade = next(row_it)

                # if string is empty, then there's an issue with the data
                if not current_grade:
                    grade_exception = str('Odd number of class data for student '
                        + str(id_primary) + ', line ' + str(line_number) + '.')
                    raise Exception(grade_exception)
            # if iterator stops, then there's an issue with the data
            except StopIteration:
                grade_exception = str('Odd number of class data for student '
                    + str(id_primary) + ', line ' + str(line_number) + '.')
                raise Exception(grade_exception)

            current_student.add_course(Course(current_units, current_grade, scale_type))

for current_student in all_students:
    current_student.convert_classes()
    current_student.calculate_gpa()

# write results to output file
if args.outfile:
    with open(args.outfile, 'w') as outfile:
        for current_student in all_students:
            out_string = str(current_student.id_primary + ' - ' + current_student.id_secondary + ' | GPA: ' + '{:.3f}'.format(current_student.final_gpa) + ', Units: ' + str(current_student.unit_sum) + '\n')
            outfile.write(out_string)
else:
    for current_student in all_students:
        out_string = str(current_student.id_primary + ' - ' + current_student.id_secondary + ' | GPA: ' + '{:.3f}'.format(current_student.final_gpa) + ', Units: ' + str(current_student.unit_sum) + '\n')
        sys.stdout.write(out_string)
