#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Creates a list of lists of integers representing Pascal's triangle.

    Parameters:
        n (int):
            The number of rows of Pascal's triangle to recreate.

    Returns:
        list of lists of ints:
            Representation of Pascal's triangle.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    triangle = []

    if n <= 0:
        return triangle

    previous = [1]

    for row_index in range(n):
        rowlist = []

        if row_index == 0:
            rowlist = [1]
        else:
            for i in range(row_index + 1):
                if i == 0:
                    rowlist.append(0 + previous[i])
                elif i == row_index:
                    rowlist.append(previous[i - 1] + 0)
                else:
                    rowlist.append(previous[i - 1] + previous[i])

        previous = rowlist
        triangle.append(rowlist)

    return triangle
