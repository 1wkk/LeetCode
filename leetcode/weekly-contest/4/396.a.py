from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n, s, f = len(nums), sum(nums), 0
        for i, v in enumerate(nums):
            f += i * v
        ans = f
        for i in range(n - 1):
            f = f + s - n * nums[n - 1 - i]
            ans = max(ans, f)
        return ans
