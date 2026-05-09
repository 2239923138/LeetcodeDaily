"""
1091. 二进制矩阵中的最短路径

给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：

路径途经的所有单元格的值都是 0 。
路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
畅通路径的长度 是该路径途经的单元格总数。

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] 为 0 或 1"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        n = len(grid)
        if n == 1:
            return 1
        dis = [[-1] * n for _ in range(n)]
        dis[0][0] = 1
        q = deque([(0, 0)])

        while q:
            i, j = q.popleft()
            for x, y in (
                (i, j - 1),
                (i, j + 1),
                (i - 1, j),
                (i + 1, j),
                (i - 1, j - 1),
                (i - 1, j + 1),
                (i + 1, j - 1),
                (i + 1, j + 1),
            ):
                if 0 <= x < n and 0 <= y < n and dis[x][y] < 0 and grid[x][y] == 0:
                    dis[x][y] = dis[i][j] + 1
                    if x == n - 1 and y == n - 1:
                        return dis[x][y]
                    q.append((x, y))
        return -1
