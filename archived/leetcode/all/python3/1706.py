from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        is_valid = lambda x, y, dir: 0 <= (y + dir) < n and grid[x][y + dir] == dir

        ans = []

        for i in range(n):
            y = i
            for j in range(m):
                dir = grid[j][y]
                if is_valid(j, y, dir):
                    y += dir
                else:
                    ans.append(-1)
                    break
            else:
                ans.append(y)

        return ans
