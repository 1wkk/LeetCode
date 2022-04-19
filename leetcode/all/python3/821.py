from cmath import inf
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [inf for _ in range(n)]

        idx = -inf
        for i, v in enumerate(s):
            if v == c:
                idx = i
            ans[i] = i - idx
        idx = inf
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                idx = i
            ans[i] = min(ans[i], idx - i)
        return ans
