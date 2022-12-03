from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        r, c = len(matrix), len(matrix[0])
        _prefixes = [[0 for _ in range(c + 1)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                _prefixes[i][j + 1] = _prefixes[i][j] + matrix[i][j]
        self._prefixes = _prefixes

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2 + 1):
            ans += self._prefixes[i][col2 + 1] - self._prefixes[i][col1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
