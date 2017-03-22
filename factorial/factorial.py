
class Factorial(object):
    """
    求x的阶乘
    """
    _d = 10
    results = []

    def __init__(self, x):
        """
        初始化
        :param x:需要求阶乘的数
        """
        self.results = [1]
        for i in range(1, x + 1):
            self.results = self.mul(self.results, i)
        self.results = self.results[::-1]

    def mul(self, arr, y):
        """
        保存与数组中的数与整数的乘法运算，结果保存在数组中
        :param arr: 被乘数（数组）
        :param y: 乘数（整数）
        :return: 数组
        """
        results = arr
        remainders = []
        remainders.append(0)
        for i in range(0, len(results)):
            results[i] *= y
            if results[i] >= self._d:
                temp = results[i] // self._d**10
                remainders.append(temp)
                temp = results[i] % self._d**10
                results[i] = temp
            else:
                remainders.append(0)

        for i in range(0, len(remainders)):
            try:
                results[i] += remainders[i]
            except IndexError:
                if remainders[i] != 0:
                    results.append(remainders[i])
        del remainders
        return results

    def division(self, x):
        """
        讲一个整数保存在数组中
        :param x: 需要转换的值
        :return: 转换后保存x的数组
        """
        results = []
        while True:
            if x >= self._d**10:
                results.append(x % self._d**10)
                x //= self._d**10
                continue
            results.append(x)
            del x
            return results

    def __str__(self):
        """
        格式化输出
        :return:
        """
        def formats(s):
            return str(s).rjust(self._d, '0')
        result = str(self.results[0])
        for i in range(1, len(self.results)):
            temp = self.results[i]
            result += formats(temp)
        return result

    def __call__(self, *args, **kwargs):
        return self
        pass

if __name__ == '__main__':
    print(Factorial(100))
