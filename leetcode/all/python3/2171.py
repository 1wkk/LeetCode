from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        return sum(beans) - max(
            (len(beans) - k) * v for k, v in enumerate(sorted(beans))
        )
