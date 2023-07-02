#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list representing Pascal's triangle.

    Raises:
        None.
    """

    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row
    while len(triangle) < n:  # Loop until the desired number of rows is reached
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # The new row always starts with 1
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])  # Compute the values for the new row
        new_row.append(1)  # The new row always ends with 1
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle
