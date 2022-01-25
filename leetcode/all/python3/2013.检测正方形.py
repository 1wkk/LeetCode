#
# @lc app=leetcode.cn id=2013 lang=python3
#
# [2013] 检测正方形
#

# @lc code=start
from collections import defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        self.cnt = defaultdict(lambda: 0)
        self.s = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.cnt[(x, y)] += 1
        self.s[x].add(y)

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        for yy in self.s[x]:
            if yy != y:
                d = yy - y
                ans += self.cnt[(x, yy)] * self.cnt[(x + d, y)] * self.cnt[(x + d, yy)]
                ans += self.cnt[(x, yy)] * self.cnt[(x - d, y)] * self.cnt[(x - d, yy)]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end
