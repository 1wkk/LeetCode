import functools
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return sorted(
            nums,
            key=functools.cmp_to_key(
                lambda a, b: b - a if abs(a) == abs(b) else abs(a) - abs(b)
            ),
        )[0]
