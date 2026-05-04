"""
48. 旋转图像

给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i, row in enumerate(matrix):
            for j in range(i + 1, n):
                row[j], matrix[j][i] = matrix[j][i], row[j]
            row.reverse()
