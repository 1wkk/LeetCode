#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#

# @lc code=start
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        # 抽屉原理（鸽巢理论）
        if n > 1440:
            return 0
        times = []
        for time in timePoints:
            h, m = int(time[:2]), int(time[-2:])
            times.append(
                h * 60 + m,
            )
            times.append(h * 60 + m + 1440)
        # print(times)
        times.sort()
        # print(times)
        return min(times[i] - times[i - 1] for i in range(1, 2 * n))


# @lc code=end
