from time import time
from sort.random_arr import get_arr

arr = get_arr(100)


def BubbleSort(arr):
    for i in range(0, arr.__len__()):
        for j in range(0, arr.__len__() - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == '__main__':
    time1 = time()
    arr = BubbleSort(arr)
    time2 = time()
    print(time2 - time1)
