#
# @lc app=leetcode.cn id=1332 lang=python3
#
# [1332] 删除回文子序列
#

# @lc code=start
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return 2
            l += 1
            r -= 1
        return 1


# @lc code=end
