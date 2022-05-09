from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        lo, hi, ans = 0, n, [0 for _ in range(n)]
        for i, ch in enumerate(s):
            if ch == 'I':
                ans[i], lo = lo, lo + 1
            else:
                ans[i], hi = hi, hi - 1
        return ans
