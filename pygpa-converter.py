# base package imports
import sys

# relative imports
import data.india10
from utils.student import Student
import utils.commandline
import utils.input
import utils.output

# command line argument processing
args = utils.commandline.argument_parsing()
all_students = []

# input file processing
utils.input.parse_input(args, all_students)

india_10_dict = {}
data.india10.parse_india_10_csv(india_10_dict)

# data processing
for current_student in all_students:
    current_student.convert_classes()
    current_student.calculate_gpa()

# output file processing
utils.output.write_output(args, all_students)
