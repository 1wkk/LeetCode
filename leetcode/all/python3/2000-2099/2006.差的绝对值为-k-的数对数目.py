#
# @lc app=leetcode.cn id=2006 lang=python3
#
# [2006] 差的绝对值为 K 的数对数目
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        counter = Counter()
        for num in nums:
            ans += counter[num + k] + counter[num - k]
            counter[num] += 1
        return ans


# @lc code=end
