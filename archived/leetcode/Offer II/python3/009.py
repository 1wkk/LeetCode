from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        l, r, s = 0, 0, 1
        while r < len(nums):
            s *= nums[r]
            while l < len(nums) and s >= k:
                s //= nums[l]
                l += 1
            if s < k:
                ans += r - l + 1
            r += 1
        return ans
