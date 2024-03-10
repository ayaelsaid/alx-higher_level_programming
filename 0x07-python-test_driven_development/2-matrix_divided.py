#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
     a function that divides all elements of a matrix.
     Args:
        matrix: list of lists
        div: an operation
    Return:
        new_marrix
        """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    new_matrix = []

    if not all(len(row) == len(matrix[0])for row in matrix):
        raise ValueError("Each row of the matrix must have the same size")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not all(isinstance(coulmn, (int, float)) for coulmn in row):
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
    for row in matrix:
        new_row = []
        for coulmn in row:
            new_colm = round(coulmn / div, 2)
            new_row.append(new_colm)
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
