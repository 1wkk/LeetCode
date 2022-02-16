class Solution:
    def countOperations(self, n1: int, n2: int) -> int:
        ans = 0
        while n1 and n2:
            ans += 1
            if n1 >= n2:
                n1 -= n2
            else:
                n2 -= n1
        return ans
