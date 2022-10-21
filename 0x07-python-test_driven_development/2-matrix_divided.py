#!/usr/bin/python3
"""
This module is composed by a function that divides a matrix.

"""


def matrix_divided(matrix, div):
    """ Function that divides a matrix.
    Args:
        matrix: a list of integer/float.
        div: a divisor of the matrix number.
    Raise:
         TypeError: if not a matrix (list of lists) of integers/floats.
         TypeError: if each row of the matrix is not the same size.
         TypeError: if div is not a number.
         ZeroDivisionError: if div is equal to zero.
    Returns:
           A new matrix with the result of the division.
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or not isinstance(matrix, list):
        raise TypeError("It must be a matrix (list of lists) of int/floats")
    len_e = 0
    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError("It must be a matrix of int/floats")
        if len_e != 0 and len(elems) != len_e:
            raise TypeError("Each row of the matrix must have the same size")
        for num in elems:
            if not type(num) in (int, float):
                raise TypeError("It must be a matrix of int/floats")
        len_e = len(elems)
    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
