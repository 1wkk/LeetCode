from typing import List


class Solution:
    def pancakeSort(self, a: List[int]) -> List[int]:
        c, ans = len(a), []
        while c:
            idx = a.index(c) + 1
            ans.append(idx)
            a = a[:idx][::-1] + a[idx:]
            ans.append(c)
            a = a[:c][::-1] + a[c:]
            c -= 1
        return ans
