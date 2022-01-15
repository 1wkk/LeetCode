#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#

# @lc code=start
from heapq import heappop, heappush
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ans, pq = [1] * n, [(primes[i], i, 0) for i in range(len(primes))]
        # print(ans)
        i = 1
        while i < n:
            val, j, idx = heappop(pq)
            if val != ans[i - 1]:
                # print(i)
                ans[i] = val
                i += 1
            heappush(pq, (ans[idx + 1] * primes[j], j, idx + 1))
        return ans[n - 1]


# @lc code=end
