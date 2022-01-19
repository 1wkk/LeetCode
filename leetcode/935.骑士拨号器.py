#
# @lc app=leetcode.cn id=935 lang=python3
#
# [935] 骑士拨号器
#

# @lc code=start
class Solution:
    def knightDialer(self, n: int) -> int:
        # 特殊情况 5
        if n == 1:
            return 10
        n1, n2, n3, n4, n6, n7, n8, n9, n0 = (
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
        )
        for _ in range(n - 1):
            n1, n2, n3, n4, n6, n7, n8, n9, n0 = (
                n6 + n8,
                n7 + n9,
                n4 + n8,
                n3 + n9 + n0,
                n1 + n7 + n0,
                n2 + n6,
                n1 + n3,
                n2 + n4,
                n4 + n6,
            )
        return sum([n1, n2, n3, n4, n6, n7, n8, n9, n0]) % (10 ** 9 + 7)


# @lc code=end
