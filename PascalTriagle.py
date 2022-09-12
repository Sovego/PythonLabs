import random
import argparse

parser = argparse.ArgumentParser(description="List size parser")
parser.add_argument("-n", dest="n", required=True, type=int)
args = parser.parse_args()
line = [1]
tmp = []
for i in range(args.n):
    tmp = tmp + [line]
    nxt = []
    for j in range(len(line) - 1):
        nxt = nxt + [line[j] + line[j + 1]]
    line = [1] + nxt + [1]
str_arr = []
for i in range(args.n):
    line = ""
    for j in range(len(tmp[i])):
        line = line + str(tmp[i][j]) + " "
    # print(line)
    str_arr = str_arr + [line]
length_max = len(str_arr[args.n - 1]) - 1
for i in range(args.n):
    s = str_arr[i]
    length = len(s) - 1
    print(" " * ((length_max - length) // 2), end='')
    print(s)
