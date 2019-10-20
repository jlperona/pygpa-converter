# base package imports
import sys

# relative imports
import data.india10
import utils.commandline
import utils.input
import utils.output
from utils.student import Student

# command line argument processing
args = utils.commandline.argument_parsing()

# input file processing
all_students = []
utils.input.parse_input(args, all_students)

# india10.csv processing
india_10_dict = {}
data.india10.parse_india_10_csv(india_10_dict)

# data processing
for current_student in all_students:
    current_student.convert_classes(india_10_dict)
    current_student.calculate_gpa()

# output file processing
utils.output.write_output(args, all_students)
