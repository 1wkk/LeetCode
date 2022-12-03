from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # 类似字典树
        ans = [0 for _ in range(n)]
        c = 1
        for i in range(n):
            ans[i] = c
            if c * 10 <= n:
                c *= 10
            else:
                # 回退 backtrack
                while c % 10 == 9 or c + 1 > n:
                    c //= 10
                c += 1
        return ans
