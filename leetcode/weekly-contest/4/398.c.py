from collections import defaultdict
from random import choice
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.dic = defaultdict(list)
        for i, v in enumerate(nums):
            self.dic[v].append(i)

    def pick(self, target: int) -> int:
        return choice(self.dic[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
