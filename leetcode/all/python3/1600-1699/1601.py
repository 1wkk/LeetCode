from itertools import combinations
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        _len = len(requests)
        for i in range(_len, -1, -1):
            for cs in combinations(requests, i):
                _count = [0 for _ in range(n)]
                for f, t in list(cs):
                    _count[f] -= 1
                    _count[t] += 1
                for c in _count:
                    if c != 0:
                        break
                else:
                    return i
        return 0
