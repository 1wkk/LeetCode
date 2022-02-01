#
# @lc app=leetcode.cn id=1763 lang=python3
#
# [1763] 最长的美好子字符串
#

# @lc code=start
class Solution:
    # 分治
    def longestNiceSubstring(self, s: str) -> str:
        st = set(s)
        for c in s:
            if c.swapcase() not in st:
                return max(
                    (self.longestNiceSubstring(ss) for ss in s.split(c)), key=len
                )
        return s


# @lc code=end
