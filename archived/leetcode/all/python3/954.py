from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = Counter(arr)
        for v in sorted(c, key=abs):
            if c[2 * v] < c[v]:
                return False
            c[2 * v] -= c[v]
        return True
