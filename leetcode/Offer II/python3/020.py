class Solution:
    def countSubstrings(self, s: str) -> int:
        _len, ans = len(s), 0

        def is_valid(l, r):
            ans = 0
            while l >= 0 and r < _len and s[l] == s[r]:
                ans, l, r = ans + 1, l - 1, r + 1
            return ans

        for i in range(_len):
            ans += is_valid(i, i)
            ans += is_valid(i, i + 1)

        return ans
