# base imports
import argparse
import sys

from typing import List

# relative imports
from utils.student import Student


def write_output(args: argparse.Namespace,
                 all_students: List['Student']) -> None:
    """Write results to output file."""
    # write output to file if defined
    if args.outfile:
        with open(args.outfile, 'w') as outfile:
            for current_student in all_students:
                outfile.write(current_student.output_gpa())
    else:  # else write output to stdout
        for current_student in all_students:
            sys.stdout.write(current_student.output_gpa())
