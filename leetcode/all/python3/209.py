from cmath import inf
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        l, r, s = 0, 0, 0
        while r < n:
            s += nums[r]
            while s >= target:
                ans = min(ans, r - l + 1)
                s -= nums[l]
                l += 1
            r += 1
        return 0 if ans == inf else ans
