class Solution:
    def arrangeCoins(self, n: int) -> int:
        # (1 + i) * i  / 2 <= n
        return int((pow(8 * n + 1, 0.5) - 1) / 2)
