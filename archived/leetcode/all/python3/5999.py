from typing import List
from sortedcontainers import SortedList


class Solution:
    def goodTriplets(self, n1: List[int], n2: List[int]) -> int:
        dic = dict()
        for i, v in enumerate(n1):
            dic[v] = i
        ans, sl, _len = 0, SortedList(), len(n2)
        # enumerate y
        for i in range(1, _len - 1):
            sl.add(dic[n2[i - 1]])
            y = dic[n2[i]]
            x = sl.bisect_left(y)
            ans += x * (_len - 1 - y - (i - x))
        return ans
