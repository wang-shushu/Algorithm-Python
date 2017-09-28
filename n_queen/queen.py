# n-皇后问题的所有解，包括旋转所得解
def nQueen(n):
    results = []
    i = j = 0
    result = [(0, 0)]
    while i < n:
        while j < n:
            if not len(result) == 0 and result[len(result) - 1][0] == i:
                j = j + 1
                break
            if not isInDanger(result, (i, j)):
                result.append((i, j))
            j = j + 1
        if len(result) != i+1 and j == n:
            if len(result) == 0:
                continue
            e = result.pop()
            if e.__eq__((0, n-1)):
                break
            j = e[1] + 1
            i = i - 1
        else:
            i = i + 1
            j = 0
        if len(result) == n:
            results.append(result.copy())
            e = result.pop()
            j = e[1] + 1
            i = i - 1
    return results


# 皇后若在当前位置，是否危险
def isInDanger(root, position) -> bool:
    for i in root:
        if i[0] == position[0] or i[1] == position[1]:
            return True
        if i[0] - position[0] == i[1] - position[1] or i[0] - position[0] == position[1] - i[1]:
            return True
    return False


if __name__ == '__main__':
    # n皇后
    n = 11
    results = nQueen(n)
    # 将结果控制台打印
    for result in results:
        print(f' {n}-Queen result {results.index(result)+1} '.center(30, '-'))
        for i in range(n):
            for j in range(n):
                if i == result[i][0] and j == result[i][1]:
                    # 表示当前位置为皇后位置
                    print('Q', end=' ')
                else:
                    # 表示当前位置为空
                    print('+', end=' ')
            print()
