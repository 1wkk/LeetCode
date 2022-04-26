from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(v > 0 for li in grid for v in li)
        zx = sum(map(max, grid))
        yz = sum(map(max, zip(*grid)))
        return xy + zx + yz
