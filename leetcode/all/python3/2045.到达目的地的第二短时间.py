#
# @lc app=leetcode.cn id=2045 lang=python3
#
# [2045] 到达目的地的第二短时间
#

# @lc code=start
from cmath import inf
from collections import defaultdict, deque
from typing import List


class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        p = defaultdict(list)
        for x, y in edges:
            p[x].append(y)
            p[y].append(x)
        d = [[inf for _ in range(2)] for _ in range(n + 1)]
        # (node, step)
        q = deque([(1, 0)])
        while d[n][1] == inf:
            x, y = q.popleft()
            for c in p[x]:
                dc = y + 1
                if dc < d[c][0]:
                    d[c][0] = dc
                    q.append((c, dc))
                elif d[c][0] < dc < d[c][1]:
                    d[c][1] = dc
                    q.append((c, dc))
        ans = 0
        for _ in range(d[n][1]):
            # 等红绿灯
            if ans % (2 * change) >= change:
                ans += change * 2 - ans % (2 * change)
            ans += time
        return ans


# @lc code=end
