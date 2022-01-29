#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        map = defaultdict(lambda: 0)
        for s in s1.split():
            map[s] += 1
        for s in s2.split():
            map[s] += 1
        lt = []
        # print(map)
        for k in map:
            if map[k] == 1:
                lt.append(k)
        return lt


# @lc code=end
