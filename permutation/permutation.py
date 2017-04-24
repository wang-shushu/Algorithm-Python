
def get_permutation(arr=[]):
    """
    获取全排列链表
    :param arr: 原元素集
    :return: 全排列列表
    """
    # 若元素集个中元素个数为1, 则全排列只有一个[[char]]
    if len(arr) <= 1:
        return [arr, ]
    # 若元素集个中元素个数为2, 则全排列有两种[[char1, char2],[char2,char1]]
    elif len(arr) == 2:
        return [arr, arr[::-1]]
    # 若元素集中元素个数为n(n>2), 则取第一个元素依次插入后n-1个元素的全排列中的每一项排列中组合,即为这n个元素的全排列
    else:
        # 取数组第1个元素,存与a0
        a0 = arr[0]
        # 获取后n-1个元素的全排列列表,permutation
        permutation = get_permutation(arr[1:])
        # 保存n个元素的全排列列表
        new_permutation = []
        # 遍历permutation中的每一项,尝试在permutation的每一项中的每一个位置都插入a0元素,组成的排列插入n个元素的全排列列表中
        for item in permutation:
            for i in range(len(item) + 1):
                t = item.copy()
                t.insert(i, a0)
                new_permutation.append(t)
        # 返回n个元素的全排列列表
        return new_permutation
