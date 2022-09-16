import random
import argparse


def bubble_sort():
    """Console Parse"""
    parser = argparse.ArgumentParser(description="List size parser")
    parser.add_argument("-n", dest="n", required=True, type=int)
    args = parser.parse_args()
    """Generate random numbers"""
    a = []
    for x in range(args.n):
        a.append(random.random())
    """Print list"""
    print(a)
    """Sorting"""
    for i in range(args.n):
        for j in range(args.n):
            if a[i] < a[j]:
                c = a[i]
                a[i] = a[j]
                a[j] = c
    """Print sorted list"""
    print(a)


bubble_sort()
