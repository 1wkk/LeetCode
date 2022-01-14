#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start


import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [2, 3, 5]
        set = {1}
        pq = [1]

        for i in range(1, n + 1):
            x = heapq.heappop(pq)
            if i == n:
                return x
            for num in nums:
                t = num * x
                if t not in set:
                    set.add(t)
                    heapq.heappush(pq, t)
        return -1


# @lc code=end
