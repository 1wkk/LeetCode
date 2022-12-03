class Solution:
    def lastRemaining(self, n: int) -> int:
        ans = 1
        flag, step = True, 1
        while n > 1:
            # 首部是否会被删除
            if flag:
                # 从左往右，首部必定被删除
                ans += step
            elif n % 2 == 1:
                # 从右往左，个数为技术时，首部会被删除
                ans += step
            flag = not flag
            n >>= 1
            step <<= 1
        return ans
