import argparse


def console_parser():
    """Console Parse"""
    parser = argparse.ArgumentParser(description="File Path")
    parser.add_argument("-i", dest="input", required=True, type=str)
    parser.add_argument("-o", dest="output", required=True, type=str)
    args = parser.parse_args()
    return args


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


def write_matrix(result_matrix, args):
    """Write matrix to file"""
    with open(args.output, "w") as file:
        for iter in result_matrix:
            tmp_str = [str(tmp_iter) for tmp_iter in iter]
            file.write(" ".join(tmp_str) + '\n')


def matrix_validate(first_matrix, second_matrix):
    if len(first_matrix[0]) != len(second_matrix) or len(first_matrix) < len(second_matrix) or len(
            first_matrix[0]) < len(second_matrix[0]):
        raise Exception("Matrix size invalid")


def matrix_convolution(first_matrix, second_matrix):
    """Matrix convolution. Second matrix is a core"""
    shiftX = -1
    shiftY = -1
    row_first_matrix = len(first_matrix[0])
    string_first_matrix = len(first_matrix)
    row_second_matrix = len(second_matrix[0])
    string_second_matrix = len(second_matrix)
    res_matrix = [[0 for i in range(row_first_matrix - row_second_matrix + 1)] for j in
                  range(string_first_matrix - string_second_matrix + 1)]
    for i in range(0, (string_first_matrix - string_second_matrix + 1)):
        shiftY += 1
        shiftX = -1
        for j in range(0, row_first_matrix - row_second_matrix + 1):
            shiftX += 1
            for q in range(i, string_second_matrix + i):
                for k in range(j, row_second_matrix + i):
                    res_matrix[i][j] += (first_matrix[q][k] * second_matrix[q - shiftY][k - shiftX])
    return res_matrix


args = console_parser()
first_matrix, second_matrix = read_matrix(args)
matrix_validate(first_matrix, second_matrix)
res_matrix = matrix_convolution(first_matrix, second_matrix)
write_matrix(res_matrix, args)
