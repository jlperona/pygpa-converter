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

The following grade scales have been implemented.

### Africa

* `Nigeria`
    * Most common scale in Nigeria.
    * Letter grades.
* `South Africa`
    * Most common scale in South Africa.
    * Grades range from 0 - 100.
* `Uganda`
    * 9 point scale in Uganda.
    * Grades range from 1 - 9.

### America

* `4`
    * 4.0 scale used in the United States.
    * Also used in Brazil, Canada, China, Hong Kong, Japan, and Taiwan.
        * Assumes that A+ is equivalent to 4.0.
        * Can also convert the 4.3 scale where A+ is equivalent to 4.3.
    * Numerical grades. For letter grades, see `United States` below.
* `Argentina`
    * Most common grade scale in Argentina.
    * Grades range from 0 - 10.
* `Brazil`
    * Most common grade scale in Brazil.
    * Grades range from 0 - 100.
* `Brazil Single`
    * Single letter grade scale used in Brazil.
    * Single letter grades.
* `Brazil Double`
    * Double letter grade scale used in Brazil.
    * Double letter grades.
* `Canada`
    * Alias of `United States`.
    * See `United States` below for more information.
    * Letter grades.
* `Canada British Columbia`
    * Most common scale in British Columbia, Canada.
    * Grades range from 0 - 100.
* `Canada Ontario`
    * Most common scale in Ontario, Canada.
    * Grades range from 0 - 100.
* `Mexico`
    * 10 point scale with 6 as passing.
    * Grades range from 0 - 10.
* `Peru`
    * Most common scale in Peru.
    * Grades range from 0 - 20.
* `United States`
    * 4.0 scale used in the United States.
    * Also used in Brazil, Canada, China, Hong Kong, Japan, and Taiwan.
        * Assumes that A+ is equivalent to 4.0.
        * Can also convert the 4.3 scale where A+ is equivalent to 4.3.
    * Letter grades. For numerical grades, see `4.0` above.

### Asia (excluding India)

* `Bangladesh`
    * Most common scale in Bangladesh.
    * Grades range from 0 - 100.
* `China`
    * Most common scale in China.
    * Grades range from 0 - 100.
* `China Modified`
    * The Chinese conversion scale has been modified to use the one in use at UC Davis.
    * Grades range from 0 - 100.
* `Hong Kong`
    * Alias of `United States`.
    * See `United States` above for more information.
    * Letter grades.
* `Iran`
    * Most common scale in Iran.
    * Grades range from 0 - 20.
* `Israel`
    * Most common scale in Israel.
    * Grades range from 0 - 100.
* `Japan`
    * Number grades in Japan.
    * Grades range from 0 - 100.
* `Lebanon`
    * University scale in Lebanon.
    * Grades range from 0 - 100.
* `Nepal`
    * Most common scale in Nepal.
    * Grades range from 0 - 100.
* `Nepal Marks`
    * Scale for certain universities in Nepal.
        * Useful when the university only uses marks and does not provide an equivalent to units.
        * Uses the same scale as `Nepal`.
        * Calculates the percentage based on the units input being equal to 100%.
        * For example, 200 units with a grade of 150 is equal to 150/200 = 75%.
    * Grades range from 0 to the number of marks input.
* `Philippines`
    * Most common scale in the Philippines.
    * Grades range from 1 - 5.
* `Russia`
    * Most common scale in Russia.
    * Letter grades.
    * Either the full translated grade (`Excellent`, etc.) or the first letter of the translated grade (`E`, etc.) is accepted.
* `Saudi Arabia`
    * University-level scale in Saudi Arabia.
    * Letter grades.
* `Singapore`
    * Most common scale in Singapore.
    * Letter grades.
* `South Korea`
    * Post-secondary scale in South Korea.
    * Letter grades.
* `Taiwan`
    * Tertiary scale in Taiwan.
    * Grades range from 0 - 100.
* `Vietnam`
    * Most common scale in Vietnam.
    * Grades range from 0 - 10.

### Europe

* `Austria`
    * Most common scale in Austria.
    * Grades range from 1 - 5.
* `Belgium`
    * Flemish scale in Belgium.
    * Grades range from 0 - 20.
* `Bulgaria`
    * Most common scale in Bulgaria.
    * Grades range from 2 - 6.
* `Denmark`
    * Most common scale in Denmark.
    * Grades range from 0 - 12 or -3.
* `ECTS`
    * European Credit Transfer System scale.
    * Letter grades.
* `France`
    * Most common scale in France.
    * Grades range from 0 - 20.
