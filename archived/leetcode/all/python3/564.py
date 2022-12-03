class Solution:
    def nearestPalindromic(self, n: str) -> str:
        _len = len(n)
        spare_tires = [10 ** (_len - 1) - 1, 10 ** _len + 1]
        # _len + 1, ceil
        _prefix = int(n[: (_len + 1) // 2])
        for x in range(_prefix - 1, _prefix + 2):
            y = x if _len % 2 == 0 else x // 10
            while y:
                x = x * 10 + y % 10
                y //= 10
            spare_tires.append(x)

        ans = -1
        n_int = int(n)
        for tire in spare_tires:
            if tire != n_int:
                if (
                    ans == -1
                    or abs(n_int - tire) < abs(n_int - ans)
                    or (abs(n_int - tire) < abs(n_int - ans) and tire < ans)
                ):
                    ans = tire
        return str(ans)
