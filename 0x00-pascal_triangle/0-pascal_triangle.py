#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    # Additional code
    # Calculate the product of the elements in the last row
    last_row_product = 1
    for num in triangle[-1]:
        last_row_product *= num

    # Calculate the average of the elements in the triangle
    total_elements = sum(len(row) for row in triangle)
    triangle_sum = sum(num for row in triangle for num in row)
    average = triangle_sum / total_elements

    # Append the additional values to the triangle
    triangle.append(["Last Row Product:", last_row_product])
    triangle.append(["Average:", average])

    return triangle

