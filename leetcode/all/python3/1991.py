from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        _len = len(nums)
        _prefix = [0 for _ in range(_len + 1)]
        for i in range(_len):
            _prefix[i + 1] = _prefix[i] + nums[i]
        for i in range(1, _len + 1):
            if _prefix[i - 1] == _prefix[_len] - _prefix[i]:
                return i - 1
        return -1
