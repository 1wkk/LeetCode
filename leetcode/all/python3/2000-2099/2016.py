from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans, _min = -1, 10 ** 9 + 1
        for x in nums:
            if x <= _min:
                _min = x
            else:
                ans = max(ans, x - _min)
        return ans
