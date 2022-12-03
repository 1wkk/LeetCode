from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            _sum = numbers[l] + numbers[r]
            if _sum == target:
                return [l + 1, r + 1]
            elif _sum < target:
                l += 1
            else:
                r -= 1
