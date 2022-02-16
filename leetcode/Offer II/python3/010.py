from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 不能用滑动窗口做，因为数据不具备迭代性（持续增加、减小）
        map = defaultdict(lambda: 0)
        map[0] = 1
        _sum, ans = 0, 0
        for num in nums:
            _sum += num
            if _sum - k in map:
                ans += map[_sum - k]
            map[_sum] += 1
        return ans
