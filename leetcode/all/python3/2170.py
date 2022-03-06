from collections import Counter
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        e, o, n = Counter(nums[::2]), Counter(nums[1::2]), len(nums)
        ee, oo = e.most_common(2), o.most_common(2)
        if len(ee) < 2:
            ee.append((0, 0))
        if len(oo) < 2:
            oo.append((0, 0))
        if ee[0][0] != oo[0][0]:
            return n - ee[0][1] - oo[0][1]
        else:
            return min(n - ee[0][1] - oo[1][1], n - ee[1][1] - oo[0][1])
