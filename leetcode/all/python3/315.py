from typing import List
from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        _len = len(nums)
        ans = [0 for _ in range(_len)]
        for i in range(_len - 1, -1, -1):
            ans[i] = sl.bisect_left(nums[i])
            sl.add(nums[i])
        return ans
