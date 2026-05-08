"""
1926. 迷宫中离入口最近的出口

给你一个 m x n 的迷宫矩阵 maze （下标从 0 开始），矩阵中有空格子（用 '.' 表示）和墙（用 '+' 表示）。同时给你迷宫的入口 entrance ，用 entrance = [entrancerow, entrancecol] 表示你一开始所在格子的行和列。

每一步操作，你可以往 上，下，左 或者 右 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。你的目标是找到离 entrance 最近 的出口。出口 的含义是 maze 边界 上的 空格子。entrance 格子 不算 出口。

请你返回从 entrance 到最近出口的最短路径的 步数 ，如果不存在这样的路径，请你返回 -1 。

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] 要么是 '.' ，要么是 '+' 。
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance 一定是空格子。
"""

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dis = [[-1] * n for _ in range(m)]
        sx, sy = entrance[0], entrance[1]
        dis[sx][sy] = 0
        q = deque([(sx, sy)])
        ans = m * n

        while q:
            i, j = q.popleft()
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                if 0 <= x < m and 0 <= y < n and maze[x][y] == "." and dis[x][y] < 0:
                    dis[x][y] = dis[i][j] + 1
                    if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and (
                        x != sx or y != sy
                    ):
                        return dis[x][y]
                    q.append((x, y))
        if ans == m * n:
            return -1
        else:
            return ans
