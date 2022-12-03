#
# @lc app=leetcode.cn id=1996 lang=python3
#
# [1996] 游戏中弱角色的数量
#

# @lc code=start
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # 在按照攻击降序，且攻击相同时防御升序排列后，记录最大防御，
        # 假设当前的防御比之前的最大防御小，即可确认当前的是弱角色，
        # 理由是：在相同的攻击内，防御是升序，出现的防御大于当前，肯定是来自于攻击更大的那些组
        properties.sort(key=lambda x: (-x[0], x[1]))
        # print(properties)
        ans = 0
        max_def = 0
        for _, df in properties:
            if df < max_def:
                ans += 1
            else:
                max_def = max(max_def, df)
        return ans


# @lc code=end
