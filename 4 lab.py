import argparse
import random

import numpy as np


def console_parser():
    """Console Parse"""
    parser = argparse.ArgumentParser(description="File Path")
    parser.add_argument("-f", dest="input", required=True, type=str)
    parser.add_argument("-s", dest="input2", required=True, type=str)
    parser.add_argument("-p", dest="p", required=True, type=float)
    args = parser.parse_args()
    return args


def read_matrix(args):
    """Matrix read from file"""
    first_matrix = np.loadtxt(args.input)
    second_matrix = np.loadtxt(args.input2)
    return first_matrix, second_matrix


def choice_element(first_matrix_element, second_matrix_element, choice_array_element):
    if choice_array_element == 1:
        return second_matrix_element
    else:
        return first_matrix_element


def first_method(args, first_matrix, second_matrix):
    "random selection of an element from matrices based on probability"
    second_matrix_p = 1 - args.p
    choice_array = np.random.choice([1, 0], len(first_matrix), True, [args.p, second_matrix_p])
    # 1 element from second matrix
    # 0 element from first matrix
    return map(choice_element, first_matrix.tolist(), second_matrix.tolist(), choice_array)


def choice_element_2(first_matrix_element, second_matrix_element):
    a = random.randint(0, 100)
    first_p, second_p = 0, 0
    if first_matrix_p > second_matrix_p:
        second_p = first_matrix_p
        first_p = second_matrix_p
    else:
        first_p = first_matrix_p
        second_p = second_matrix_p
    if 0 <= a <= first_p:
        if first_p == first_matrix_p:
            return first_matrix_element
        else:
            return second_matrix_element
    elif first_p <= a <= second_p:
        if second_p == second_matrix_p:
            return second_matrix_element
        else:
            return first_matrix_element
    if a >= second_p:
        if second_p == second_matrix_p:
            return second_matrix_element
        else:
            return first_matrix_element


def second_method(first_matrix, second_matrix):
    return map(choice_element_2, first_matrix.tolist(), second_matrix.tolist())


args = console_parser()
first_matrix, second_matrix = read_matrix(args)
second_matrix_p = (1 - args.p) * 100
first_matrix_p = args.p * 100
res = second_method(first_matrix, second_matrix)
print(list(res))
