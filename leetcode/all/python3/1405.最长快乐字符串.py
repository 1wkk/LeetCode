#
# @lc app=leetcode.cn id=1405 lang=python3
#
# [1405] 最长快乐字符串
#

# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnt.sort(key=lambda x: x[0], reverse=True)
            has_next = False
            for i, (c, ch) in enumerate(cnt):
                if c <= 0:
                    break
                if len(ans) >= 2 and ans[-2] == ch and ans[-1] == ch:
                    continue
                ans.append(ch)
                cnt[i][0] -= 1
                has_next = True
                # 每轮都要退出循环重新选择
                break
            if not has_next:
                return ''.join(ans)


# @lc code=end
