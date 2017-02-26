from random import randint


def get_arr(n, min_of_randint=-10000, max_of_randint=10000):
    """
    :param n:所需的随机数个数
    :param min_of_randint: 随机数的最小值，默认值为10000
    :param max_of_randint: 随机数的最大值，默认值为10000
    :return: 随机产生的长度为n的数组
    """
    arr = []
    for i in range(0, n+1):
        arr.append(randint(min_of_randint, max_of_randint))
    return arr

