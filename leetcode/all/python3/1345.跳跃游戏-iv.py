#
# @lc app=leetcode.cn id=1345 lang=python3
#
# [1345] 跳跃游戏 IV
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # 构建图
        map = defaultdict(list)
        for i, a in enumerate(arr):
            map[a].append(i)
        # 记录数组某项是否访问过
        vis = set()
        q = deque()
        # [idx, step]
        q.append([0, 0])
        while q:
            idx, step = q.popleft()
            if idx == n - 1:
                return step
            # 当前的值
            v = arr[idx]
            step += 1
            # 相同值的所有索引
            for i in map[v]:
                if i not in vis:
                    vis.add(i)
                    q.append([i, step])
            # 可以省去下一次 for 循环步骤
            del map[v]
            # 后一位
            if idx + 1 < n and (idx + 1) not in vis:
                vis.add(idx + 1)
                q.append([idx + 1, step])
            # 前一位
            if idx - 1 >= 0 and (idx - 1) not in vis:
                vis.add(idx - 1)
                q.append([idx - 1, step])


# @lc code=end
