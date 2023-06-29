#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = pascal[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        pascal.append(row)

    # Additional code
    # Calculate the product of the elements in the last row
    last_row_product = 1
    for num in pascal[-1]:
        last_row_product *= num

    # Calculate the average of the elements in the triangle
    total_elements = sum(len(row) for row in pascal)
    triangle_sum = sum(num for row in pascal for num in row)
    average = triangle_sum / total_elements

    # Append the additional values to the triangle
    pascal.append(["Last Row Product:", last_row_product])
    pascal.append(["Average:", average])

    return pascal


def pascal_triangle(n):
    triangle = []

    if n <= 0:
        return triangle

    # Calculate the maximum number of digits in the triangle
    max_digits = len(str(2**(n-1)))

    triangle.append([1])

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            value = prev_row[j - 1] + prev_row[j]
            row.append(value)

        row.append(1)
        triangle.append(row)

    # Convert triangle elements to strings with padding
    for i, row in enumerate(triangle):
        triangle[i] = [str(num).rjust(max_digits) for num in row]

    return triangle

