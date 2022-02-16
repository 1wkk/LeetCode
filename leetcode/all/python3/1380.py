from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rs = [min(i) for i in matrix]
        cs = [max(i) for i in zip(*matrix)]
        return [i for i in rs if i in cs]
