#
# @lc app=leetcode.cn id=1001 lang=python3
#
# [1001] 网格照明
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def gridIllumination(
        self, n: int, lamps: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        points = set()
        row, col, diag, anti_diag = Counter(), Counter(), Counter(), Counter()
        for r, c in lamps:
            if (r, c) not in points:
                points.add((r, c))
                row[r] += 1
                col[c] += 1
                diag[r - c] += 1
                anti_diag[r + c] += 1
        ans = []
        for r, c in queries:
            if row[r] or col[c] or diag[r - c] or anti_diag[r + c]:
                ans.append(1)
            else:
                ans.append(0)
            for x in range(r - 1, r + 2):
                for y in range(c - 1, c + 2):
                    if 0 <= x < n and 0 <= y < n and (x, y) in points:
                        row[x] -= 1
                        col[y] -= 1
                        diag[x - y] -= 1
                        anti_diag[x + y] -= 1
                        points.remove((x, y))
        return ans


# @lc code=end
