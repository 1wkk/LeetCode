from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        move = [0] * n
        for i, num in enumerate(nums):
            if num <= i:
                move[0] += 1
                move[(i - num + 1) % n] -= 1
                move[(i + 1) % n] += 1
            else:
                move[(i + 1) % n] += 1
                move[(n - (num - i) + 1) % n] -= 1
        sc, mx, ans = 0, 0, 0
        for i, _sc in enumerate(move):
            sc += _sc
            if sc > mx:
                mx = sc
                ans = i
        return ans
