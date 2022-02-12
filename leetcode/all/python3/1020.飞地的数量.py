from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def fs(x, y):
            grid[x][y] = 0
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                n_x, n_y = x + i, y + j
                if 0 <= n_x < m and 0 <= n_y < n and grid[n_x][n_y] == 1:
                    fs(n_x, n_y)

        for i in range(m):
            if grid[i][0] == 1:
                fs(i, 0)
            if grid[i][n - 1] == 1:
                fs(i, n - 1)
        for j in range(n):
            if grid[0][j] == 1:
                fs(0, j)
            if grid[m - 1][j] == 1:
                fs(m - 1, j)

        return sum(j == 1 for i in grid for j in i)
