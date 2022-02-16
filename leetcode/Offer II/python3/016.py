from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _len, l, r, ans = len(s), 0, 0, 0
        ct = defaultdict(lambda: 0)
        while r < _len:
            ct[s[r]] += 1
            while ct[s[r]] > 1:
                ct[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
