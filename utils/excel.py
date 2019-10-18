# based on a post from StackOverflow
# https://stackoverflow.com/questions/23861680/convert-spreadsheet-number-to-column-letter
def column_number_to_string(n):
    string = ''
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string
