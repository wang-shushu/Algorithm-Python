from factorial import Factorial
from maze import Maze
from sort import BubbleSort
from sort import get_arr
from sort import InsertionSort
from sort import Mergesort
from sort import QuickSort
from sort import SelectionSort
from time import time
from permutation import get_permutation

if __name__ == '__main__':
    arr = get_arr(100)
    t1 = time()
    arr = BubbleSort(arr)
    t2 = time()
    print('BubbleSort: ', t2 - t1)

    t1 = time()
    arr = SelectionSort(arr)
    t2 = time()
    print('SelectionSort: ', t2 - t1)

    arr = get_arr(100)
    t1 = time()
    arr = InsertionSort(arr)
    t2 = time()
    print('InsertionSort: ', t2 - t1)

    arr = get_arr(100)
    t1 = time()
    arr = Mergesort(arr)
    t2 = time()
    print('Mergesort: ', t2 - t1)

    arr = get_arr(100)
    t1 = time()
    arr = QuickSort(arr)
    t2 = time()
    arr = get_arr(100)
    print('QuickSort: ', t2 - t1)

    print(Factorial(500))

    print(Maze())

    arr = [1, 3, 5, 2]
    print(get_permutation(arr=arr))
