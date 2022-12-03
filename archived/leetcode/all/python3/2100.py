from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # \ /
        n = len(security)
        l, r = [0 for _ in range(n)], [0 for _ in range(n)]
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                l[i] = l[i - 1] + 1
            if security[n - i - 1] <= security[n - i]:
                r[n - i - 1] = r[n - i] + 1
        return [i for i in range(time, n - time) if l[i] >= time and r[i] >= time]
