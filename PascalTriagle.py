import argparse


def console_parser():
    """Console Parse"""
    parser = argparse.ArgumentParser(description="List size parser")
    parser.add_argument("-n", dest="n", required=True, type=int)
    return parser.parse_args()


def pascal_triagle():
    args = console_parser()
    line = [1]
    tmp = []
    """Generating numbers"""
    for _ in range(args.n):
        tmp += [line]
        nxt = [line[j] + line[j + 1] for j in range(len(line) - 1)]
        line = [1] + nxt + [1]
    """Generating strings for output"""
    str_arr = []
    for i in range(args.n):
        line = "".join(f"{str(tmp[i][j])} " for j in range(len(tmp[i])))
        str_arr += [line]
    """Print strings"""
    length_max = len(str_arr[args.n - 1]) - 1
    for i in range(args.n):
        s = str_arr[i]
        length = len(s) - 1
        print(" " * ((length_max - length) // 2), end='')  # multiply the lines by the difference of the longest and the
        # current line, we get the middle from where we need to write
        print(s)


pascal_triagle()
