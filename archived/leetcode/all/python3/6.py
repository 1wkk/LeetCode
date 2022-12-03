class Solution:
    def convert(self, s: str, n: int) -> str:
        if n < 2:
            return s
        l = ['' for _ in range(n)]
        i, f = 0, -1
        for c in s:
            l[i] += c
            if i == 0 or i == n - 1:
                f = -f
            i += f
        return ''.join(l)
