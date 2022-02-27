from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        strs = list(map(str, nums))
        _len = len(strs)
        if _len == 1:
            return strs[0]
        elif _len == 2:
            return strs[0] + '/' + strs[1]
        else:
            return strs[0] + '/(' + '/'.join(strs[1:]) + ')'
