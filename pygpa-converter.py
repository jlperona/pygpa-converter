# base package imports
import sys

# relative imports
from utils.student import Student
import utils.commandline
import utils.input
import utils.output

# command line argument processing
args = utils.commandline.argument_parsing()
all_students = []

# input file processing
utils.input.parse_input(args, all_students)

# data processing
for current_student in all_students:
    current_student.convert_classes()
    current_student.calculate_gpa()

# output file processing
utils.output.write_output(args, all_students)
