#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        st = set()
        for i, n in enumerate(nums):
            if i > k:
                st.remove(nums[i - k - 1])
            if n in st:
                return True
            st.add(n)
        return False


# @lc code=end
