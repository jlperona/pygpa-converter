# base imports
import argparse


def argument_parsing() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Take in a CSV file with student transcript data. '
                    'Output GPAs on the 4.0 scale for each student.'
    )

    # mandatory input file
    parser.add_argument(
        'infile',
        metavar='input.csv',
        help='Input CSV file with valid student transcript data.'
    )

    # optional output file
    parser.add_argument(
        'outfile',
        nargs='?',
        help='If specified, write to an output file instead of the console. '
             'Output file will be overwritten.'
    )

    # no header flag
    parser.add_argument(
        '-n',
        '--noheader',
        action='store_true',
        help='Treat the first row of the file as data rather than skipping it.'
    )

    return parser.parse_args()
