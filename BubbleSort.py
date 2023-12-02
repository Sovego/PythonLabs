import random
import argparse


def console_parser():
    """Console Parse"""
    parser = argparse.ArgumentParser(description="List size parser")
    parser.add_argument("-n", dest="n", required=True, type=int)
    return parser.parse_args()


def number_generator(args):
    """Generate random numbers"""
    return [random.random() for _ in range(args.n)]


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
