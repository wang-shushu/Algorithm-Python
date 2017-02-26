from time import time
from sort.random_arr import get_arr

arr = get_arr(1000)


def SelectionSort(arr):
    l = arr.__len__()
    for i in range(0, l - 1):
        for j in range(i + 1, l):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
    t1 = time()
    arr = SelectionSort(arr)
    t2 = time()
    print(t2 - t1)
