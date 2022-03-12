from collections import defaultdict
from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        graph = defaultdict(list)
        for i in range(1, n):
            graph[parents[i]].append(i)

        f = [0] * n

        def dfs(u):
            ans = 1
            for v in graph[u]:
                ans += dfs(v)
            f[u] = ans
            return ans

        dfs(0)
        ans, mx = 0, 0
        for x in range(n):
            cur = 1
            for v in graph[x]:
                cur *= f[v]
            if x != 0:
                cur *= n - f[x]
            if cur > mx:
                ans, mx = 1, cur
            elif cur == mx:
                ans += 1
        return ans
