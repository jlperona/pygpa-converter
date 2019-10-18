# Conversion Functions

All conversion functions go here, separated into files based on the continent of the country for that grade scale.
For a list of all conversion functions implemented, see [the main README](../README.md).

## Exception Handling

If a conversion function determines that the input is invalid, it should raise a `ValueError` exception with no message.
The exception handler in `course.py` will inform the user what row and column the exception occurred at.
