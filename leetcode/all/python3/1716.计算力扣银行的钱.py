#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        ans, wk, day = 0, 1, 1
        for _ in range(n):
            ans += wk + day - 1
            day += 1
            if day == 8:
                day = 1
                wk += 1
        return ans


# @lc code=end
