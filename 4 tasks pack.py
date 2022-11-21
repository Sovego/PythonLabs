import numpy as np


def first_task():
    arr = np.random.randint(0, 60, 1000)
    counts = np.bincount(arr)
    maxsort = counts.argsort()[::-1]
    sorted_arr = (maxsort, counts[maxsort])
    # print(arr)
    print(sorted_arr[1])


def second_task(h, w):
    array = np.random.randint(0, 255, (h, w, 3), dtype=np.ubyte)
    stacked_array = array[..., 0] * 256 * 256 + array[..., 1] * 256 + array[..., 2]
    n = len(np.unique(stacked_array))
    print(n)



def third_task(x, n):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[n:] - cumsum[:-n]) / float(n)


def four_task():
    array = np.array([[1, 2, 3], [9, 6, 3], [4, 6, 1], [3, 4, 5], [10, 11, 18]])
    a, b, c = np.hsplit(array, 3)
    a = np.where(a < b + c, a, 0)
    b = np.where(b < a + c, b, 0)
    c = np.where(c < a + b, c, 0)
    a = np.where(a < b + c, a, 0)
    b = np.where(b < a + c, b, 0)
    c = np.where(c < a + b, c, 0)
    a = np.where(a < b + c, a, 0)
    b = np.where(b < a + c, b, 0)
    c = np.where(c < a + b, c, 0)
    a = a[(a > 0)]
    b = b[(b > 0)]
    c = c[(c > 0)]
    res = np.column_stack([a, b, c])
    print(res)


second_task(480, 640)