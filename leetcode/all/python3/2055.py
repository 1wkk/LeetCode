from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        _sum, preSum = 0, [0 for _ in range(n)]

        left, idx = [0 for _ in range(n)], -1
        for i, ch in enumerate(s):
            if ch == '*':
                _sum += 1
            else:
                idx = i
            preSum[i] = _sum
            left[i] = idx

        right, idx = [0 for _ in range(n)], -1
        for i in range(n - 1, -1, -1):
            ch = s[i]
            if ch == '|':
                idx = i
            right[i] = idx

        ans = []
        for l, r in queries:
            ll, rr = right[l], left[r]
            if ll < rr and ll >= 0 and rr >= 0:
                ans.append(preSum[rr] - preSum[ll])
            else:
                ans.append(0)
        return ans
