from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        r = 1
        cap = 100
        for c in s:
            n = widths[ord(c) - ord('a')]
            if cap >= n:
                cap -= n
            else:
                r += 1
                cap = 100 - n
        return [r, 100 - cap]
