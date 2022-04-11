class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        a, c = 10, 9
        for i in range(n - 1):
            c *= 9 - i
            a += c
        return a
