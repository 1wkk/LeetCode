#
# @lc app=leetcode.cn id=1447 lang=python3
#
# [1447] 最简分数
#

# @lc code=start
from math import gcd
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [
            f'{j}/{i}' for i in range(2, n + 1) for j in range(1, i) if gcd(j, i) == 1
        ]


# @lc code=end
