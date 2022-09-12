import random
import argparse

parser = argparse.ArgumentParser(description="List size parser")
parser.add_argument("-n", dest="n", required=True, type=int)

args = parser.parse_args()
a = []
for x in range(0, args.n):
    a.append(random.random())
print(a)
for i in range(0, args.n):
    for j in range(0, args.n):
        if a[i] < a[j]:
            c = a[i]
            a[i] = a[j]
            a[j] = c
print(a)
