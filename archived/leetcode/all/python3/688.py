class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        is_valid = lambda x, y: 0 <= x < n and 0 <= y < n
        directions = (
            (-2, 1),
            (-2, -1),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (1, -2),
            (1, 2),
        )
        dp = [[[0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][0] = 1

        for s in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for x, y in directions:
                        ni, nj = i + x, j + y
                        if is_valid(ni, nj):
                            dp[i][j][s] += dp[ni][nj][s - 1] / 8

        return dp[row][column][k]
