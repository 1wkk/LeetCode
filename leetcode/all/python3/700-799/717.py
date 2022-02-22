from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        l, _len = 0, len(bits) - 1
        while l < _len:
            # l += 1 if bits[l] == 0 else 2
            l += bits[l] + 1  # 0 -> 1, 1 -> 2 abbreviation
        return l == _len
