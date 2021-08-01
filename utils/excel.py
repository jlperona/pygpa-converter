def col_num_to_str(n: int) -> str:
    """Convert a column number to its Excel equivalent (A, B, ...).

    Based on a post from StackOverflow.
    https://stackoverflow.com/a/23862195
    """
    string = ''
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string

    return string


def col_row_to_cell(col: int, row: int) -> str:
    """Convert a row/column combination to its Excel equivalent (A1, ...)."""
    col_string = col_num_to_str(col)
    return col_string + str(row)
