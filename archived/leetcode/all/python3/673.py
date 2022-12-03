from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n, _max, ans = len(nums), 0, 0
        dp = [1] * n
        cnt = [1] * n
        for i in range(0, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            if dp[i] > _max:
                _max = dp[i]
                ans = cnt[i]
            elif dp[i] == _max:
                ans += cnt[i]
        return ans
