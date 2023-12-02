import argparse
import sys


def console_parser():
    """Console Parse"""
    parser = argparse.ArgumentParser(description="File Path")
    parser.add_argument("-i", dest="input", required=True, type=str)
    parser.add_argument("-o", dest="output", required=True, type=str)
    return parser.parse_args()


def read_matrix(args):
    """Matrix read from file"""
    strs_1 = []
    strs_2 = []
    with open(args.input, "r") as file:
        s = ''
        while s != '\n':
            s = file.readline()
            if s == '\n':
                break
            strs_1.append(s)
        strs_2 = file.readlines()
    first_matrix = [list(map(int, row.split())) for row in strs_1]
    second_matrix = [list(map(int, row.split())) for row in strs_2]
    return first_matrix, second_matrix


def matrix_mult(first_matrix, second_matrix):
    """Matrix multiplication"""
    r = []
    m = []
    for i in range(len(first_matrix)):
        for j in range(len(second_matrix[0])):
            sums = 0
            for k in range(len(second_matrix)):
                sums = sums + (first_matrix[i][k] * second_matrix[k][j])
            r.append(sums)
        m.append(r)
        r = []
    return m


def write_matrix(result_matrix, args):
    """Write matrix to file"""
    with open(args.output, "w") as file:
        for iter in result_matrix:
            tmp_str = [str(tmp_iter) for tmp_iter in iter]
            file.write(" ".join(tmp_str) + '\n')


def matrix_validate(first_matrix, second_matrix):
    if len(first_matrix[0]) != len(second_matrix):
        raise Exception("Matrix size invalid")


if __name__ == "__main__":
    args = console_parser()
    first_matrix, second_matrix = read_matrix(args)
    matrix_validate(first_matrix, second_matrix)
    result_matrix = matrix_mult(first_matrix, second_matrix)
    write_matrix(result_matrix, args)
