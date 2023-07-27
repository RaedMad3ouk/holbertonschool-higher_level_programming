#!/usr/bin/python3
"""Function to generate Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle."""

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        cur_row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            cur_row.append(prev_row[j-1] + prev_row[j])
        cur_row.append(1)
        triangle.append(cur_row)
    return triangle
