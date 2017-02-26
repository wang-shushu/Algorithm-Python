from time import time
from sort.random_arr import get_arr

arr = get_arr(10000)


def InsertionSort(arr):
    for i in range(1, arr.__len__()):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

if __name__ == '__main__':
    t1 = time()
    arr = InsertionSort(arr)
    t2 = time()
    print(arr)
    print(t2 - t1)
