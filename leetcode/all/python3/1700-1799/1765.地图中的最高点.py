#
# @lc app=leetcode.cn id=1765 lang=python3
#
# [1765] 地图中的最高点
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ds = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        dq = deque()
        x, y = len(isWater), len(isWater[0])
        h = [[-1 for _ in range(y)] for _ in range(x)]
        for i in range(x):
            for j in range(y):
                if isWater[i][j] == 1:
                    dq.append((i, j))
                    h[i][j] = 0
        while len(dq) > 0:
            xx, yy = dq.popleft()
            for dx, dy in ds:
                nx, ny = xx + dx, yy + dy
                # 一圈一圈的遍历 不会造成 h1 - h2 > 1 的情况
                if 0 <= nx < x and 0 <= ny < y and h[nx][ny] == -1:
                    h[nx][ny] = h[xx][yy] + 1
                    dq.append((nx, ny))
        return h


# @lc code=end
