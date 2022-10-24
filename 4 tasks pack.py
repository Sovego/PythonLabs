import numpy as np

arr = np.random.randint(0, 60, 1000)
counts = np.bincount(arr)
maxsort = counts.argsort()[::-1]
sorted_arr = (maxsort, counts[maxsort])
#print(arr)
print(sorted_arr[1])
