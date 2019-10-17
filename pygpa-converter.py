import sys

from utils.student import Student
import utils.commandline
import utils.input
import utils.output

args = utils.commandline.argument_parsing()
all_students = []

utils.input.parse_input(args, all_students)

for current_student in all_students:
    current_student.convert_classes()
    current_student.calculate_gpa()

utils.output.write_output(args, all_students)
