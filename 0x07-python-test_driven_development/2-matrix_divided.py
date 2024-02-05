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
        raise ZeroDivisionError("the message division by zero")
    if not isinstance(div, (int, float)):
       raise TypeError("the message div must be a number")
    new_matrix=[]
    if not all(len(row) == len(matrix[0])for row in matrix):
        raise ValueError("Each row of the matrix must be of the same size")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Each element in the matrix must be a number")

    for row in matrix:
       if not all(isinstance(coulmn, (int, float)) for coulmn in row):
           raise TypeError("Each element in the matrix must be a number")
        new_row=[]
        for coulmn in row:
            new_colm = round(coulmn / div,2)
            new_row.append(new_colm)
        new_matrix.append(new_row)
    return new_matrix
