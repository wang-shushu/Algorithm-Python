from time import time
from sort.random_arr import get_arr

arr = get_arr(10000)


def Mergesort(L):
    def marge(L, b, m, e):
        temp_L = L[b:e + 1]
        l = e - b
        n = m - b
        j = n + 1
        c = i = 0
        while c <= l:
            if i > n:
                L[b + c] = temp_L[j]
                j += 1
                c += 1
            elif j > l:
                L[b + c] = temp_L[i]
                i += 1
                c += 1
            elif temp_L[i] <= temp_L[j]:
                L[b + c] = temp_L[i]
                i += 1
                c += 1
            else:
                L[b + c] = temp_L[j]
                j += 1
                c += 1
        return L

    def m_sort(L, l=0, h=L.__len__()-1):
        if h < l:
            return False
        if h == l:
            return L
        elif h-l == 1:
            if L[l] > L[h]:
                L[l], L[h] = L[h], L[l]
            return L
        else:
            m = (h+l)//2
            m_sort(L, l, m)
            m_sort(L, m+1, h)
            marge(L, l, m, h)
        return L
    return m_sort(L)

if __name__ == '__main__':
    t1 = time()
    arr = Mergesort(arr)
    t2 = time()
    print(t2 - t1)
