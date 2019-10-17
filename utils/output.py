import sys

from utils.student import Student

# write results to output file
def write_output(args, all_students):
    # write output to file if defined
    if args.outfile:
        with open(args.outfile, 'w') as outfile:
            for current_student in all_students:
                outfile.write(current_student.output_gpa())
    # else write output to stdout
    else:
        for current_student in all_students:
            sys.stdout.write(current_student.output_gpa())
