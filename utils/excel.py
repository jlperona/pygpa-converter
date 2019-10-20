# based on a post from StackOverflow
# https://stackoverflow.com/questions/23861680/convert-spreadsheet-number-to-column-letter
def col_num_to_str(n):
    string = ''
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

def col_row_to_cell(col, row):
    col_string = col_num_to_str(col)

    return col_string + str(row)
