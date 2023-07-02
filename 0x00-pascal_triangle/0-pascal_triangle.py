#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Creates a list of lists of integers representing Pascal's triangle

    Parameters:
        n (int): The number of rows of Pascal's triangle to recreate

    Returns:
        list of lists of ints: Representation of Pascal's triangle
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    
    triangle = []
    
    if n <= 0:
        return triangle
    
    previous = [1]
    
    for row_index in range(n):
        rowlist = [1]
        
        for i in range(row_index):
            rowlist.append(previous[i] + previous[i + 1])
        
        rowlist.append(1)
        
        previous = rowlist
        triangle.append(rowlist)
    
    return triangle

