import copy
MAZE = [[1,  1,  0,  0,  0,  1,  1,  1,  1,  0],
              [0,  1,  0,  1,  1,  1,  0,  1,  0,  0],
              [1,  1,  0,  1,  0,  0,  1,  1,  0,  0],
              [1,  1,  1,  1,  0,  1,  1,  0,  0,  0],
              [1,  0,  0,  0,  1,  1,  0,  0,  1,  0],
              [0,  0,  0,  0,  1,  0,  0,  0,  1,  0],
              [0,  1,  1,  1,  1,  0,  1,  1,  1,  0],
              [0,  1,  0,  0,  1,  1,  1,  0,  1,  0],
              [0,  1,  1,  1,  1,  0,  1,  1,  0,  0],
              [0,  0,  1,  0,  1,  1,  0,  1,  1,  1]]


class Maze(object):
    """
    迷宫问题
    自动寻找一条走出迷宫的路径
    由于初始化迷宫比较复杂，故直接使用现有为10*10的一个迷宫
    """
    def __init__(self):
        """
        初始化迷宫
        """
        # 使用copy模块的deepcopy方法实现重新申请一片空间并复制
        self.maze = copy.deepcopy(MAZE)
        self.findRoad()
        self.mazeRoad = copy.deepcopy(self.maze)
        # 将路径在self.mazeRoad中绘制出来，2表示路径
        for item in self.road:
            self.mazeRoad[item[0]][item[1]] = 2

    def findRoad(self):
        """
        寻找路径
        :return:
        """
        self.road = []

        def test(x, y):
            """
            测试是否可以通过(x,y)点找到出路，将路径保存在self.road里
            :param x: 迷宫路径x轴
            :param y: 迷宫路径y轴
            :return:
            """
            # 如果(9, 9)在路径中说明已经找到出路，直接返回
            if (9, 9) in self.road:
                return
            # 如果(x, y)点不在self.road中，且(x, y)可以通过，则将(x, y)点暂时加入self.road
            if (x, y) not in self.road and self.maze[x][y] == 1:
                self.road.append((x, y))
                try:
                    # 依次测试(x, y+1),(x+1, y),(x, y-1),(x-1, y)点是否可以通过且之前没有经过该点
                    if self.maze[x][y + 1] == 1 and (x, y + 1) not in self.road and y + 1 <= 9:
                        test(x, y + 1)
                    if self.maze[x + 1][y] == 1 and (x + 1, y) not in self.road and x + 1 <= 9:
                        test(x + 1, y)
                    if self.maze[x][y - 1] == 1 and (x, y - 1) not in self.road and y - 1 >= 0:
                        test(x, y - 1)
                    if self.maze[x - 1][y] == 1 and (x - 1, y) not in self.road and x - 1 >= 0:
                        test(x - 1, y)
                    else:
                        # 如果(x, y+1),(x+1, y),(x, y-1),(x-1, y)都不能通过；
                        # 如果此时该点为(9, 9)说明已经走到出路口，返回；
                        # 否则将(x, y)点从路径删除，原路返回上一个坐标
                        if (9, 9) in self.road:
                            return
                        self.road.pop()
                except IndexError:
                    pass
        test(0, 0)

    def __call__(self, *args, **kwargs):
        return self

    def __str__(self):
        """
        字符串格式返回迷宫，以及迷宫出路
        :return:
        """
        smazeRoad = "\n".join([str(i) for i in self.mazeRoad])
        smaze = '\n'.join([str(i) for i in self.maze])
        return f'maze:\n{smaze}\nroad:\n{"->".join([str(i) for i in self.road])}\n{smazeRoad}'
        # return f'''
        # maze:\n
        # {}
        # '''
if __name__ == '__main__':
    print(Maze())
    pass
