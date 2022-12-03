from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count, ans = 0, 0
        dic = dict()
        dic[count] = -1
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in dic:
                ans = max(ans, i - dic[count])
            else:
                dic[count] = i
        return ans
