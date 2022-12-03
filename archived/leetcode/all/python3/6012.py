class Solution:
    def countEven(self, num: int) -> int:
        ans = 0

        def calc(x):
            _sum = 0
            while x:
                _sum += x % 10
                x //= 10
            return _sum

        for i in range(1, num + 1):
            if calc(i) % 2 == 0:
                ans += 1
        return ans
