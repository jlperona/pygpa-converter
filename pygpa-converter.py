import argparse
import csv
import sys

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

# open file and begin reading data
with open(args.infile) as infile:
    csvreader = csv.reader(infile)

    if args.noheader == False:
        next(csvreader)

    for row in csvreader:
        print(row)
        # (TO DO) Read through CSV file and build student objects

# (TO DO) For each student, convert classes and calculate GPA

# write results to output file

if args.outfile:
    with open(args.outfile, 'w') as outfile:
        outfile.write('Write to file\n')
else:
    sys.stdout.write('Write to stdout\n')
    # (TO DO) Write converted output to file
