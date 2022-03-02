class Solution:
    def addDigits(self, n: int) -> int:
        return (n - 1) % 9 + 1 if n else 0