* `Germany`
    * Tertiary scale in Germany.
    * Grades range from 1 - 6.
* `Greece`
    * Most common scale in Greece.
    * Grades range from 0 - 10.
* `Ireland`
    * Most common scale in Ireland.
    * Grades range from 0 - 100.
* `Italy`
    * Most common scale in Italy.
    * Grades range from 0 - 30.
* `Netherlands`
    * Most common scale in the Netherlands.
    * Grades range from 1 - 10.
* `Romania`
    * Most common scale in Romania.
    * Grades range from 0 - 10.
* `Spain`
    * Most common scale in Spain.
    * Grades range from 0 - 10.
* `Sweden`
    * Most common scale in Sweden.
    * Letter grades.
* `Sweden 5`
    * Five point scale in Sweden.
    * Grades range from 1 - 5.
    * For letter grades, use `Sweden` above.
* `Switzerland`
    * Most common scale in Switzerland.
    * Grades range from 0 - 6.
* `United Kingdom`
    * Most common scale in the United Kingdom.
    * Grades range from 0 - 100.
* `University of Glasgow`
    * Scale specifically for the University of Glasgow in Scotland.
    * Letter grades.

### India

* `India 10`
    * UGC 10 point scale in India.
    * Grades range from 0 - 10.
    * *See below for special information about this scale.*
* `India 100`
    * 100 point scale in India.
    * Grades range from 0 - 100.
* `India Marks`
    * Scale for certain universities in India.
        * Useful when the university only uses marks and does not provide an equivalent to units.
        * Uses the same scale as `India 100`.
        * Calculates the percentage based on the units input being equal to 100%.
        * For example, 200 units with a grade of 150 is equal to 150/200 = 75%.
    * Grades range from 0 to the number of marks input.

### Oceania

* `Australia`
    * Post-secondary scale in Australia.
    * Letter grades.
* `Australia New South Wales`
    * Most common scale in New South Wales, Australia.
    * Grades range from 0 - 100.
    * For letter grades, use `Australia` above.
* `New Zealand`
    * Post-secondary scale in New Zealand.
    * Letter grades.

### Indian 10 Point Scale

#### Background

The Indian 10 point scale (`India 10` above) is somewhat unique, in that many universities use the 10 point scale, but add their own letter grade values.
Typing in letter grades is easier than doing the conversion manually, so there are grade scales that support each university's specific letter grades.

#### Code

The CSV file [`data/india10.csv`](./data/india10.csv) contains the translations from letter grades to the 10 point scale for universities that I've encountered.
[`data/india10.py`](./data/india10.py) builds a dictionary of dictionaries for each grade scale on every row of that file.
Adding new universities is as simple as adding a new line to the CSV file.

#### Usage

All universities that are supported are listed in the first column of `data/india10.csv`.
The appropriate string from that column goes in the *Grade Scale* column for each student.
If you want to use numerical grades instead of the letter grades, use the `India 10` scale instead.

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

I intend to add more grade scales as necessary for my job.

### Pull Requests

If you have any that you would like to add, feel free to make a [pull request](https://github.com/jlperona/pygpa-converter/pulls).

### Adding a New Scale

#### Regular Scales

For examples of commits that add regular grade scales (ones that use a normal conversion function), see the following examples:

* [*Brazil Single*](https://github.com/jlperona/pygpa-converter/commit/6711dc104f185cc03e64ba18f131062bf6e34245) for letter grade scales
* [*Canada British Columbia*](https://github.com/jlperona/pygpa-converter/commit/fe1728b14789527e5da4c834c18670a55f184460) for number grade scales

Below are the steps to add a new scale:

1. Create the function in the appropriate `continent.py` file.
    * Function names should be in the form of `convert_country()`.
    * Copying the style of other functions is encouraged.
2. Update `convert_to_letter()` in the `Course` class to add the new scale.
3. Update **README.md** (this document) to list the new scale.

#### India 10 Overlays

For an example of a commit that adds an overlay scale for `India 10`, see the commit for [*PES University*](https://github.com/jlperona/pygpa-converter/commit/6a1bb9cd4281eec1afbeb692804a61572faa1b5f).

Below are the steps to add a new `India 10` overlay scale:

1. Add a new row to [`data/india10.csv`](./data/india10.csv).
2. In the first column, add the university name.
3. For each grade to add:
    1. Find the column with the corresponding number grade.
        * If the column does not exist, insert a new column with the first row being the number grade.
    2. Add the grade to that column in the same row.
    3. If a grade already exists there, separate them with a comma and a space ", ".
