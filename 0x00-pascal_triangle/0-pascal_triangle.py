#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    mat = list(range(n))
    mat[0] = [1]
    mat[1] = [1, 1]

    if n <= 0:
        return []
    if n == 1:
        return mat

    for i in range(2, n):
        mat[i] = [
            mat[i - 1][j] + mat[i - 1][j + 1]
            for j in range(len(mat[i - 1]) - 1)
        ]
        mat[i] = [1] + mat[i] + [1]

    # Additional code
    # Calculate the product of the elements in the last row
    last_row_product = 1
    for num in mat[-1]:
        last_row_product *= num

    # Calculate the average of the elements in the triangle
    total_elements = sum(len(row) for row in mat)
    triangle_sum = sum(num for row in mat for num in row)
    average = triangle_sum / total_elements

    # Append the additional values to the triangle
    mat.append(["Last Row Product:", last_row_product])
    mat.append(["Average:", average])

    return mat


