class Solution:
    def binaryGap(self, n: int) -> int:
        ans, pre, i = 0, -1, 0
        while n:
            if n & 1:
                if pre != -1:
                    ans = max(ans, i - pre)
                pre = i
            i, n = i + 1, n >> 1
        return ans
