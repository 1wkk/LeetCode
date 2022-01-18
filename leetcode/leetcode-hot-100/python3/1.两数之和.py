#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, num in enumerate(nums):
            l = target - num
            if l in dic:
                return [dic[l], i]
            dic[num] = i
        return []


# @lc code=end
