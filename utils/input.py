# base imports
import argparse
import csv

from typing import List

# relative imports
from utils.student import Student
from utils.course import Course


def parse_input(args: argparse.Namespace,
                all_students: List['Student']) -> None:
    """Read input file and place parsed data in all_students."""
    # open file and begin reading data
    with open(args.infile) as infile:
        csvreader = csv.reader(infile)

        # skip header line depending on command line arguments
        if args.noheader is False:
            next(csvreader)

        # for every line in the csv file
        for row in csvreader:
            line_number = csvreader.line_num

            row_it = iter(row)
            column_number = -1

            # process first three columns with non-course data
            try:
                column_number += 1
                id_primary = next(row_it)

                column_number += 1
                id_secondary = next(row_it)

                column_number += 1
                scale_type = next(row_it)
            except StopIteration:
                msg = str('Not enough data input on row '
                          + str(line_number) + '.')
                raise Exception(msg)

            # create new student
            current_student = Student(id_primary, id_secondary,
                                      scale_type, line_number)
            all_students.append(current_student)

            # parse remaining columns in sets of two
            while True:
                # read first column of two
                try:
                    column_number += 1
                    current_units = next(row_it)

                    # if string is empty, then we're at the end of the courses
                    if not current_units:
                        break
                # if iterator stops, then we're at the end of the courses
                except StopIteration:
                    break

                # read second column of two
                try:
                    column_number += 1
                    current_grade = next(row_it)

                    # if string is empty, then there's an issue with the data
                    if not current_grade:
                        msg = str('Odd number of class data for student '
                                  + str(id_primary) + ', row '
                                  + str(line_number) + '.')
                        raise Exception(msg)
                # if iterator stops, then there's an issue with the data
                except StopIteration:
                    msg = str('Odd number of class data for student '
                              + str(id_primary) + ', row '
                              + str(line_number) + '.')
                    raise Exception(msg)

                current_student.add_course(
                    Course(current_units, current_grade,
                           scale_type, line_number, column_number)
                )

            # if no courses added, then no courses existed in the input
            if len(current_student._courses) == 0:
                msg = str('No courses input for student ' + str(id_primary)
                          + ', row ' + str(line_number) + '.')
                raise Exception(msg)
