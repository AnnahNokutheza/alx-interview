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


def is_pascal_triangle_valid(triangle):
    if not isinstance(triangle, list):
        return False

    for i, row in enumerate(triangle):
        if not isinstance(row, list):
            return False

        if i > 0 and len(row) != len(triangle[i - 1]) + 1:
            return False

        if i > 1:
            prev_row = triangle[i - 1]
            for j in range(1, len(row) - 1):
                if row[j] != prev_row[j - 1] + prev_row[j]:
                    return False

    return True


# Additional test cases
test_triangle = pascal_triangle(5)
print(test_triangle)
print("Is Pascal's triangle valid?", is_pascal_triangle_valid(test_triangle))

test_triangle = pascal_triangle(6)
print(test_triangle)
print("Is Pascal's triangle valid?", is_pascal_triangle_valid(test_triangle))

test_triangle = pascal_triangle(7)
print(test_triangle)
print("Is Pascal's triangle valid?", is_pascal_triangle_valid(test_triangle))

