# pygpa-converter

A Python program to take in student transcript data from other countries via CSV format, and convert them to GPAs in the United States' 4.0 grading scale.
This is a Python rewrite of [jlperona/gpa-converter](https://github.com/jlperona/gpa-converter).

## Python

### Version

Python 3.6 or later is required due to a usage of `open()` with `Path` from `pathlib`.

### Dependencies

This script does not use any packages that aren't provided in base Python as of Python 3.4.

## Use

### Command Line

    python3 pygpa-converter.py [-h] [-n] input.csv [outfile]

Use `-n` or `--no-header` if your data does not have a header row.
Output will be written to `stdout` if `outfile` is not specified.
If specified, the file will be overwritten with the final GPA data.
For more help with command line arguments, run the program with `-h`.

### Input CSV File

The format of the input CSV file should look like this:

    Header row will be ignored.
    Student 1 Primary Identifier, Secondary Identifier, Grade Scale, Class 1 Units, Class 1 Grade, Class 2 Units, Class 2 Grade, ...
    Student 2 Primary Identifier, Secondary Identifier, Grade Scale, ...
    ...

The primary and secondary identifiers can be anything.
I typically use the primary identifier for ID numbers, and the secondary identifier to indicate multiple transcripts for the same student.

## Grade Scales

All grade scale conversions are credited to [Scholaro](https://www.scholaro.com/pro/Countries), previously *ForeignCredits*.
The appropriate string below goes in the *Grade Scale* column for each student.

For the list of grade scales that have been implemented, see the [conversion README](./conversion/README.md).

## Motivation

### Why Python?

Originally I wrote [this script in C++](https://github.com/jlperona/gpa-converter).
I didn't know Python very well at the time, but I knew C++.
That program was *okay*, but it wasn't great.
The base of the program worked just fine, but eventually I decided I wanted to implement overlay scales for the `India 10` grade scale (see the section above).
This would have taken a significant amount of work to do in C++, but is fairly easy in Python.

As with any rewrite, eventually I "bit the bullet" and decided to go forward with the rewrite.
I'm glad that I did so, as the code is far more readable and less verbose in Python.
Error handling and providing feedback to the end-user on what went wrong is so much better here, as well.

### Background

This was designed for personal use.
Some sort of conversion needs to be done for non-US GPAs in order to be able to make fair comparisons between students attending schools from different countries.
In the past, what was done at my workplace was:

1. Take student transcript data
2. Input it into a web app
3. Calculate the student's GPA
4. Print out the web app page

This seemed inefficient.
This app helps speed the process along.

### Benefits

* Data entry is easier
    * It's much easier to use your favorite spreadsheet editor to enter data than using a web app
* Data is saved to CSV
    * Parsing is easy
    * Can be uploaded to a cloud storage website, rather than printing them out
* Open source
    * Code easily checked for errors rather than relying on the programming of a web app

### Drawbacks

* Data is saved to CSV
    * Not the most elegant format to use
* Doesn't fix the time spent on data entry
    * It only helps speed it up
    * Programmatically determining grades and credit hours would require OCR

## Future

This script can be expanded with new grade scales.
To see how to add a new scale, see the [conversion README](./conversion/README.md).

### Pull Requests

If you have any that you would like to add, feel free to make a [pull request](https://github.com/jlperona/pygpa-converter/pulls).
