#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for x in line:
            if x != line[-1]:
                print("{:d}".format(x), end=" ")
            else:
                print("{:d}".format(x), end=" ")
        print()
