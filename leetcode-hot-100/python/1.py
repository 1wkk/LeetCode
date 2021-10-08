from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            anthor_num = target - num
            if anthor_num in hashmap:
                return [hashmap[anthor_num], index]
            hashmap[num] = index
        return None
