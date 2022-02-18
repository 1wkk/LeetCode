from cmath import inf
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ct = Counter(text)
        ans = inf
        for c in ('b', 'a', 'l', 'o', 'n'):
            if c in ('b', 'a', 'n'):
                ans = min(ans, ct[c])
            else:
                ans = min(ans, ct[c] // 2)
        return ans
