from heapq import nlargest
from itertools import product
from typing import List


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        g = [[] for _ in range(len(scores))]
        for x, y in edges:
            g[x].append((scores[y], y))
            g[y].append((scores[x], x))
        for i, v in enumerate(g):
            g[i] = nlargest(3, v)
        ans = -1
        for x, y in edges:
            for (sa, a), (sb, b) in product(g[x], g[y]):
                if y != a != b != x:
                    ans = max(ans, sa + sb + scores[x] + scores[y])
        return ans