from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return (
            [original[i : i + n] for i in range(0, len(original), n)]
            if len(original) == m * n
            else []
        )
