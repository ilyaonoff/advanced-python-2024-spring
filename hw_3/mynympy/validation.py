def check_rows_length(num_columns, values):
    for row in values:
        if len(row) != num_columns:
            return False
    return True


def validate(rows, columns, values):
    if len(values) != rows:
        raise ValueError('Incorrect number of rows')

    if not check_rows_length(columns, values):
        raise ValueError('All rows in matrix must be the same length')

    if rows <= 0 or columns <= 0:
        raise ValueError('Empty matrix')
