import random
import argparse


def console_parser():
    """Console Parse"""
    parser = argparse.ArgumentParser(description="List size parser")
    parser.add_argument("-n", dest="n", required=True, type=int)
    args = parser.parse_args()
    return args


def number_generator(args):
    """Generate random numbers"""
    a = []
    for x in range(args.n):
        a.append(random.random())
    return a


def bubble_sort():
    args = console_parser()
    a = number_generator(args)
    """Print list"""
    print(a)
    """Sorting"""
    for i in range(args.n-1):
        for j in range(args.n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]
                #c = a[i]
                #a[i] = a[j]
                #a[j] = c
    """Print sorted list"""
    print(a)


bubble_sort()
