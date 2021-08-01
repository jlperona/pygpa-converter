import csv
import pathlib

from inspect import getsourcefile
from os.path import abspath
from typing import Dict


def parse_india_10_csv(india_10_dict: Dict[str, Dict[str, str]]) -> None:
    """Parse through the india10.csv file in this directory.
    Create a dictionary to serve as a lookup for the scales inside.

    Layout of india_10_dict:
    key = grade scale names
    value = another dictionary

    Layout of sub-dictionaries:
    key = grade
    value = 10 scale value of that grade

    The next lines on pathing are based in part on this StackOverflow post:
    https://stackoverflow.com/a/18489147
    """
    # none checking has to be done to satisfy mypy
    source_path = getsourcefile(lambda: 0)
    if source_path is None:
        msg = "Cannot find source directory path of india10.py."
        raise Exception(msg)
    else:
        script_path = abspath(source_path)

    csv_path = pathlib.Path(script_path).parent / 'india10.csv'

    with open(csv_path) as india_10_csv:
        csvreader = csv.reader(india_10_csv)

        # turn header row into a reference key
        grade_key = next(csvreader)

        # non-header rows
        for row in csvreader:
            # create iterator over the list
            column_number = -1
            row_it = iter(row)

            # get scale name
            column_number += 1
            grade_scale_name = next(row_it)

            # create dictionary for this scale
            current_scale_dict = {}

            # iterate over remaining elements in the row
            for cell in row_it:
                column_number += 1

                # blank, skip
                if not cell:
                    continue

                # possible that there's more than one grade in this cell
                all_grades_in_cell = cell.split(', ')

                # add all grades along with value into the dictionary entry
                for grade in all_grades_in_cell:
                    current_scale_dict[grade] = grade_key[column_number]

            # add finished dictionary to main dictionary
            india_10_dict[grade_scale_name] = current_scale_dict
