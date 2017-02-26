from time import time
from sort.random_arr import get_arr

arr = get_arr(1000000)


def QuickSort(arr):
    def qsort(arr, l, h):
        if h - l <= 1:
            return arr
        elif h - l == 2:
            if arr[0] > arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
            return arr
        else:
            i = l + 1
            j = h - 1
            while i <= j:
                if arr[l] >= arr[i]:
                    i += 1
                    continue
                if arr[l] <= arr[j]:
                    j -= 1
                    continue
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[j] = arr[j], arr[l]
        qsort(arr, l, j)
        qsort(arr, i, h)
        return arr
    return qsort(arr, 0, arr.__len__())
if __name__ == '__main__':
    t1 = time()
    QuickSort(arr)
    t2 = time()
    # print(new_arr)
    print(t2 - t1)
